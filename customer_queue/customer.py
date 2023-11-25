from datetime import datetime
from customer_queue.project_enums import QueueType, Service
import psycopg2 as pg
from typing import Literal


class Customer:
    __slots__ = ('customer_id',
                 'service_type',
                 'in_queue',
                 'status',
                 'time_in',
                 'time_out',
                 'queue_type',)

    def __init__(self,
                 customer_id: str,
                 in_queue: datetime,
                 status: Literal['GOLD', 'SILVER', 'PLATINUM', 'REGULAR'] = 'REGULAR',
                 service_type: Service = Service.TRANSFER,
                 queue_type: QueueType = QueueType.ONLINE,
                 ):
        self.customer_id = customer_id
        self.in_queue = in_queue
        self.service_type = service_type
        self.status = status
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

        # try:
        #     conn = pg.connect(
        #         host='localhost',
        #         database='postgres',
        #         port=5432,
        #         user='admin',
        #         password='secret')
        #
        #     curr = conn.cursor()
        #
        #     curr.execute("""
        #
        #     CREATE TABLE IF NOT EXISTS BankServices (
        #     id SERIAL PRIMARY KEY,
        #     customer_id VARCHAR(255),
        #     in_queue TIMESTAMP NOT NULL,
        #     service_type VARCHAR(50) DEFAULT 'TRANSFER',
        #     status status NOT NULL,
        #     time_in TIMESTAMP NOT NULL DEFAULT '2023-11-25 12:00:00',
        #     time_out TIMESTAMP,
        #     queue_type VARCHAR(50) DEFAULT 'ONLINE');""")
        #
        #     conn.commit()
        #     curr.execute(f"""
        #     INSERT INTO your_table_name (customer_id, in_queue, service_type, status, time_in, time_out, queue_type )
        #     VALUES ('{self.customer_id}', '{self.in_queue}', f'{self.service_type}', {self.status}, '{self.time_in}', '{self.time_out}', '{self.queue_type}');""")
        #     conn.commit()
        #
        # except Exception as err:
        #     print('something went wrong!')

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
