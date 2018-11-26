coding = "utf-8"
import scrapy
import re
import io
import sys
import json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')#'gb18030'|
from scrapy_redis.spiders import RedisSpider

class LalaSpider(RedisSpider):
    name = 'lala'
    allowed_domains = ['zhihu.com','httpbin.org']
    # start_urls = ['https://www.zhihu.com/people/zhang-jia-wei/activities','http://httpbin.org/ip']
    redis_key = 'zh'
    # def start_requests(self):
    #
    #     # yield scrapy.Request(self.start_urls[1], callback=self.check_ip, dont_filter=True)
    #     yield scrapy.Request(self.start_urls[0],cookies = cookies,callback=self.parse)

    def parse(self, response):

        cookies = "_zap=554e65d0-a4bb-4b15-b9ea-ae392fb669ad; d_c0=AGCoRLW6ag6PThEZ7kamy-PooIwtaDPRA4w=|1540460652; q_c1=96d1efefc8bd496db21c38fb972b7815|1540460655000|1540460655000; _xsrf=4oRmyeKPQrCZhmRVbr94CdUs62Eh0Jbu; l_cap_id=ZDcyZjkxN2EyOTM4NDM1ZTk1MGFhODE5ZjM3MmUwMGM=|1540622756|f85307f0cfa632e29a7da5fde50f3bbb01e417bc; r_cap_id=OWY4NWYwMTYyOTJiNGQxZGI4NWM2OTFlNTE4Y2U2NWY=|1540622756|de1751cb3698cfba15afb00587a4c1f4fb76d84d; cap_id=Yzk2N2Q3NjliNzA2NDU4N2EzM2VlNDQ0YzI1MDcwOTg=|1540622756|90c21a5f2e25ef91ff2cae737bad3e33954ddf18; __gads=ID=77a7ff089bde8375:T=1540693845:S=ALNI_MZmQ5jTX3rUS1oo9P7EKaJimBq1Gw; _ga=GA1.2.1378665705.1540698352; tst=f; capsion_ticket=2|1:0|10:1541214610|14:capsion_ticket|44:ZWU3MmNiMmIxMGY4NGY3MWJiOTNhNDA4M2QxZmQ1YWM=|a66a2dcccba6c47c8ae560c4d944b5987ad3dfbd3c1994593d3c3fc299e2b445; z_c0=2|1:0|10:1541214818|4:z_c0|92:Mi4xdjB0bUNRQUFBQUFBWUtoRXRicHFEaVlBQUFCZ0FsVk5ZbURLWEFBRkdjOTN3VUFpX0VGVG5GS0FZbnNKSHZNUnV3|e319a4854eac54dd63e0ce7c18b31b40832d34e46fe26c9def1923c2feb32fc1; __utma=51854390.1378665705.1540698352.1541215002.1541215002.1; __utmz=51854390.1541215002.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/300941338/answer/523160601; __utmv=51854390.100--|2=registration_date=20180512=1^3=entry_date=20180512=1; tgw_l7_route=c919f0a0115842464094a26115457122"
        # cookies = "_zap=554e65d0-a4bb-4b15-b9ea-ae392fb669ad; d_c0=AGCoRLW6ag6PThEZ7kamy-PooIwtaDPRA4w=|1540460652; q_c1=96d1efefc8bd496db21c38fb972b7815|1540460655000|1540460655000; _xsrf=4oRmyeKPQrCZhmRVbr94CdUs62Eh0Jbu; l_cap_id=ZDcyZjkxN2EyOTM4NDM1ZTk1MGFhODE5ZjM3MmUwMGM=|1540622756|f85307f0cfa632e29a7da5fde50f3bbb01e417bc; r_cap_id=OWY4NWYwMTYyOTJiNGQxZGI4NWM2OTFlNTE4Y2U2NWY=|1540622756|de1751cb3698cfba15afb00587a4c1f4fb76d84d; cap_id=Yzk2N2Q3NjliNzA2NDU4N2EzM2VlNDQ0YzI1MDcwOTg=|1540622756|90c21a5f2e25ef91ff2cae737bad3e33954ddf18; __gads=ID=77a7ff089bde8375:T=1540693845:S=ALNI_MZmQ5jTX3rUS1oo9P7EKaJimBq1Gw; _ga=GA1.2.1378665705.1540698352; tst=f; capsion_ticket=2|1:0|10:1541214610|14:capsion_ticket|44:ZWU3MmNiMmIxMGY4NGY3MWJiOTNhNDA4M2QxZmQ1YWM=|a66a2dcccba6c47c8ae560c4d944b5987ad3dfbd3c1994593d3c3fc299e2b445; z_c0=2|1:0|10:1541214818|4:z_c0|92:Mi4xdjB0bUNRQUFBQUFBWUtoRXRicHFEaVlBQUFCZ0FsVk5ZbURLWEFBRkdjOTN3VUFpX0VGVG5GS0FZbnNKSHZNUnV3|e319a4854eac54dd63e0ce7c18b31b40832d34e46fe26c9def1923c2feb32fc1; __utma=51854390.1378665705.1540698352.1541215002.1541215002.1; __utmc=51854390; __utmz=51854390.1541215002.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/300941338/answer/523160601; __utmv=51854390.100--|2=registration_date=20180512=1^3=entry_date=20180512=1; tgw_l7_route=b3dca7eade474617fe4df56e6c4934a3"
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
        url = "https://www.zhihu.com/api/v4/members/zhang-jia-wei/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20"
        yield scrapy.Request(url,callback=self.parse_detail,cookies = cookies)
        # yield scrapy.Request(url_proxy_ip,callback=self.parse_ip,dont_filter=True)

    def parse_detail(self,response):
        # print(response.status)
        try:
            js_str = response.body.decode()
            dic1 = json.loads(js_str)
            # print(dic1["data"])
            name = response.url.split("https://www.zhihu.com/api/v4/members/")[1]
            name = name.split("/")[0]
            if dic1["data"] is not None:
                item = {}
                item["from"] = name
                if not dic1["paging"]["is_end"]:
                    item["totals"] = dic1["paging"]["totals"]
                    # item["next"] = dic1["paging"]["next"]
                    item["page"] = int(dic1["paging"]["next"].split("=")[3])/20
                    item["next"] = "https://www.zhihu.com/"+"api/v4/"+dic1["paging"]["next"].split("https://www.zhihu.com/")[1]
                    # print(item["next"])
                    for i in dic1["data"]:
                        item["name"] = i["name"]
                        item["gender"] = i["gender"]
                        item["url_token"] = i["url_token"]
                        item["is_followed"] = i["is_followed"]
                        item["answer_count"] = i["answer_count"]
                        item["follower_count"] = i["follower_count"]
                        item["id"] = i["id"]
                        item["gender"] = i["gender"]
                        item["avatar_url"] = i["avatar_url"]
                        item["url"] = i["url"]
                        item["is_org"] = i["is_org"]
                        item["headline"] = i["headline"]
                        item["is_followed"] = i["is_followed"]
                        yield item
                        # yield scrapy.Request(self.start_urls[1], callback=self.check_ip, dont_filter=True)
                        yield scrapy.Request("https://www.zhihu.com/api/v4/members/"+item["url_token"]+"/followers?include=data%5B%2A%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=20&offset=0",callback=self.parse_detail)
                    yield scrapy.Request(item["next"],callback=self.parse_detail)
        except Exception as e:
            pass

    def check_ip(self,response):
        print(response.body.decode()*5)

#