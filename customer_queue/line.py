from customer_queue.exceptions import NoCustomerInQueue, NotCustomers
from customer_queue.customer import Customer
from customer_queue.project_enums import Service, QueueType
from heapq import heappop, heappush


class Line:

    slots = 'line_number', 'queue', 'late', 'line_type', 'reference_branch'

    def __init__(self, line_number: int, reference_branch: object, line_type: Service = Service.TRANSFER):
        self.line_number = line_number
        self.line_type = line_type
        self.reference_branch = reference_branch
        self.queue = list()
        self.late = list()
        self.dummy_customer = None
        self.flag = False

    def next_customer(self) -> None:
        if self.late:
            self.dummy_customer = self.late.pop()
        elif self.queue:
            self.dummy_customer = self.queue.pop()
        else:
            raise NoCustomerInQueue

    def start_process(self, customer: Customer) -> None:
        if customer.is_late() and customer.queue_type == QueueType.ONLINE:
            self.late.append(customer)
            self.late.sort(reverse=True)
        else:
            self.queue.append(customer)
            self.queue.sort(reverse=True)

    def close_process(self) -> None:
        current_customer = None
        if self.late:
            current_customer = self.late.pop()
        elif self.queue:
            current_customer = self.queue.pop()
        if current_customer is None:
            return
        else:
            if current_customer.customer_out():
                print(f'Customer on exit {current_customer}')
                self.close_process()

    def __lt__(self, other):
        return len(self.queue) + len(self.late) < len(other.queue) + len(other.late)

    def __repr__(self):
        return f'Line(line_number={self.line_number} {[customer for customer in self.queue + self.late]})'
