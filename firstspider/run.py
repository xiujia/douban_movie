# -*- coding: utf-8 -*-
"""
@Date : 2017/8/25
@Author : cg
@Function : pycharm shell debug

"""
from scrapy import cmdline

name = 'douban_movie_top250'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
