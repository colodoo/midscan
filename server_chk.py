#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/4/27 10:56
# @Author  : CoLoDoo
# @Site    : 
# @File    : server_chk.py
# @Software: PyCharm

import requests

# 检查server，依照server加相应的后缀试控制台
def server_chk():
    file=open('ip_server.txt', 'r')
    # [!]目前只有tongweb
    server=['/twns', '/console/rest']
    try:
        send_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        for ip in file.readlines():
            ip=ip.replace('\n', '')
            for s in server:
                url=ip+s
                # if 'https' in url:
                #     response = requests.get(url, timeout=0.5, verify=False)
                # else:
                #     response = requests.get(url, timeout=0.5)
                response = requests.get(url, timeout=1, headers=send_headers)
                print '[+] {0}\t{1}'.format(url, str(response.status_code))
    except Exception,e:
        print '[!] {0}'.format(str(e))
    file.close()

server_chk()