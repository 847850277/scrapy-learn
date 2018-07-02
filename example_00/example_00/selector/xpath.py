# -*- coding: utf-8 -*-
'''
xpath的方法
'''

from scrapy.selector import Selector
from scrapy.http import HtmlResponse
body = '''
        <html>
            <head>
                <base href="http://example.com">
                <title>Example website</title>
            </head>
            <body>
                <div id ="images">
                    <a href="image1.html">Name:Image1 <br/><img src="image1.jpg"></a>
                    <a href="image2.html">Name:Image2 <br/><img src="image2.jpg"></a>
                    <a href="image3.html">Name:Image3 <br/><img src="image3.jpg"></a>
                    <a href="image4.html">Name:Image4 <br/><img src="image4.jpg"></a>
                    <a href="image5.html">Name:Image5 <br/><img src="image5.jpg"></a>
                </div>
            </body>

        </html>
       '''
response = HtmlResponse(url='http://www.example.com',body=body)
#print(response) 
#从根开始
selector = response.xpath('/html')  
#print(selector)
#head
selector = response.xpath('/html/head') 
#print(selector)
#选中某个节点的下a的元素
#选中div下面的所有a
selector = response.xpath('/html/body/div/a')
#print(selector)
#所有节点的a
selector = response.xpath('//a')
#print(selector)
#某个节点后的所有元素
#img后面的所有元素
selector = response.xpath('/html/body//img')
#print(selector)
#文本节点
selector = response.xpath('//a/text()')
#print(selector)
#print(selector.extract())
#子节点
selector = response.xpath('/html/*')
#print(selector)
#选中div的所有后代元素节点
selector = response.xpath('/html/body/div//*')
#print(selector)
#选中孙节点的所有E
selector = response.xpath('//div/*/img')
#print(selector)
#选中E的attr属性
selector = response.xpath('//img/@src')
#print(selector)
#选中文档的attr属性
selector = response.xpath("//@href")
#print(selector)
#选中E的所有属性
selector = response.xpath("//a[1]/img/@*")
#print(selector)


#TODO xpath 常用的函数

