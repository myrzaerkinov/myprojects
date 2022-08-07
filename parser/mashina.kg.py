import requests
from bs4 import BeautifulSoup as Beauty

URL = 'https://www.mashina.kg/search/all/'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request

def get_data(html):
    soup = Beauty(html, "html.parser")
    items = soup.find_all("div", class_='list-item list-label')
    cars = []
    for i in items:
        cars.append({
            'title': i.find("div", class_='block title').get("h2").getText(),
            'price': i.find("div", class_='block price').get("p").getText(),
            'description': i.find("div", class_='block info-wrapper item-info-wrapper').get("p").getText()
        })
    return cars

def get_parser():
    html = get_html(URL)
    if html.status_code == 200:
        # cars = []
        for i in get_data(html.text):
            print(i)
    else:
        raise Exception('error')

get_parser()