import cv2
import time
import os
import yaml
import torch
import logging
from ultralytics import YOLO


# Load config

with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

ROI = (
    config["roi"]["x1"],
    config["roi"]["y1"],
    config["roi"]["x2"],
    config["roi"]["y2"],
)

TRIGGER_TIME = config["trigger_time"]
CAMERA_INDEX = config["camera_index"]
USE_GPU = config["use_gpu"]


# Logging setup

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


# Create events directory

os.makedirs("events", exist_ok=True)


# Load model

device = "cuda" if torch.cuda.is_available() and USE_GPU else "cpu"
logging.info(f"Using device: {device}")

model = YOLO("yolov8n.pt")
model.to(device)

cap = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_V4L2)

if not cap.isOpened():
    logging.error("Camera not opened")
    exit()

track_timers = {}

while True:
    ret, frame = cap.read()
    if not ret:
        logging.warning("Frame not received")
        break

    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml",
        device=0 if device == "cuda" else "cpu",
        classes=[0],
        verbose=False,
    )

    annotated = results[0].plot()

    x1, y1, x2, y2 = ROI
    cv2.rectangle(annotated, (x1, y1), (x2, y2), (0, 255, 0), 2)

    if results[0].boxes.id is not None:
        for box, track_id in zip(results[0].boxes.xyxy, results[0].boxes.id):

            tx1, ty1, tx2, ty2 = map(int, box)
            cx = (tx1 + tx2) // 2
            cy = (ty1 + ty2) // 2
            tid = track_id.item()

            if x1 < cx < x2 and y1 < cy < y2:
                if tid not in track_timers:
                    track_timers[tid] = time.time()
                else:
                    elapsed = time.time() - track_timers[tid]
                    if elapsed > TRIGGER_TIME:
                        filename = f"events/event_{tid}_{int(time.time())}.jpg"
                        cv2.imwrite(filename, frame)
                        logging.info(f"Event saved: {filename}")
                        track_timers.pop(tid)
            else:
                track_timers.pop(tid, None)

    cv2.imshow("AI Monitor", annotated)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()