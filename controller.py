# coding=utf-8

from api.sort import sort_ip_port, drop_port
from api.scan import open_url
import api.constant as constannt
import threading
from itertools import izip_longest

def get_ip():
    result_list = sort_ip_port()
    save_file = open(constannt.SORT_IP_RESULT_FILE_NAME, 'w')

    for result in result_list:
        save_file.write(result + '\n')
    save_file.close()

def scan():
    result1_list = []
    f = open(constannt.SORT_IP_RESULT_FILE_NAME, 'r')
    for ip in f.readlines():
        result1_list.append(str(ip).replace('\n', '').strip())
    print len(result1_list)
    chunk_list = lambda a_list, n: izip_longest(*[iter(a_list)] * n)
    result_groups = list(chunk_list(result1_list, len(result1_list)/30))

    for result in result_groups:
        t=threading.Thread(target=open_url, args=(result, 0))
        t.start()
    t.join()

def drop():
    drop_port()