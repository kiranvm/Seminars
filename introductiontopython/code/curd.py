#!/usr/bin/env python
import BeautifulSoup

with open ("cs2.html","r") as inf:
	doc = inf.read()
	print doc
	

soup = BeautifulSoup.BeautifulSoup(doc)
for i in range (10,45):
	print soup('td')[i].string

