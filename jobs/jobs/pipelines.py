# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# import json
# from scrapy.exporters import JsonItemExporter
import pymysql
from scrapy.exceptions import DropItem

class JobsPipeline(object):

    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                                    user='root',
                                    passwd='123456',
                                    db='51jobs',
                                    charset='utf8', 
                                    use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            insert_sql = """
            insert into jobs_data(jobid,job_href,job_name,company_href,company_name,providesalary,\
            workarea,company_type,jobwelf,experience,education,number,companysize,companyind)\
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            self.cursor.execute(insert_sql,(item['jobid'],item['job_href'],item['job_name'],
                item['company_href'],item['company_name'],item['providesalary'],item['workarea'],
                item['company_type'],item['jobwelf'],item['experience'],item['education'],
                item['number'],item['companysize'],item['companyind']))
            
            self.conn.commit()
        except:
            raise DropItem("Insert Error in %s" % item)

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

