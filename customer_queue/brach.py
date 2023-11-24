from collections import defaultdict, deque
from customer_queue.Exceptions import NoCustomerInQueue


class Line:
    __slots__ = '__queue', '__late'

    def __init__(self):
        self.__queue = deque()
        self.__late = deque()

    def next_customer(self) -> int:
        if self.__late:
            queue_number = self.__late.popleft()
            return queue_number
        if self.__queue:
            queue_number = self.__queue.popleft()
            return queue_number
        raise NoCustomerInQueue

    def customer_in(self, queue_number: int) -> None:
        if self.check_for_late(queue_number):
            self.__late.appendleft(queue_number)
        else:
            self.__queue.appendleft(queue_number)

    def customer_out(self):
        ...

    def check_for_late(self, queue_number: int) -> bool:
        return queue_number < self.__queue[0]


class Branch:
    __slots__ = '__lines', 'branch_id'

    def __init__(self, branch_id):
        self.branch_id = branch_id
        self.__lines = defaultdict(Line)
