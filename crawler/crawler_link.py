import requests
import time
from lxml.html import fromstring


class crawl_link_web:

	def __init__(self, dom, cate, link):

		self.dom = dom
		self.cate = cate
		self.link = link

	def getcate(self):
		print("2__")

		req = requests.get(self.dom)
		tree = fromstring(req.text)
		cate = tree.xpath(self.cate)
		ct = []

		for c in list(dict.fromkeys(cate)):

			if "https://" in c:
				l = self.getlink(c)
				ct.append(l)
			elif c.startswith("/"): 
				l = self.getlink(self.dom + c[1:])
				ct.append(l)

		return ct 


	def getlink(self,c):

		req = requests.get(c)
		tree = fromstring(req.text)
		link = tree.xpath(self.link)
		li = []

		for i in list(dict.fromkeys(link)): 

			if "https://" in i: 
				if i.count(".") == 2:
					li.append(i)

			if c.startswith("/"): 
				if i.count(".") == 2:
					li.append(self.dom + i[1:])
					
		return li

