from face_recognition.controller import get_user_picture, upload_user_picture
from face_recognition.collection import Collection

if __name__ == '__main__':
	collection = Collection()
	# print(collection.get_faces('cool_guys'))
	# collection.delete_collection('cool_guys')
	# print(collection.get_faces('cool_guys'))

	print(get_user_picture('cool_guys', 'eku.ulanov@yandex.com'))
	# print(upload_user_picture('new_file', '123', image))
