import sys
# import math
from math import pi
from langdetect import detect


print('Hello World')
# print(sys.argv[0])
print(sys.argv[1])
print(pi)
print(sys.argv[2])
print (detect("Ein, zwei, drei, vier"))

a= 4
b=3



# import requests
#
# url = 'https://ip.decodo.com/json'
# proxy_line='city.decodo.com:21001:user-sp8chmas0h-sessionduration-60:2Oyk1nkgnLDuy~6zQ7'
# hostname, port, username, password = proxy_line.split(':', 4)
# proxy = f"https://{username}:{password}@{hostname}:{port}"
#
# result = requests.get(url, proxies = {'http': proxy, 'https': proxy})
# rjson=result.json()['city']
#
# print(result.text)
# print(f'https://google.com/maps?q={rjson["latitude"]},{rjson["longitude"]}')
# print(proxy)