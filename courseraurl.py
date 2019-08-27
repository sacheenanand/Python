__author__ = 'sanand'

import urllib.request, urlib.parses, urlib.error
from bs4 import BeautifulSoup


url = input("enter the url ")

html = urlib.request.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

# Retreive all of the anchor tags

tags - soup('a')
for tag in tags:
    print(tag.get('href', None))

