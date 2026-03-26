from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")

model.track(
    source="video.mp4",
    show=True,
    save=True
)
