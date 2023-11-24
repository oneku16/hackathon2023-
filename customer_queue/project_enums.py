from enum import Enum


class Status(Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    MISTAKEN = "mistaken"


class Service(Enum):
    DEPOSIT = 'deposit'
    TRANSFER = 'transfer'
    LOAN = 'loan'
