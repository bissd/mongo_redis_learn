#-*- coding:utf-8 -*-

"""
# __author__ = 'hitler'
# time : '2019/4/26 1:16 PM'

#info:
    消费者 redis

"""
import time
import redis
import json
import random
from threading import Thread


class Consumer(Thread):
    def __init__(self):
        super().__init__()
        self.queue = redis.Redis()

    def run(self):
        while True:
            num_touple = self.queue.blpop('producer')
            a, b = json.loads(num_touple[1].decode())
            print(f'消费者 消费数字 {a} + {b} = {a+b}')
            x = random.randint(0,10)
            print(x)
            time.sleep(x)


consumer = Consumer()

consumer.start()

while True:
    time.sleep(1)