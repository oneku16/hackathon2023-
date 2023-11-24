from datetime import datetime
from customer_queue.queue_types import Status


class Customer:
    __slots__ = 'customer_id', 'in_queue', 'status', 'time_in', 'time_out', 'queue_type'

    def __init__(self, customer_id: str, in_queue: datetime, queue_type: Status = Status.ONLINE):
        self.customer_id = customer_id
        self.in_queue = in_queue
        self.status = False
        self.time_in: datetime = datetime.now()
        self.time_out = None
        self.queue_type = queue_type

    def customer_out(self) -> None:
        self.time_out = datetime.now()

    def is_late(self) -> bool:
        return self.in_queue.time() < self.time_in.time()

    def __eq__(self, other):
        if not isinstance(other, Customer):
            return NotImplemented

        return self.in_queue == other.in_queue

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Customer):
            return NotImplemented

        return self.in_queue < other.in_queue

    def __le__(self, other):
        if not isinstance(other, Customer):
            return NotImplemented

        return self.in_queue <= other.in_queue

    def __gt__(self, other):
        if not isinstance(other, Customer):
            return NotImplemented

        return self.in_queue > other.in_queue

    def __ge__(self, other):
        if not isinstance(other, Customer):
            return NotImplemented

        return self.in_queue >= other.in_queue
