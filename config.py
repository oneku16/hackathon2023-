import os

current_dir = os.path.dirname(os.path.abspath(__file__))

MEDIA = os.path.join(current_dir, 'media_base')

CASCADE_CLASSIFIER = 'cascades/data/haarcascade_frontalface_alt2.xml'

REFERENCE_IMAGES = os.path.join(MEDIA, 'reference_images')
EVENT_IMAGES = os.path.join(MEDIA, 'event_images')
DATE_BASE = 'account/users.db'
