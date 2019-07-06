#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/5 17:28
# @Author  : yangtao
# @File    : 多线程.py
import time
import threading
# import threading.Thread


def music(name,loop):
    for i in range(loop):
        print("listen music {} {} {}".format(name,time.ctime(),threading.Thread.getName(t1)))
        time.sleep(1)


def movie(name,loop):
    for i in range(loop):
        print("look movie {} {} {}".format(name,time.ctime(),threading.Thread.name))
        time.sleep(1)


# 创建多线程
t1 = threading.Thread(target=music,args=("爱转角",5))
t1.setName("线程1")
t2 = threading.Thread(target=movie,args=("小王子",4),)
# t2.setName("线程2")


if __name__ == "__main__":
    # 守护主线程   主线程结束，杀死子线程
    t1.setDaemon(True)
    t2.setDaemon(True)

    # 启动线程
    t1.start()
    t2.start()
    # t1.join()
    # t2.join()
    print("主线程：",time.ctime())
