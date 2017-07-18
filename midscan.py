#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/10 10:23
# @Author  : CoLoDoo
# @Site    : 
# @File    : scan1web.py
# @Software: PyCharm

import controller
import sys
from optparse import OptionParser
import api.constant as constant

def init_opt():
    usage = "midsca.py [ -f|--file <filename>] [-s|--scan] <scanresult>]"
    optParser = OptionParser(usage)
    optParser.add_option("-f","--file",action = "store",type="string",dest = "sort ip nmap file name")
    optParser.add_option("-s","--s",action = "store",type="string",dest = "scan result save file name")
    return optParser

# 主要对参数的处理
def main():
    optParser = init_opt()
    if len(sys.argv) >= 2:
        if sys.argv[1] == '-f' or sys.argv[1] == '--file':
            if len(sys.argv) == 3:
                constant.NMAP_SCAN_RESULT_FILE_NAME = sys.argv[2]
            controller.get_ip()
        if sys.argv[1] == '-s' or sys.argv[1] == '--scan':
            if len(sys.argv) == 3:
                constant.SCAN_IP_PORT_RESULT_FILE_NAME = sys.argv[2]
            controller.scan()
        if sys.argv[1] == '-h' or sys.argv[1] == '--help':
            optParser.print_help()
        else:
            optParser.print_usage()

if __name__ == '__main__':
    main()