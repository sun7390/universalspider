#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-11 16:00:45
# @Author  : 孙阳 (you@example.org)
# @Link    : ${link}
# @Version : $Id$
import scrapy

def china(start,end):
	for page in range(start,end + 1):
		yield 'http://ech.china.com/articles/index_' + str(page) +'.html'
		
def jxw(start,end,keyword):
	for page in range(start,end+1):
		url = 'http://106.38.57.66:8080/oasearch/front/search.do'
		post_data = {
			'pageNo': str(page),
			'query': keyword
		}
		request = scrapy.FormRequest(url=url,formdata=post_data)
		yield request