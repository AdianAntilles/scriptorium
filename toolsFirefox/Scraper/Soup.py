#!/bin/env python3

from bs4 import BeautifulSoup
import requests

with open('websitelist','r') as sitelist:
    horizon = sitelist.readlines()

for entry in horizon:
    try:
        record = requests.get(entry.rstrip())
    except:
        record = entry
    soup = BeautifulSoup(record, 'html.parser')
    print('BS ', soup, ' was loaded.')
    for link in soup.find_all('a'):
        if 'href' in link:
            print('link found: ', link)








