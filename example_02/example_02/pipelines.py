# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#TODO 把python2.7.xxx升级为python3.xxx版本

from scrapy.pipelines.files import FilesPipeline
from urllib.parse import urlparse
from os.path import  basename,dirname,join

class Example02Pipeline(object):
    def process_item(self, item, spider):
        return item


class MyFilesPipeline(FilesPipeline):
    
    def file_path(self,request,response=None,info=None):
        path = urlparse(request.url).path
        return join(basename(dirname(path)),basename(path))
