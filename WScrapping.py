#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 23:20:47 2022

@author: jotape42p
"""

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
