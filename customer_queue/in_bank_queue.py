from customer_queue.Exceptions import NoCustomerInQueue
from customer_queue.customer import Customer
from customer_queue.project_enums import Service
from heapq import heappop, heappush


class Line:
    slots = 'line_number', 'queue', 'late', 'line_type'

    def __init__(self, line_number: int, line_type: Service = Service.TRANSFER):
        self.line_number = line_number
        self.line_type = line_type
        self.queue = list()
        self.late = list()
        self.current_customer = None

    def next_customer(self) -> Customer:
        if self.late:
            self.current_customer = heappop(self.late)
        if self.queue:
            self.current_customer = heappop(self.queue)
        if self.current_customer:
            return self.current_customer
        raise NoCustomerInQueue

    def customer_in(self, customer: Customer) -> None:
        if self.current_customer is None:
            self.current_customer = customer
        if customer.is_late():
            heappush(self.late, customer)
        else:
            heappush(self.queue, customer)

    def customer_out(self) -> Customer:
        print(f'customer_out={self.current_customer}')
        return self.current_customer

    def __lt__(self, other):
        return len(self.queue) + len(self.late) < len(other.queue) + len(other.late)
