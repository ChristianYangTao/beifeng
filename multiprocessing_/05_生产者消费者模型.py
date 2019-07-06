#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/6 15:30
# @Author  : yangtao
# @File    : 05_生产者消费者模型.py

import threading
import time
import queue


q = queue.Queue(maxsize=10)
def producer(name):
    count = 1
    while True:
        q.put("骨头{}".format(count))
        print('生产了骨头{}  {}'.format(count,time.ctime()))
        count += 1
        time.sleep(0.5)


def consumer(name):
    while True:
        print('{}取到{}并且吃了它。。。。 {}'.format(name,q.get(),time.ctime()))
        time.sleep(1)

p = threading.Thread(target=producer,args=("tim",))
c1 = threading.Thread(target=consumer,args=("king",))
c2 = threading.Thread(target=consumer,args=("wang",))
p.start()
c1.start()
c2.start()
