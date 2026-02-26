# Edge AI Monitoring System

Real-time edge AI video monitoring system with person detection, tracking and event trigger logic.

## Features

- Real-time object detection (YOLOv8)
- Multi-object tracking (ByteTrack)
- ROI-based monitoring
- Time-based trigger (>3 seconds in zone)
- Automatic event snapshot saving
- GPU acceleration (CUDA)
- Configurable via YAML
- Structured logging
- Docker-ready

---

## Architecture

Camera → YOLO Detection → ByteTrack Tracking  
→ ROI Filter → Timer per Track ID  
→ Trigger → Save Event Image

---

## Technologies

- Python 3.12
- PyTorch (CUDA)
- Ultralytics YOLOv8
- ByteTrack
- OpenCV
- NVIDIA RTX 3050
- Ubuntu 24
- Docker

---

## Project Structure
ai-monitor/
│
├── main.py
├── config/
│ └── config.yaml
├── events/
├── requirements.txt
├── Dockerfile
└── README.md

---

## Configuration

Edit:
config/config.yaml

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

## Run
python main.py

## Tested on:

NVIDIA RTX 3050 (4GB)
~50 FPS
~1.2GB VRAM usage