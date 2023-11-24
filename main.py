from face_recognition.controller import get_user_picture, upload_user_picture
from face_recognition.collection import Collection
from PIL import Image
from time import sleep
from config import REFERENCE_IMAGES


def plot_picture(file_path):
    image = Image.open(file_path)
    sleep(1)
    image.show()


if __name__ == '__main__':
    collection = Collection()

    name = 'cool_guys'
    target = 'eku.ulanov@yandex.com.jpeg'

    # name = 'marathon'
    # target = 'usainbolt@gmail.com.jpeg'

    # name = 'CENTRAL_ASIAN_TECH_FORUM_2023'
    # target = 'chubak.temirov@gmail.com.jpeg'
    # print(collection.create_new_collection('cool_guys'))
    # print(collection.collection_exists('cool_guys'))
    # print(collection.add_image('cool_guys', 'D:\Projects\hackathon2023-\media_base\event_images\cool_guys\photo_10_2023-04-20_06-59-31.jpg'))
    # for _image in collection.get_faces(name):
    #     print(_image)
    #
    # print(collection.collections)
    # # collection.delete_collection(name)
    #
    # found_pictures = get_user_picture(name, target)
    # # print(found_pictures)
    # for _file_path in found_pictures:
    #     plot_picture(_file_path)
