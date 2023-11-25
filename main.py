from customer_queue.brach import Branch
from customer_queue.customer import Customer
from customer_queue.line import Line
from customer_queue.project_enums import Service, QueueType
from datetime import datetime
from heapq import heappop


def main():
    branch_naryn = Branch('Naryn-Main')
    # branch_naryn.add_new_line(branch_naryn, Service.DEPOSIT)
    branch_naryn.add_new_line(branch_naryn, Service.TRANSFER)
    customers: list[Customer] = [
            Customer(customer_id='1',
                     in_queue=datetime(2023, 11, 25, 12, 50, 00),
                     service_type=Service.TRANSFER,
                     queue_type=QueueType.OFFLINE),
            Customer(customer_id='2',
                     in_queue=datetime(2023, 11, 25, 13, 30, 00),
                     service_type=Service.TRANSFER,
                     queue_type=QueueType.ONLINE),
            Customer(customer_id='3',
                     in_queue=datetime(2023, 11, 25, 13, 00, 00),
                     service_type=Service.TRANSFER,
                     queue_type=QueueType.ONLINE),
    ]

    # customers.sort()
    # print(customers)

    # while customers:
    #     print(heappop(customers))

    for customer in customers:
        branch_naryn.customer_in(customer=customer)

    for line_key, line_values in branch_naryn.lines.items():
        print(type(line_values))
        while line_values:
            line = line_values.pop()
            while line:
                line.close_process()


if __name__ == '__main__':
    main()

# from face_recognition.controller import get_user_picture, upload_user_picture
# from face_recognition.collection import Collection
# from PIL import Image
# from time import sleep
# from config import REFERENCE_IMAGES
#
#
# def plot_picture(file_path):
#     image = Image.open(file_path)
#     sleep(1)
#     image.show()
#
#
# if __name__ == '__main__':
#     collection = Collection()
#
#     name = 'cool_guys'
#     target = 'eku.ulanov@yandex.com.jpeg'
#
#     # name = 'marathon'
#     # target = 'usainbolt@gmail.com.jpeg'
#
#     # name = 'CENTRAL_ASIAN_TECH_FORUM_2023'
#     # target = 'chubak.temirov@gmail.com.jpeg'
#     # print(collection.create_new_collection('cool_guys'))
#     # print(collection.collection_exists('cool_guys'))
#     # print(collection.add_image('cool_guys', 'D:\Projects\hackathon2023-\media_base\event_images\cool_guys\photo_10_2023-04-20_06-59-31.jpg'))
#     # for _image in collection.get_faces(name):
#     #     print(_image)
#     #
#     # print(collection.collections)
#     # # collection.delete_collection(name)
#     #
#     # found_pictures = get_user_picture(name, target)
#     # # print(found_pictures)
#     # for _file_path in found_pictures:
#     #     plot_picture(_file_path)
