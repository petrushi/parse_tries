import requests
from bs4 import BeautifulSoup


URL = 'https://www.google.ru/search?q=буква+с&tbm=isch'
HEADERS = None # enter user-agent and accept from network information


def get_html(url, params=None):
    r = requests.get(URL, headers=HEADERS, params=params)
    return r



def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='isv-r')
    tokens = []
    for item in items:
        next_items = item.find_all('a', class_='islib')
        for next_item in next_items:
            more_items = next_item.find_all('div', class_='islir')
            for more_item in more_items:
                tokens.append({
                    'last_items': more_item.find_all('img', class_='rg_i')
                })
    return tokens


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        print(get_content(html.text))
    else:
        print('Error')


parse()
