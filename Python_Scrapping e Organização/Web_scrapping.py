#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 18:32:23 2022

@author: jotape42p
"""

import requests, time, re

url = "https://edhrec.com/combos"

colors = ['w', 'u', 'b', 'r', 'g', 'colorless', 'wu', 'ub', 'br', 'rg', 'gw', 'wb', 'ur', 'bg', 'rw', 'gu', 'wub', 'ubr', 'brg', 'rgw', 'gwu', 'wbg', 'urw', 'bgu', 'rwb', 'gur', 'wubr', 'ubrg', 'brgw', 'rgwu', 'gwub', 'wubrg']

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0',
}

listcombos = []
for cl in colors:
    print('\n', cl)
    response = requests.get('https://json.edhrec.com/combos/'+ cl + '.json', headers=headers)
    print(response)
    j = response.json()
    listcombos.append(j['container']["json_dict"]['cardlists'])
    print(len(j['container']["json_dict"]['cardlists']))
    time.sleep(2)

#%%

listcombos = [l2 for l in listcombos for l2 in l]
print(len(listcombos))

#%%

c = {}

for combo in listcombos:
    c['combo_'+combo['cardviews'][0]['url'].split("/")[-1]] = {}
    d = c['combo_'+combo['cardviews'][0]['url'].split("/")[-1]]
    for card in combo['cardviews']:
        d['name'] = card['name']
        d['type'] = card['primary_type']
        d['rarity'] = card['rarity']
    d['url'] = card['url']
    d['id'] = card['url'].split('/')[-1]
    if len(d['url'].split("/")[-1]) > 4:
        print(d['url'])
    d['number_of_decks'] = re.search("\(.*\)", combo['tag']).group()[1:-1]

#%%

import pandas as pd

df = pd.DataFrame(c).T
print(df['url'].str.split('/').str[-1].min())
    

#%%

import requests, time, re
from bs4 import BeautifulSoup

url = "https://commanderspellbook.com/combo"
c = {}
for i in range(1, 10217):
    print(i)
    c[str(i)] = {}
    response = requests.get(url+"/"+str(i))
    # print(response)
    # time.sleep(0.2)
    soup = BeautifulSoup(response.text, 'html.parser')
    if len(soup.find_all("div", {"id": "combo-metadata"})) > 0:
        for s in soup.find_all("div", {"id": "combo-metadata"}):
            c[str(i)]['n_of_decks'] = re.search("[0-9]+", s.find("span", {"class": "text"}).text).group()
            print(c[str(i)]['n_of_decks'])
    else:
        c[str(i)]['n_of_decks'] = 0
        print(c[str(i)]['n_of_decks'])
        
print("Scrapping finalizado")

import pandas as pd

df = pd.DataFrame(c).T
print(df)

df.to_csv('EDHREC Number of Decks.csv')

