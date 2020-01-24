import time
from multiprocessing import Pool as ProcessPool
from multiprocessing.dummy import Pool as ThreadPool
import requests


def get_html(url):
    # begin = time.time()
    r = requests.get(url)
    # print(time.time() - begin)
    # print(r.content)

urls = [
    'http://google.com',
    'http://yandex.ru',
    'http://mail.ru'
] * 10

if __name__ == '__main__':
    processPool = ProcessPool(4)
    begin = time.time()
    # processPool.map(get_html, urls)
    print(time.time() - begin)
    # 4.945696830749512, 3.8851890563964844 4.080380439758301
    
threadPool = ThreadPool(4)
begin = time.time()
threadPool.map(get_html, urls)
# 1.6660172939300537  1.7026770114898682 1.6796414852142334
print(time.time() - begin)







