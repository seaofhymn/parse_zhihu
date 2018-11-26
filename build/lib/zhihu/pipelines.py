# -*- coding: utf-8 -*-
from pymysql import *
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ZhihuPipeline(object):
    def process_item(self, item, spider):

        con = connect(host ="localhost",port=3306, user='root', password='123', database='zhihu', charset='utf8')
        cur = con.cursor()


        sql = """insert into zhihuuser (name,totals,page,next,gender,url_token,is_followed,answer_count,follow_count,url,is_org,headline,avatar_url,idd,idfrom) values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s");""" %(item["name"],item["totals"],item["page"],item["next"],item["gender"],item["url_token"],item["is_followed"],item["answer_count"],item["follower_count"],item["url"],item["is_org"],item["headline"],item["avatar_url"],item["id"],item["from"])

            # sql = """insert into yunyinyue (na,likes,href) values("%s","%s","%s");""" %(item["name"],item["likes"],item["href"])
        cur.execute(sql)
        con.commit()
            # print(item)


        print(item)
        cur.close()
        con.close()
        return item


