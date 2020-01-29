import feedparser, requests

#d = feedparser.parse('')
#for post in d.entries
    #print(post.title)

import xml

headers={'accept':'*/*',
         'user-agent': 'Chrome/79.0.3945.130'}
url='https://lenta.ru/rss/news.xml'

def rss_parse(url, headers):
    session = requests.Session()
    request=session.get(url, headers=headers)
    #time.sleep(3)

    if request.status_code==200:

        print('OK', request.status_code)
        page= feedparser.parse(url)
        return page
    else:
        pass


print(rss_parse(url, headers))




