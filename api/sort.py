# coding=utf-8

import bs4
import constant

# !!处理的结果
def sort_ip_port():
    '''
    返回ip端口对应列表
    :return: result_list
    '''
    result_list = []
    # 这里采用参数的方式更为妥当
    result_file = open(constant.NMAP_SCAN_RESULT_FILE_NAME, 'r')
    result_source = result_file.read()
    bs_source = bs4.BeautifulSoup(result_source,'lxml')
    hosts = bs_source.find_all('host')
    for host in hosts:
        ports = host.ports.find_all('port')
        for port in ports:
            ip = host.address['addr']
            portid = port['portid']
            retult = ip + ':' + portid
            print ip + ':' + portid
            result_list.append(retult)
    result_file.close()

    return result_list

# 判断是否为相应的port，如果为是，则抛掉
def drop_port():
    ip_file=open(constant.SORT_IP_RESULT_FILE_NAME, 'r')
    drop_port_file=open(constant.DROP_PORTS_LIST, 'w')
    lenght = 0
    for ip in ip_file.readlines():
        ll=[]
        port=ip.strip().replace('\n', '').split(':')[1].strip().replace('\n', '')
        if '21' != port and '22' != port and '23' != port and '111' != port and '161' != port \
                and '1919' != port:
            print ip.strip().replace('\n', '')
            drop_port_file.write(ip.strip()+'\n')
            lenght=lenght+1
    print '\t[+] lenght:{0}'.format(str(lenght))
    ip_file.close()