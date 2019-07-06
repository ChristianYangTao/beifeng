#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/5 17:28
# @Author  : yangtao
# @File    : 多线程.py
import time
import multiprocessing_
# import threading.Thread


def music(name,loop,lock):
    lock.acquire()
    for i in range(loop):
        print("listen music {} {}".format(name,time.ctime()))
        time.sleep(1)
    lock.release()

def movie(name,loop,lock):
    lock.acquire()
    for i in range(loop):
        print("look movie {} {}".format(name,time.ctime()))
        time.sleep(1)
    lock.release()


if __name__ == "__main__":
    lock = multiprocessing_.Lock()
    t1 = multiprocessing_.Process(target=music, args=("爱转角", 5, lock))
    t2 = multiprocessing_.Process(target=movie, args=("小王子", 4, lock))


    t1.start()
    t2.start()
