from multiprocessing import Process     #需要提前安装模块
from os import getpid
from random import randint
from time import time, sleep
# python 多进程编程

def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())      #pid 进程识别号 进程标识符
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    p1 = Process(target=download_task, args=('Python从入门到住院.pdf', ))
    p1.start()
    p2 = Process(target=download_task, args=('Peking Hot.avi', ))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()