import time
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
import requests


def get_html(url):
    return requests.get(url).status_code
    # a = 0
    # for i in range(1000):
    #     a += i

urls = [
	'http://www.python.org',
	'http://www.python.org/about/',
	'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
	'http://www.python.org/doc/',
	'http://www.python.org/download/',
	'http://www.python.org/getit/',
	'http://www.python.org/community/',
	'https://wiki.python.org/moin/',
	'http://planet.python.org/',
	'https://wiki.python.org/moin/LocalUserGroups',
	'http://www.python.org/psf/',
	'http://docs.python.org/devguide/',
	'http://www.python.org/community/awards/'
	] * 50


if __name__ == '__main__':
    print('Number of links:', len(urls))

    pool = Pool(4)
    threadPool = ThreadPool(4)
    current = time.time()
    pool.map(get_html, urls)
    print('time: ', time.time() - current)

    current = time.time()
    threadPool.map(get_html, urls)
    print('time: ', time.time() - current)



