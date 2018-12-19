#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-11 14:43:27
# @Author  : 孙阳 (you@example.org)
# @Link    : ${link}
# @Version : $Id$

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

rules = {
    'china': (
        Rule(LinkExtractor(allow=r'article\/.*\.html', restrict_xpaths='//div[@id="left_side"]//div[@class="con_item"]'),
             callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths='//div[@id="pageStyle"]//a[contains(., "下一页")]'))
    ),
    'jxw': (
    	Rule(LinkExtractor(allow=r'http:\/\/.*\.htm',restrict_xpaths='//div[@class="inform_search_text"]//dl[@class="result_text"]'),
    		callback='parse_item'),
    	Rule(LinkExtractor())
    )
}
