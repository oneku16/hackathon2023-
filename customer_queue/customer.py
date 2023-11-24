from datetime import datetime
from customer_queue.project_enums import Status, Service


class Customer:
    __slots__ = 'customer_id',  'service_type', 'in_queue', 'status', 'time_in', 'time_out', 'queue_type'

    def __init__(self,
                 customer_id: str,
                 in_queue: datetime,
                 service_type: Service = Service.TRANSFER,
                 queue_type: Status = Status.ONLINE,
                 ):
        self.customer_id = customer_id
        self.in_queue = in_queue
        self.service_type = service_type
        self.status = False
        self.time_in: datetime = datetime.now()
        self.time_out: datetime = ...
        self.queue_type = queue_type

    def customer_out(self) -> None:
        self.time_out = datetime.now()

    def is_late(self) -> bool:
        return self.in_queue.time() < self.time_in.time()

    def __lt__(self, other):
        return self.in_queue < other.in_queue

