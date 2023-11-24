from customer_queue.in_bank_queue import Line
from customer_queue.project_enums import Service
from customer_queue.customer import Customer
from typing import List, Dict
from heapq import heappop, heappush


class Branch:
    __slots__ = '__lines', 'branch_id'

    def __init__(self, branch_id):
        self.branch_id = branch_id
        self.__lines: Dict[Service, List[Line]] = dict()

    def add_new_line(self, line_type: Service = Service.TRANSFER) -> None:
        if line_type not in self.__lines:
            self.__lines[line_type] = list()
        self.__lines[line_type].append(Line(line_number=len(self.__lines[line_type]) + 1, line_type=line_type))

    def get_closest_line(self, line_type: Service = Service.TRANSFER) -> Line:
        closet_line = heappop(self.__lines[line_type])
        return closet_line

    def customer_in(self, customer: Customer) -> None:
        line = self.get_closest_line(line_type=customer.service_type)
        line.customer_in(customer=customer)
        heappush(self.__lines[customer.service_type], line)
