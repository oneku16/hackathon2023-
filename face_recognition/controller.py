from .stalker import find_faces
from config import EVENT_IMAGES
from PIL import Image
import os
import pathlib


def get_user_picture(collection_name, user_picture):
	if not user_picture.endswith('.jpeg') and not user_picture.endswith('jpg'):
		user_picture += '.jpeg'

	def _wrapper():
		for image in find_faces(collection_name=collection_name, target_name=user_picture):
			yield os.path.join(EVENT_IMAGES, image)

	return list(_wrapper())

def upload_user_picture(collection_name: str, image_name, image: Image):
	file_path = pathlib.Path(os.path.join(EVENT_IMAGES, collection_name))
	if not file_path.is_dir():
		os.mkdir(file_path)

	image.save(os.path.join(file_path, image_name + '.jpg'))




