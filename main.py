from face_recognition.controller import get_user_picture, upload_user_picture
from face_recognition.collection import Collection
from PIL import Image

def plot_picture(file_path):
	print(file_path)
	image = Image.open(file_path)
	image.show()


if __name__ == '__main__':
	collection = Collection()

	# name = 'cool_guys'
	# target = 'eku.ulanov@yandex.com.jpeg'

	name = 'marathon'
	target = 'usainbolt@gmail.com.jpeg'

	# name = 'CENTRAL_ASIAN_TECH_FORUM_2023'
	# rename_image(name)

	for _image in collection.get_faces(name):
		print(_image)

	print(collection.collections)
	# collection.delete_collection(name)

	for file_path in get_user_picture(name, target):
		plot_picture(file_path)
