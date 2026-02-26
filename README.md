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
