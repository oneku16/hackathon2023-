from customer_queue.line import Line
from customer_queue.project_enums import Service
from customer_queue.customer import Customer
from typing import List, Dict
from heapq import heappop, heappush
from collections import defaultdict


class Branch:
    __slots__ = '__lines', 'branch_id'

    def __init__(self, branch_id: str):
        self.branch_id: str = branch_id
        self.__lines: Dict[Service, List[Line]] = defaultdict(list)

    @property
    def lines(self) -> Dict[Service, List[Line]]:
        return self.__lines

    def is_empty(self, line_type) -> bool:
        return len(self.__lines[line_type]) == 0

    def add_new_line(self, reference_branch: object, line_type: Service = Service.TRANSFER) -> None:
        self.__lines[line_type].append(Line(line_number=len(self.__lines[line_type]) + 1, line_type=line_type, reference_branch=reference_branch))

    def get_closest_line(self, line_type: Service = Service.TRANSFER) -> Line:
        # print(f'25: {line_type=} || {self.__lines.keys()}')
        closet_line = heappop(self.__lines[line_type])
        return closet_line

    def customer_in(self, customer: Customer) -> None:
        line = self.get_closest_line(line_type=customer.service_type)
        line.start_process(customer=customer)
        heappush(self.__lines[customer.service_type], line)

    def customer_out(self, line_number, line_type) -> None:
        # print(f'{line_number=} {line_type=}')
        # print(self.__lines[line_type])
        ...

    def __repr__(self):
        return f'Branch(branch_id={self.branch_id}, lines=[{self.__lines}])'
