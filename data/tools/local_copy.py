from bs4 import BeautifulSoup
import json
import requests

def get_page(url):
    page = requests.get(url)
    return page.content

def create_page(name, page):
    with open('local_pages/'+name+'.html', 'wb') as f:
        f.write(page)

def get_url_list(raw_url):
    with open(raw_url, 'r') as f:
        data = json.load(f)
    return data

def get_local_page(file_name):
    with open(file_name, 'r') as f:
            page = f.read()
    return page

local_file = "icfghani-cbd.html"
page = get_page("https://www.leafly.com/indica/afghani-cbd")
raw_url = "../url_list.json"

url_list = get_url_list(raw_url)

for stain in url_list:
    url = url_list[stain]['url']
    name = url_list[stain]['name']
    page = get_page(url)
    create_page(name, page)

'''
    url_list = []

    for value in data:
        url_list.append(data[value]['url'])
'''