#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-11 14:25:35
# @Author  : 孙阳 (you@example.org)
# @Link    : ${link}
# @Version : $Id$

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, Compose

class NewsLoader(ItemLoader):
    default_output_processor = TakeFirst()

class ChinaLoader(NewsLoader):
    text_out = Compose(Join(), lambda s: s.strip())  #
    source_out = Compose(Join(), lambda s: s.strip())

