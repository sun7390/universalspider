#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-11 14:48:46
# @Author  : 孙阳 (you@example.org)
# @Link    : ${link}
# @Version : $Id$

import sys
import random
from scrapy.utils.project import get_project_settings
from scrapyuniversal.spiders.universal import UniversalSpider
from scrapyuniversal.utils import get_config
from scrapy.crawler import CrawlerProcess
def run():
    name = sys.argv[1]
    keyword = sys.argv[2]
    custom_settings = get_config(name)
    # 爬取使用的Spider名称
    spider = custom_settings.get('spider', 'universal')
    project_settings = get_project_settings()
    settings = dict(project_settings.copy())
    # 合并配置
    settings.update(random.choice(custom_settings.get('settings')))
    process = CrawlerProcess(settings)
    # 启动爬虫
    process.crawl(spider, **{'name': name,'keyword':keyword})
    process.start()

if __name__ == '__main__':
    run()
