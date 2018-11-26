# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random

class IPProxydownloadermiddleware(object):
    PROXIES = [
# "39.104.15.226:8080",
# "14.23.114.92:81",
# "116.62.9.96:80",
# "222.92.244.40:80",
# "139.196.110.205:80",
# "139.129.165.171:80",
# "123.56.237.214:80",
# "223.203.0.14:8000",
# "123.103.93.38:80",
# "120.76.40.254:80",
# "117.131.75.134:80",
# "14.23.114.92:81"
# "112.74.187.216:80"

# "223.203.0.14:8000",
# "123.103.93.38:80"
"101.132.98.70:808",
"223.203.0.14:8000",
"112.74.41.42:80",
"120.77.170.112:80",
"123.103.93.38:80",
"121.40.36.239:80",
"120.76.40.254:80",
"139.196.110.205:80",
"120.77.205.21:80",
        "80.26.152.146:60133",
"103.57.227.74:53281",
"47.94.221.41:8118",
"94.43.142.221:53281",
"103.98.78.9:58161",
"177.53.8.166:51499",
"183.129.207.82:12085",
"118.97.95.196:8080",
"116.212.152.226:50029",
"89.207.111.62:41258",
"159.224.193.190:53176",
"190.152.6.106:49471",
"41.138.208.193:56148",
"41.217.221.190:8888",
"108.170.48.173:808",
"185.178.83.111:52663",
"41.242.57.38:31368",
"105.235.205.38:42053",
"65.78.155.119:80",
"200.35.106.180:8080",
"92.245.4.223:38066",
"103.1.93.135:60804",
"202.72.219.42:61300",
"197.149.125.50:45224",
"170.79.88.66:53281",
"183.252.16.100:63000",
"200.35.56.113:44477",
"166.143.199.252:49710",
"87.255.75.224:57567",
"128.68.42.150:8888",
"104.199.190.42:80",
"191.36.141.33:43310",
"140.190.54.187:53277",
"83.242.255.41:8080",

"197.211.39.7:56680",
"103.92.117.18:33611",
"166.159.115.50:39059",
"177.105.231.190:53192",
"195.14.114.24:56897",
"105.233.35.90:51988",
"83.97.108.8:41258",
"190.147.43.62:21776",
"77.109.59.196:38860",
"190.214.16.230:53281",
"64.192.234.39:53281",
"47.52.141.35:80",
"103.15.140.241:50168",
"178.150.166.71:58153",
"195.9.91.66:33199",
"103.215.210.221:39780",
"95.78.177.63:46184",
"202.138.242.69:38189",
"109.167.207.52:61331",
"86.57.254.100:47717",
"60.6.241.72:808",
"179.106.88.162:80",
"202.183.32.181:80",
"103.254.94.245:37420",
"95.140.20.94:33994",
"101.255.44.204:55399",
"203.95.221.222:59838",
"95.107.6.252:44508",
"152.74.58.247:8888",
"202.74.239.21:37639",
"155.186.173.52:53281",
"141.101.236.49:8888",
"101.132.98.70:808",

"104.228.234.78:30591",
"111.68.45.227:8080",
"41.78.243.198:53281",
"31.31.162.92:52298",
"116.212.135.134:40992",
"217.8.227.22:8888",
"170.81.141.34:53281",
"138.185.9.45:44717",
"96.87.188.193:61748",
"36.37.160.108:55583",
"103.99.251.61:39703",
"80.51.100.10:44878",
"46.151.60.99:45605",
"217.12.212.150:219",
"93.63.147.2:8888",
"187.45.106.176:8080",
"1.10.188.102:45806",
"119.235.19.42:38546",
"109.196.82.214:46950"


]
    def process_request(self,request,spider):
        proxy = random.choice(self.PROXIES)
        request.meta["proxy"] = proxy
        print(proxy*20)