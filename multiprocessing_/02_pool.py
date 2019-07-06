#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/6 9:13
# @Author  : yangtao
# @File    : 02_pool.py
# 进程池
import multiprocessing
import os
import time


def work1(n):
    print("run work {},work id {}".format(n,os.getpid()))
    time.sleep(2)
    print("work {} stop,work id {}".format(n,os.getpid()))


if __name__ == "__main__":
    print("Parent process {}".format(os.getpid()))
    p = multiprocessing.Pool(3)
    for i in range(10):
        p.apply_async(work1,args=(i,))
    p.close()
    p.join()