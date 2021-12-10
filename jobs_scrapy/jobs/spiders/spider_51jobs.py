import re
import ast
import scrapy
from bs4 import BeautifulSoup
from jobs.items import JobsItem
from jobs.jobs_list import get_jobs_list

class Spider51jobsSpider(scrapy.Spider):
    name = 'spider_51jobs'
    allowed_domains = ['51job.com']
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    
    def start_requests(self):
        job_list = get_jobs_list()
        for i in job_list[4:6]:
            for j in range(1, 2):
                url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,{key},2,{page}.html/'.format(key=i, page=j)
                yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        
        jobid_list = re.findall('"jobid":"(.*?)"', response.text)
        job_href_list = re.findall('"job_href":"(.*?)"', response.text)
        job_name_list = re.findall('"job_name":"(.*?)"', response.text)

        company_href_list = re.findall('"company_href":"(.*?)"', response.text)
        company_name_list = re.findall('"company_name":"(.*?)"', response.text)
        providesalary_list = re.findall('"providesalary_text":"(.*?)"', response.text)
        workarea_list = re.findall('"workarea_text":"(.*?)"', response.text)
        company_type_list = re.findall('"companytype_text":"(.*?)"', response.text)
        jobwelf_list = re.findall('"jobwelf":"(.*?)"', response.text)

        attribute_list = re.findall('"attribute_text":(\\[.*?\\])', response.text)

        experience_list = re.findall('"companytype_text":"(.*?)"', response.text)
        education_list = re.findall('"companytype_text":"(.*?)"', response.text)
        number_list = re.findall('"companytype_text":"(.*?)"', response.text)

        companysize_list = re.findall('"companysize_text":"(.*?)"', response.text)
        companyind_list = re.findall('"companyind_text":"(.*?)"', response.text)

        for i in range(len(jobid_list)):
            item = JobsItem()

            item['jobid'] = jobid_list[i].replace("\\","")
            item['job_href'] = job_href_list[i].replace("\\","")
            item['job_name'] = job_name_list[i].replace("\\","")
            item['company_href'] = company_href_list[i].replace("\\","")
            item['company_name'] = company_name_list[i].replace("\\","")
            item['providesalary'] = providesalary_list[i].replace("\\","")
            item['workarea'] = workarea_list[i].replace("\\","")
            item['company_type'] = company_type_list[i].replace("\\","")
            item['jobwelf'] = jobwelf_list[i].replace("\\","")

            attributes = ast.literal_eval(attribute_list[i])
            try:
                item['experience'] = attributes[1].replace("\\","")
                item['education'] = attributes[2].replace("\\","")
                item['number'] = attributes[3].replace("\\","")
            except:
                continue

            item['companysize'] = companysize_list[i].replace("\\","")
            item['companyind'] = companyind_list[i].replace("\\","")

            yield item