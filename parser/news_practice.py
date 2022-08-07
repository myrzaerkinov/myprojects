import requests
from bs4 import BeautifulSoup as Beauty

URL = 'https://www.securitylab.ru/news/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request

def get_data(html):
    soup = Beauty(html, "html.parser")
    items = soup.find_all("a", class_='article-card inline-card')
    news = []
    for i in items:
        news.append({
            'title': i.find("h2", class_='article-card-title').getText(),
            'desc': i.find("p").getText(),
            'link': f"https://www.securitylab.ru{i.get('href')}",
            'time': i.find("time").getText()
        })
    return news

def parser():
    html = get_html(URL)
    if html.status_code == 200:
        news = []
        for page in range(1, 3):
            html = get_html(f"{URL}page1_{page}.php")
            news.extend(get_data(html.text))
        return news
    else:
        raise Exception('PARSER ERROR')

print(parser())
