# -*- coding: utf-8 -*-
import scrapy,re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapyuniversal.utils import get_config
from scrapyuniversal.rules import rules
from scrapyuniversal.items import NewsItem
from scrapyuniversal.ChinaLoader import ChinaLoader
from scrapyuniversal import urls
from bs4 import BeautifulSoup
from scrapy import FormRequest
import json
class UniversalSpider(CrawlSpider):
    name = 'universal'
    def __init__(self,name,keyword,*args,**kwargs):
        config = get_config(name)
        self.config = config
        self.rules = rules.get(config.get('rules'))
        self.name = name
        self.keyword = keyword
        #self.start_urls = ["http://106.38.57.66:8080/oasearch/front/search.do"]
        #if start_urls:
            #if start_urls.get("type") == 'static':
                #self.start_urls = start_urls.get("value")
            #elif start_urls.get("type") == 'dynamic':
                #self.start_urls = list(eval('urls.' + start_urls.get('method'))(*start_urls.get('args',[]),keyword))
        self.allowed_domains = config.get('allowed_domains')
        super(UniversalSpider,self).__init__(*args,**kwargs)
    def start_requests(self):
        urls = self.config.get("start_urls")
        url = urls['start_url']
        args = urls['args']
        requests = []
        for i in range(args[0],args[1]+1):
            formdata = {
                "pageNo": str(i),
                "query": self.keyword
           }
            #yield scrapy.Request(url=self.start_urls[0],method="POST",body={"pageNo":'1',"query":'it'},callback=self.parse_item,
            #headers={'Content-Type':'application/x-www-form-urlencoded'})
            result=FormRequest(url=url,method='POST',formdata=formdata,callback=self.parse_url)
            requests.append(result)
        return requests

    def parse_url(self,response):
        content = response.body
        soup = BeautifulSoup(content,'html5lib')
        #tag_a_list = soup.find_all('a',attrs={'target':'_blank'})
        tag_i_list = soup.find_all('i')
        url_list = []
        for tag_i in tag_i_list:
            #url = tag_a['href']
            str_tag_i = str(tag_i)
            t = re.findall(r'\.htm',str_tag_i)
            if t:
                url_list.append(tag_i.get_text())
        for url in url_list:
            yield scrapy.Request(url=url,callback=self.parse_item)

    def parse_item(self, response):
        #content = response.text
        #from scrapy.shell import inspect_response
        #inspect_response(response,self)
        item = self.config.get('item')
        if item:
            cls = eval(item.get('class'))()
            loader = eval(item.get('loader'))(cls,response=response)
            for key,value in item.get('attrs').items():
                for extractor in value:
                    if extractor.get('method') == 'xpath':
                        loader.add_xpath(key, *extractor.get('args'), **{'re': extractor.get('re')})
                    if extractor.get('method') == 'css':
                        loader.add_css(key, *extractor.get('args'), **{'re': extractor.get('re')})
                    if extractor.get('method') == 'value':
                        loader.add_value(key, *extractor.get('args'), **{'re': extractor.get('re')})
                    if extractor.get('method') == 'attr':
                        loader.add_value(key, getattr(response, *extractor.get('args')))
            yield loader.load_item()







       
