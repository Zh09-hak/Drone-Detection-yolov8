import os
import shutil
import random

def split_dataset(source, train_img, val_img, train_lbl, val_lbl):
    os.makedirs(train_img, exist_ok=True)
    os.makedirs(val_img, exist_ok=True)
    os.makedirs(train_lbl, exist_ok=True)
    os.makedirs(val_lbl, exist_ok=True)

    images = [f for f in os.listdir(source) if f.endswith(".jpg")]
    random.shuffle(images)

    split = int(len(images) * 0.8)

    train_images = images[:split]
    val_images = images[split:]

    for img in train_images:
        txt = img.replace(".jpg", ".txt")
        shutil.copy(os.path.join(source, img), train_img)
        shutil.copy(os.path.join(source, txt), train_lbl)

    for img in val_images:
        txt = img.replace(".jpg", ".txt")
        shutil.copy(os.path.join(source, img), val_img)
        shutil.copy(os.path.join(source, txt), val_lbl)

    print("Dataset prepared")
