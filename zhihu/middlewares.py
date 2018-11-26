# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
import time
import pymysql
USER_AGENT_LIST = [
                    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
                    'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19',
                    'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
                    'Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                    'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',
                    'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0',
                    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36',
                    'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19',
                    'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'
                   ]

class IPProxydownloadermiddleware(object):
    def process_request(self,request,spider):
        ua = random.choice(USER_AGENT_LIST)
        if ua:
            request.headers['User-Agent'] = ua
        while True:
            proxy = getip()
            if proxy:
                request.meta["proxy"] = proxy
                break
            else:
                continue
    # def solve_ip(self):
    #         proxy = getip()
    #         if proxy:
    #             request.meta["proxy"] = proxy



def getip():
    try:
        conn = pymysql.connect(host='132.232.102.235', user='root', passwd='Root_12root', port=3306, db='nihao')
        sql = """select ip,stat from dyn where randid=9;"""
        cur = conn.cursor()
        cur.execute(sql)
        # conn.commit()
        ret = cur.fetchall()
        if ret:
            sta = ret[0][1]
            if sta:
                ip = ret[0][0] + ':808'
                print(ip)
                conn.close()
                # time.sleep(10)
                return ip
        else:
            print("请等待")
            return 0

    except Exception as e:
        print(e)
        return 0