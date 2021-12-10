# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobsItem(scrapy.Item):

    # 唯一id
    jobid = scrapy.Field()
    # 招聘链接
    job_href = scrapy.Field()
    # 招聘名称
    job_name = scrapy.Field()
    # 公司链接
    company_href = scrapy.Field()
    # 公司名称
    company_name = scrapy.Field()
    # 薪资
    providesalary = scrapy.Field()
    # 工作地点
    workarea = scrapy.Field()
    # 公司类型
    company_type = scrapy.Field()
    # 工作福利
    jobwelf = scrapy.Field()
    # 经验要求
    experience = scrapy.Field()
    # 学历要求
    education = scrapy.Field()
    # 招聘人数
    number = scrapy.Field()
    # 公司规模
    companysize = scrapy.Field()
    # 公司标签
    companyind = scrapy.Field()