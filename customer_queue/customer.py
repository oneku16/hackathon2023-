from datetime import datetime
from customer_queue.project_enums import QueueType, Service


class Customer:
    __slots__ = ('customer_id',
                 'service_type',
                 'in_queue',
                 'status',
                 'time_in',
                 'time_out',
                 'queue_type')

    def __init__(self,
                 customer_id: str,
                 in_queue: datetime,
                 service_type: Service = Service.TRANSFER,
                 queue_type: QueueType = QueueType.ONLINE,
                 ):
        self.customer_id = customer_id
        self.in_queue = in_queue
        self.service_type = service_type
        self.status = False
        self.time_in: datetime = datetime(2023, 11, 25, 12, 00, 00)  # datetime.now()
        self.time_out: datetime = ...
        self.queue_type = queue_type

    def customer_out(self) -> bool:
        self.time_out = datetime.now()
        print(30, self.__repr__())
        print(self.time_in, self.in_queue)
        user = input('done?')
        while user != 'yes':
            user = input('done?')

        self.status = True
        return True

    def is_late(self) -> bool:
        return self.in_queue.time() < self.time_in.time()

    def __lt__(self, other):
        print(self.in_queue, other.in_queue, self.in_queue <= other.in_queue)
        return self.in_queue <= other.in_queue

    def __str__(self):
        return f'customer_id={self.customer_id}'

    def __repr__(self):
        return f'Customer({self.customer_id=}{self.service_type=} {self.queue_type=} {self.in_queue})'.replace('self.', '')
