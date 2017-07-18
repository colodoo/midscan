# coding=utf-8

import requests
import constant

# !!出了点问题,长度方面的,log方面的
def open_url(result_list, is_https):
    result_file = open(constant.SCAN_IP_PORT_RESULT_FILE_NAME, 'w')
    remaining = result_list.__len__()
    send_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding':'gzip, deflate',
        'Connection':'keep-alive',
        'Upgrade-Insecure-Requests':'1'
    }
    for result in result_list:
        tmp=str(result).strip().split(':')
        ip=tmp[0]
        port=tmp[1]
        result_str_list=[]
        try:
            if is_https == 1:
                url='https://' + result
            else:
                url='http://' + result
            response = requests.get(url, timeout=5, headers=send_headers, verify=False)
            # response = requests.get(url, timeout=3, headers=send_headers)

            # server信息获取
            server = ''
            _headers = response.headers
            if 'Server'.lower() in str(_headers):
                server = _headers['server']
            else:
                server = ''

            # headers = response.headers
            # content = response.content
            print '[+] ' + str(result)
            # 写入文件
            result_file.write(ip + '\t' + port + '\t' + url + '\t\t' + server + '\n')
        except Exception,e:
            pass
            print '[!] ' + str(result) + ':' + str(e)
            # if 'BadStatusLine' in str(e):
            #     result_file.write(ip + '\t' + port + '\t' + url + '\t' + 'BadStatusLine' +'\n')
        finally:
            remaining -= 1
            print str('remaining:' + str(remaining))