#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/6 15:18
# @Author  : yangtao
# @File    : 04_pipe_.py
# 左边接收，右边发送
import multiprocessing
import time


def send_(q):
    for value in ['a','b','c']:
        print('发送{}到pipe。。。，{}'.format(value,time.ctime()))
        q[1].send(value)
        time.sleep(2)


def recv_(q):
    while True:
        value = q[0].recv()
        print('从pipe接收{}   {}'.format(value,time.ctime()))


if __name__ == "__main__":
    p = multiprocessing.Pipe(duplex=False)
    pw = multiprocessing.Process(target=send_,args=(p,))
    pr = multiprocessing.Process(target=recv_,args=(p,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
