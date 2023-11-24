from collections import defaultdict


class CustomerQueue:
    __slots__ = ['__head']

    def __init__(self):
        self.__head = 1
