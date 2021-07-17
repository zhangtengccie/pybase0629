import re

str1 = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'
str2 = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

re_result_str1 = re.match(r'(\d{1,4})\s+([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})\s+(\w+)\s+(\w\S+\d)',
                          str1.strip()).groups()
'''
vlan  \d{1,4}
mac   [0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}
interface   \w\S+\d
'''
print(re_result_str1)

re_result_str2 = re.match(
    r'(\w+)\s+\w+\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d{1,5})\s+localserver\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d{1,5}),\s+idle\s+(\d{1,2}):(\d{1,2}):(\d{1,2}),\s+bytes\s+(\d+),\s+flags\s+(\w+)',
    str2.strip()).groups()
print(re_result_str2)
