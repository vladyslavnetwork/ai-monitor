# Edge AI Monitoring System

Real-time edge AI video monitoring system with person detection, tracking and event-trigger logic.

This project demonstrates a production-style computer vision pipeline running on GPU with configurable ROI monitoring and time-based event activation.

---

## Features

* Real-time object detection (YOLOv8)
* Multi-object tracking (ByteTrack)
* ROI-based monitoring zone
* Time-based trigger (> configurable seconds in zone)
* Automatic event snapshot saving
* YAML-based configuration
* Structured logging
* GPU acceleration (CUDA)
* Docker-ready architecture

---

## System Architecture

Camera
→ YOLO Detection
→ ByteTrack Tracking (unique IDs)
→ ROI Filter
→ Per-object Timer
→ Trigger (>N seconds)
→ Save Event Image

---

## Technologies

* Python 3.12
* PyTorch (CUDA)
* Ultralytics YOLOv8
* ByteTrack
* OpenCV
* YAML configuration
* NVIDIA RTX 3050
* Ubuntu 24
* Docker

---

## Project Structure

```
ai-monitor/
│
├── main.py
├── config/
│   └── config.yaml
├── events/              # auto-created
├── screenshots/
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## Configuration

All runtime parameters are defined in:

```
config/config.yaml
```

Example:

```yaml
roi:
  x1: 200
  y1: 100
  x2: 900
  y2: 600

trigger_time: 3
camera_index: 0
use_gpu: true
```

Parameters:

* `roi` — monitoring zone (pixels)
* `trigger_time` — seconds inside ROI before event fires
* `camera_index` — camera device index
* `use_gpu` — enable CUDA acceleration

---

## Run Locally

Create virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

Press `q` to exit.

---

## Docker

Build:

```bash
docker build -t ai-monitor .
```

Run with GPU:

```bash
docker run --gpus all \
  --device=/dev/video0 \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  ai-monitor
```

---

## Performance

Tested on:

* NVIDIA RTX 3050 (4GB VRAM)
* ~40–70 FPS
* ~1–1.5 GB VRAM usage
* Real-time multi-object tracking

---

## Example Use Cases

* Edge AI monitoring
* Intrusion detection systems
* Smart perimeter control
* Industrial safety monitoring
* Prototype defense-grade video analytics

---

## Screenshots

Add images inside `screenshots/` and reference them here:

```markdown
![Detection](screenshots/detection.png)
![Trigger Event](screenshots/trigger.png)
```

---

## Future Improvements

* Headless mode
* REST API integration
* Telegram/HTTP alerts
* Database event logging
* Multi-camera support
* Docker Compose deployment

---

## License

MIT License
