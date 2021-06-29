#!/usr/bin/python3.9
# -*- coding=utf8 -*- 
# Creater:zhangteng


import re

str1 = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

re_match = re.match(
    '([A-Z]{3})\s+[a-z]{6}\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d{1,5})\s+\w{11}\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d{1,5}),\s+\w{4}\s+([0-2]:[0-2][0-3]:[0-5][0-9]),\s+\w{5}\s+(\d{8}),\s+\w{5}\s+([A-Z]{3})',
    str1).groups()
print(f'{"protcol":15}:' + re_match[0])
print(f'{"server":15}:' + re_match[1])
print(f'{"localserver":15}:' + re_match[2])
print(f'{"idle":15}:' + re_match[3])
print(f'{"bytes":15}:' + re_match[4])
print(f'{"flags":15}:' + re_match[5])
