#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/19 10:42
# @Author  : CoLoDoo
# @Site    : 
# @File    : get_title.py
# @Software: PyCharm

import requests
from selenium import webdriver
from bs4 import BeautifulSoup as bs

url = 'http://127.0.0.1/index.php?a=1'
driver = webdriver.PhantomJS()
driver.get(url)
content = driver.page_source

print content
content=bs(content, 'lxml')
# print content.find('title').string