import cv2
import os
from config import MEDIA
import time
from face_recognition.stalker import find_faces
import psycopg2 as pg


def take_pic(collection: str = 'customers'):
    seen = set()
    cnt = 1
    capture = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
    image_dir = os.path.join(MEDIA, 'reference_images')
    while True:
        ret, image = capture.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        for (x, y, w, h) in faces:
            roi_gray = gray[y: y + h, x: x + w]
            roi_color = image[y: y + h, x: x + w]
            target = os.path.join(image_dir, 'target.jpeg')
            cv2.imwrite(os.path.join(image_dir, 'target.jpeg'), roi_color)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            name = list(find_faces(collection_name=collection, target_name=target))

            if name and name[0] not in seen:
                seen.add(name[0])
                cnt += 1
                try:
                    conn = pg.connect(
                        host='localhost',
                        database='postgres',
                        port=5432,
                        user='admin',
                        password='secret'
                    )
                    print("Connection established.")

                    # here fetch data about target, send it to service provider
                    curr = conn.cursor()

                    curr.execute(f"""SELECT * FROM Users AS U WHERE U.user_id = f{name[0]}""")


                    # cur = conn.cursor()
                    # cur.execute(
                    #     """
                    #     CREATE TABLE IF NOT EXISTS Picture(
                    #     id SERIAL PRIMARY KEY,
                    #     name VARCHAR(255)
                    #     );""")
                    #
                    # conn.commit()
                    # print('Going to update Picture table.')
                    # cur.execute("""DELETE FROM Picture;""")
                    # cur.execute(f"""
                    # INSERT INTO Picture (id, name) VALUES ({cnt}, '{name[0]}');
                    # """)


                except Exception as err:
                    raise err

        cv2.imshow('look_at_me', image)
        time.sleep(1)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()


take_pic()