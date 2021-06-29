#!/usr/bin/python3.9
# -*- coding=utf8 -*- 
# Creater:zhangteng


import re

vlan = 'VLAN ID'
mac = 'MAC'
type = 'Type'
interface = 'Interface'
str1 = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'
re1 = re.match('(\d{1,4})\s+([0-9a-fA-F]{4}(\.[0-9a-fA-F]{4}){2})\s+([A-Z]{7})\s+(\w+.*\d)', str1).groups()


print(f'{vlan:15}' + ':' + re1[0])
print(f'{mac:15}' + ':' + re1[1])
print(f'{type:15}' + ':' + re1[3])
print(f'{interface:15}' + ':' + re1[4])
