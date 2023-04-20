import cv2
import os
from re import split
import requests
from config import CASCADE_CLASSIFIER, REFERENCE_IMAGES
from PIL import Image


def cut_picture(target_picture: str, scale_w=2.5, scale_h=2.5):
    img = cv2.imread(target_picture)
    width = img.shape[0] // scale_w
    height = img.shape[1] // scale_h
    resized_img = cv2.resize(img, (height, width))
    cv2.imwrite(target_picture, resized_img)

def extract_file_name(file_name: str) -> str:
    return split('[\\\/]', file_name)[-1]

def get_image_from_url(image_url: str):
    image_bytes = requests.get(image_url).content
    return image_bytes

def get_image_from_file(file_name: str):
    with open(file_name, 'rb') as image_file:
        return image_file.read()

def get_image(img_name: str) -> Image:
    return get_image_from_url(img_name) if img_name.lower().startswith('http') else get_image_from_file(img_name)


def save_image(image: Image, file_name: str) -> None:
    image.save(os.path.join(REFERENCE_IMAGES, file_name))


class ImageEditor:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(CASCADE_CLASSIFIER)
        self.image_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), REFERENCE_IMAGES)

    def run_scissors(self):
        for root, dirs, files in os.walk(self.image_dir):
            for file in files:
                if file.endswith("jpeg") or file.endswith("JPG"):
                    path_to_target = os.path.join(root, file)
                    self.cut_faces(path_to_target)
                    cut_picture(path_to_target)

    def cut_faces(self, target_picture: str):
        img = cv2.imread(target_picture)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face = self.face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        for (x, y, w, h) in face:
            roi_gray = gray[y: y + h, x: x + w]
            cv2.imwrite(target_picture, roi_gray)
