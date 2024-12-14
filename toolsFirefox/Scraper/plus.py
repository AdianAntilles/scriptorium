#!/bin/env python3

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'AliceStory')

print(soup.prettify())
