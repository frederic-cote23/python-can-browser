from bs4 import BeautifulSoup
import json
import requests
import glob, os

def get_remote_page(url):
    page = requests.get(url)
    return page.content

def get_local_page(file_name):
    with open(file_name, 'r') as f:
            page = f.read()
    return page

'''
EFFECT
<div class="m-histogram-item-wrapper">
    <div class="m-attr-label copy--sm">Sleepy</div>
        <div class="strain__histogram l-container" m-animate="" m-animate-default="strain__histogram--default" m-animate-play="strain__histogram--animate">
        <div class="m-histogram-item">
            <div class="m-attr-bar" style="width:87.5763747454175%"></div>
        </div>
    </div>
</div>
'''

def extract_info (page):
    soup = BeautifulSoup(page, 'html.parser')

    raw_info = soup.find_all(class_="m-histogram-item-wrapper")

    strain_title = soup.title.text.replace(' Cannabis Strain Information - Leafly', '')

    clean_info = {"Name": strain_title, "Effects": {}}

    for effect in raw_info:
        try:
            effect_name = effect.find(class_="m-attr-label copy--sm").text
            effect_score = effect.find(class_="m-attr-bar")["style"].replace('width:', '').replace('%', '')
            clean_info['Effects'][effect_name] = effect_score
        except:
            None

    return clean_info

def create_url_list(info_file,leafly_info):
    with open(info_file, 'w') as f:
        f.write(json.dumps(info_file))

#url = 'https://www.leafly.com/indica/afghani-cbd'


info_file = 'extract/info.json'
local_file_rep = 'data/tools/local_pages'



'''
os.chdir(local_file_rep)
for file in glob.glob("*.html"):
    print(file)
'''

os.chdir(local_file_rep)
for file in glob.glob("*.html"):
    file_name = file
    page = get_local_page(file_name)
    extract_info = extract_info(page)
    curated_info = {"Name": extract_info['Name'],"Effects": extract_info['Effects']}
    break


print(curated_info)