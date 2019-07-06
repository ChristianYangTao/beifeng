#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/5 16:19
# @Author  : yangtao
# @File    : 单线程.py

import time
import threading


def music(name,loop):
    for i in range(loop):
        print("listen music {} {}".format(name,time.ctime()))
        time.sleep(1)


def movie(name,loop):
    for i in range(loop):
        print("look movie {} {}".format(name,time.ctime()))
        time.sleep(1)


if __name__ == "__main__":
    music("爱转角",5)
    movie("小王子",4)
    print("end time",time.ctime())
