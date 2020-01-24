import time
from multiprocessing import Pool as ProcessPool
from multiprocessing.dummy import Pool as ThreadPool
import requests


def get_html(url):
    requests.get(url)

urls = [
    'http://google.com',
    'http://yandex.ru',
    'http://mail.ru'
] * 100


def calc_something(data):
    a = 0
    for i in range(10000):
        a += i


if __name__ == '__main__':
    processPool = ProcessPool(4)
    begin = time.time()
    processPool.map(get_html, urls)
    # 4.945696830749512, 3.8851890563964844 4.080380439758301
    # processPool.map(calc_something, urls)
    # 2.231503963470459 2.155320644378662 2.1670475006103516
    print(time.time() - begin)
    threadPool = ThreadPool(4)
    begin = time.time()
    threadPool.map(get_html, urls)
    # 1.6660172939300537  1.7026770114898682 1.6796414852142334
    # threadPool.map(calc_something, urls)
    # 0.04798388481140137 0.0467376708984375 0.045984506607055664
    print(time.time() - begin)







