#!/usr/bin/env python3.5
# -*- coding:utf8 -*-

import requests
from bs4 import BeautifulSoup

init_url='http://www.data5u.com/'

headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"}

init_html=requests.get(init_url,headers=headers)
init_soup=BeautifulSoup(init_html.text,'lxml')

result = init_soup.find_all('ul',class_='l2')

for ipSrc in result:
    ipSrc_r=ipSrc.find('span').find('li').extract()
    print(ipSrc_r)
