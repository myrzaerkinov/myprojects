import requests
from bs4 import BeautifulSoup as Beauty

URL = 'https://hd-rezka.biz/filmy'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = Beauty(html, "html.parser")
    items = soup.find_all("div", class_='b-content__inline_item short-story')
    films = []
    for i in items:
        films.append({
            'title': i.find("div", class_='b-content__inline_item-link').find("a").getText(),
            'image': 'https://hd-rezka.biz' + i.find("div", class_='b-content__inline_item-cover').find("img").get("data-src")
        })
    return films

def parser():
    html = get_html(URL)
    if html.status_code == 200:
        films = []
        for page in range(1, 3):
            html = get_html(f"{URL}/page/{page}")
            films.extend(get_data(html.text))
        return films
        # for i in get_data(html.text):
        #     print(i)
    else:
        raise Exception('Parser error')

print(parser())

