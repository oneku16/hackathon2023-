import boto3
from tools.image_tools import extract_file_name, get_image
from typing import List
from botocore.exceptions import ClientError


class Collection:
    __slots__ = '__client',

    def __init__(self):
        self.__client = boto3.client('rekognition')

    @property
    def collections(self) -> List[str]:
        response = self.__client.list_collections()
        result = []
        while True:
            collections = response['CollectionIds']
            result.extend(collections)
            if 'NextToken' in response:
                next_token = response['NextToken']
                response = self.__client.list_collections(NextToken=next_token)
            else:
                break
        return result

    def collection_exists(self, collection_name: str) -> bool:
        return collection_name in self.collections

    def create_new_collection(self, collection_name: str):
        if not self.collection_exists(collection_name):
            response = self.__client.create_collection(CollectionId=collection_name)
            if response['StatusCode'] != 200:
                raise f'Could not create collection, {collection_name}, status code: {str(response["StatusCode"])}'

    def delete_collection(self, collection_name: str):
        try:
            self.__client.delete_collection(CollectionId=collection_name)
        except ClientError as exception:
            raise exception.response['Error']['Code']

    def get_faces(self, collection_name: str) -> List[dict]:
        response = self.__client.list_faces(CollectionId=collection_name)
        tokens = True
        result = []
        while tokens:
            faces = response['Faces']
            result.extend(faces)
            if 'NextToken' in response:
                next_token = response['NextToken']
                response = self.__client.list_faces(CollectionId=collection_name, NextToken=next_token)
            else:
                tokens = False
        return result

    def add_image(self, collection_name: str, image_path: str):
        target_pic = self.__client.index_faces(CollectionId=collection_name, Image={'Bytes': get_image(image_path)},
                                               ExternalImageId=extract_file_name(image_path))
        if not target_pic['FaceRecords']:
            raise Exception('No face found in the image')
