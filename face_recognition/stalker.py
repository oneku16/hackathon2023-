from os import path
from glob import glob
from .aws_api import face_rekognition_api
from .collection import Collection
from config import REFERENCE_IMAGES, EVENT_IMAGES


def find_faces(collection_name: str, target_name: str):
    collection = Collection()
    full_path = path.join(EVENT_IMAGES, collection_name)
    if not collection.collections or collection_name not in collection.collections:
        collection.create_new_collection(collection_name)

    list_faces_name = glob(f'{full_path}/*.jpg')
    for victim in list_faces_name:
        if victim not in collection.collections:
            collection.add_image(collection_name, victim)
            break

    img_victim = path.join(REFERENCE_IMAGES, target_name)
    faces_info = face_rekognition_api(collection_name, img_victim)
    for face_info in faces_info:
        yield face_info['Face']['ExternalImageId']


def find_text():
    ...


def find_object():
    ...
