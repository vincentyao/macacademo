#!/usr/bin/env python3.5
# -*- coding:utf8 -*-

import requests
from bs4 import BeautifulSoup
import os

headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"}
start_url='http://www.mzitu.com/all'
start_html=requests.get(start_url,headers)

soup=BeautifulSoup(start_html.text,'lxml')
li_list=soup.find('div',class_='all').find_all('a')

for li in li_list:
    title = li.get_text()
    href=li['href']

    html=requests.get(href,headers=headers)
    html_soup=BeautifulSoup(html.text,'lxml')
    max_span=html_soup.find_all('span')[10].get_text()

    for page in range(1,int(max_span)+1):
        page_url=href+'/'+str(max_span)
        img_html=requests.get(page_url,headers=headers)
        img_soup=BeautifulSoup(img_html.text,'lxml')
        img_url=img_soup.find('div',class_='main-image').find('img')['src']
        print(img_url)
