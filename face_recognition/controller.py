from .stalker import find_faces
from config import EVENT_IMAGES, REFERENCE_IMAGES
from PIL import Image
import os
import pathlib


def get_user_picture(collection_name, user_picture):
    """returns list of path to matched images"""
    if not user_picture.endswith('.jpeg') and not user_picture.endswith('jpg'):
        user_picture += '.jpeg'

    def _wrapper():
        for image in find_faces(collection_name=collection_name, target_name=user_picture):
            yield os.path.join(EVENT_IMAGES, collection_name, image)

    matched_images = list(_wrapper())
    # for file in os.listdir(REFERENCE_IMAGES):
    # 	os.remove(os.path.join(REFERENCE_IMAGES, file))

    return matched_images


def upload_user_picture(image_name, image: Image, collection_name=None):
    """uploads picture and pictures to collection depending on status"""
    if collection_name:
        file_path = pathlib.Path(os.path.join(EVENT_IMAGES, collection_name))
        if not file_path.is_dir():
            os.mkdir(file_path)
    else:
        file_path = pathlib.Path(os.path.join(REFERENCE_IMAGES))
    image.save(os.path.join(file_path, image_name + '.jpg'))
