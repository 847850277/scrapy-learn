# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy import Request


class ImagesspiderSpider(scrapy.Spider):
    name = 'ImagesSpider'
    start_urls = ['https://image.so.com/']
    BASE_URL = 'https://image.so.com/zj?ch=beauty&sn=%s&listtype=new&temp=1'
    print(BASE_URL % 0)
    start_index = 0

    #限制最大下载量，防止磁盘用量过大
    MAX_DOWNLOAD_NUM = 5000
    start_urls = [
        BASE_URL % 0
    ]

    def parse(self, response):

        infos = json.loads(response.body.decode('utf-8'))
        #print("infos:")
        #print(infos)
        yield {
            'image_urls':[info['qhimg_url'] for info in  infos['list']]
        }
        #如果count数大于0，并且下载数量不足MAX_DOWNLOAD_NUM 继续获取下一页
        self.start_index += infos['count']
        if infos['count'] >0 and self.start_index < self.MAX_DOWNLOAD_NUM:
            yield Request(self.BASE_URL % self.start_index)
