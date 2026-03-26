# 🚁 Drone Detection and Tracking (YOLOv8)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-red)

---

## 📌 Overview

This project detects and tracks drones in video using YOLOv8.

---

## 📊 Dataset

https://www.kaggle.com/datasets/dasmehdixtr/drone-dataset-uav

⚠️ Dataset is not included due to size limitations.

---

## 🧠 Model

* YOLOv8 (Ultralytics)
* Object Detection + Tracking

---

## 🚀 Features

* Real-time drone detection
* Multi-object tracking
* Works on high-speed objects

---

## ⚠️ Limitations

* Occasional tracking loss at high speeds (~200 km/h)
* Small object detection challenges
* Motion blur impact

---

## ⚙️ Project Structure

```bash
project/
├── src/
├── model/
├── data/ (not included)
├── runs/ (not included)
├── README.md
```

---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Train model

```bash
python src/train.py
```

### 3. Run tracking

```bash
python src/track.py
```

---

## 🔮 Example

* Detects drones in video
* Tracks moving objects across frames

---

## 💡 Future Improvements

* Improve tracking stability
* Use YOLOv8x for higher accuracy
* Add custom tracker (DeepSORT / ByteTrack)

---

## 👨‍💻 Author

https://github.com/Zh09-hak
