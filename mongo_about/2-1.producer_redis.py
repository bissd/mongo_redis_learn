#-*- coding:utf-8 -*-

"""
# __author__ = 'hitler'
# time : '2019/4/26 11:50 AM'

#info:
    基于 redis 替换 queue  生产者


"""
import time
import json
import redis
import random
from threading import Thread

class Producer(Thread):
    def __init__(self):
        super().__init__()
        self.queue = redis.Redis()

    def run(self):
        while True:
            a = random.randint(0,10)
            b = random.randint(90,100)
            print(f'生产者 生产两个数字（{a},{b}）')
            self.queue.rpush('producer', json.dumps((a,b)))
            time.sleep(2)


producer = Producer()

producer.start()

while True:
    time.sleep(1)