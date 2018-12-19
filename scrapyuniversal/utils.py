#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-11 14:44:59
# @Author  : 孙阳 (you@example.org)
# @Link    : ${link}
# @Version : $Id$

from os.path import realpath,dirname
import json
def get_config(name):
	path = dirname(realpath(__file__)) + '/configs/' + name + '.json'
	with open(path,'r',encoding = 'utf-8') as f:
		return json.loads(f.read())