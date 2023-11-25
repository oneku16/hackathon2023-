from customer_queue.brach import Branch
from customer_queue.customer import Customer
from customer_queue.project_enums import Service, QueueType
from datetime import datetime
from face_recognition.collection import Collection
from config import MEDIA
from os import path
import psycopg2 as pg


def send_report():
    try:
        conn = pg.connect(
            host='localhost',
            database='postgres',
            port=5432,
            user='admin',
            password='secret'
        )
        print("Connection established.")
        cur = conn.cursor()
        # cur.execute("""
        #     CREATE TABLE IF NOT EXISTS Users(
        #         customerId SERIAL PRIMARY KEY,
        #         city VARCHAR(128),
        #         serviceType VARCHAR(128),
        #         queueType VARCHAR(128),
        #         branch VARCHAR(64),
        #         date DATE,
        #         confirmationCode VARCHAR(64)
        #     """)

        conn.commit()
        try:
            cur.execute("""
            SELECT name FROM Picture;
            """)
            path_name = cur.fetchall()
            print(f'{path_name=}')

        except Exception as error:
            print('Something went wrong!')
        print('Going to update Picture table.')
        # cur.execute(f"""
        # INSERT INTO Picture (id, name) VALUES ({cnt}, '{name[0]}');
        # """)


    except Exception as err:
        raise err


    branch_naryn = Branch('Naryn-Main')
    branch_naryn.add_new_line(branch_naryn, Service.DEPOSIT)
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

    for customer in customers:
        branch_naryn.customer_in(customer=customer)

    for line_key, line_values in branch_naryn.lines.items():
        print(line_values)
        if line_values:
            while line_values:
                line = line_values.pop()
                while line.queue + line.late:
                    line.close_process()
                    print(f'{line=}')


def face():
    collection = Collection()
    # collection.delete_collection('customers')
    # collection.create_new_collection('customers')
    # collection.add_image('customers', path.join(MEDIA, 'collections', 'customers', '98765432.jpg'))
    # print(len(collection.get_faces('customers')))

if __name__ == '__main__':
    send_report()
    # face()

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
