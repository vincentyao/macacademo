#!/usr/bin/env python3.5
#-*- coding:utf8 -*-

import requests
url = 'http://www.baidu.com'
r = requests.get(url)
print (r.text)
