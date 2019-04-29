#-*- coding:utf-8 -*-

"""
# __author__ = 'hitler'
# time : '2019/4/26 11:32 AM'

#info:

    生产者 消费者 模型

"""

import time
import random
from queue import Queue
from threading import Thread

class Producer(Thread):                                                     # 生产者
    def __init__(self,queue):
        super().__init__()                                                  # 显示调用复类的初始化方法
        self.queue = queue

    def run(self):
        while True:
            a = random.randint(1,10)
            b = random.randint(90,100)
            print(f'生产者 生产数字 （{a}, {b}）')
            self.queue.put((a, b))                                          # 生成的随机数 放入队列
            time.sleep(2)


class Consumer(Thread):                                                     # 消费者
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            num_tuple = self.queue.get(block=True)                          # block=True 队列为空时阻塞   直到队列有数据为止
            sum_a_b = sum(num_tuple)
            print(f'消费者 消费了一组数, {num_tuple[0]}+{num_tuple[1]}={sum_a_b}')
            time.sleep(random.randint(0,10))                                # 暂停随机时间  10s 内

queue = Queue()

producer = Producer(queue)
consumer = Consumer(queue)

# 启动子线程
producer.start()
consumer.start()
while True:
    time.sleep(1)




"""
    待考虑问题
    队列状态查看/持久化/新加消费者
"""