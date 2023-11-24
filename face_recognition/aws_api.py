import boto3
from tools.image_tools import get_image
from typing import List


def face_rekognition_api(collection_name: str, victim: str) -> List[dict]:
    client = boto3.client('rekognition')
    detected_faces = client.search_faces_by_image(CollectionId=collection_name, Image={'Bytes': get_image(victim)})
    return detected_faces['FaceMatches']


def text_ract_api():
    ...


def polly_api():
    ...
