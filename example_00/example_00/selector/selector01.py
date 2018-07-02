# -*- coding: utf-8 -*-

from scrapy.selector import Selector

text = '''
    <html>
        <body>
            <h1>hello world</h1>
            <h1>hello scrapy</h1>
            <h1>hello python</h1>
            <ul>
                <li>c++</li>
                <li>java</li>
                <li>python</li>
            </ul>
        </body>
    <html>
       '''
selector = Selector(text=text)
#print(selector)    

#xpath选取所有的h1节点

selector_list = selector.xpath('//h1')
#print(selector_list)

#遍历selector_list
for sel in selector_list:
    #print(sel.xpath('./text()'))
    #print(type(sel.xpath('./text()')))
    pass


#extarct()方法：

s1 = selector.xpath('.//li')
#print(s1)
s1Value = s1[0].extract()
#print(s1Value)

s1 = selector.xpath('.//li/text()')
#print(s1)
#print(s1.extract()) 

text = '''

        <ul>
            <li>python学习手册 <b>价格:99.00元</b></li>
            <li>python核心编程 <b>价格:88.00元</b></li>
            <li>python基础教程 <b>价格:80.00元</b></li>
        </ul>
       '''
selector = Selector(text=text)
#print(selector) 
print(selector.xpath('.//li/b/text()'))  
#正则只取数字部分
print(selector.xpath('.//li/b/text()').re('\d+\.\d+')) 
#只取第一个元素的数字
print(selector.xpath('.//li/b/text()')).re_first('\d+\.\d+')     