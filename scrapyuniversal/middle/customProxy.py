#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-12 15:44:26
# @Author  : 孙阳 (you@example.org)
# @Link    : ${link}
# @Version : $Id$

from scrapyuniversal.middle.resource import PROXIES
import random
class RandomProxy(object):
	def process_request(self,request,spider):
		proxy = random.choice(PROXIES)
		request.meta['proxy'] = 'http://%s'% proxy

