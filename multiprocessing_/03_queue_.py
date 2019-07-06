#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/6 15:01
# @Author  : yangtao
# @File    : 03_queue_.py
# 跨进程通信

import multiprocessing
import time


def put_(q):
    for value in ['a','b','c']:
        print('发送{}到queue。。。'.format(value))
        q.put(value)
        time.sleep(2)

def get_(q):
    while True:
        value = q.get(True)
        print('从queue接收{}'.format(value))


if __name__ == "__main__":
    q = multiprocessing.Queue()
    pw = multiprocessing.Process(target=put_,args=(q,))
    pr = multiprocessing.Process(target=get_,args=(q,))
    # 启动子进程，写入
    pw.start()
    # 启动子进程pr，读取
    pr.start()
    pw.join()

    #pr 进程是死循环，无法等待其结束；当get无法得到数据时，强制终止
    pr.terminate()
