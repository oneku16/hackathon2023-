from enum import Enum


class QueueType(Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    MISTAKEN = "mistaken"


class Service(Enum):
    DEPOSIT = 'deposit'
    TRANSFER = 'transfer'
    LOAN = 'loan'
