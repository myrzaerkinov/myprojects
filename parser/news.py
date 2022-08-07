import requests
from bs4 import BeautifulSoup

URL = 'https://www.securitylab.ru/news/'

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0"
}

def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('a', class_='article-card inline-card')
    news = []
    for i in items:
        news.append({
            'title': i.find("h2", class_='article-card-title').getText(),
            'desc': i.find("p").getText(),
            'link': f"https://www.securitylab.ru/{i.get('href')}",
            'time': i.find("time").getText()
        })
    return news


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        news = []
        for page in range(1, 4):
            html = get_html(f"{URL}page1_{page}.php")
            news.extend(get_data(html.text))
        return news
        # for i in get_data(html.text):
        #     print(i)
    else:
        raise Exception("ERROR in Parser")

print(parser())
