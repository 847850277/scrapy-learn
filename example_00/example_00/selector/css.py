# -*- coding: utf-8 -*-
'''
css选择器
'''
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
body = '''
        <html>
            <head>
                <base="http://www.example.com">
                <title>Example website</title>
            </head>
            <body>
                <div id = "images-1" style="width:1230px;">
                    <a href="image1.html">Name:Image 1 </br><img src="image1.jpg"></a>
                    <a href="image2.html">Name:Image 2 </br><img src="image2.jpg"></a>
                    <a href="image3.html">Name:Image 3 </br><img src="image3.jpg"></a>
                </div>
                <div id = "images-2" class="small">
                    <a href="image4.html">Name:Image 4 </br><img src="image4.jpg"></a>
                    <a href="image5.html">Name:Image 5 </br><img src="image5.jpg"></a>
                </div>
            </body>
        </html>
       ''' 
response = HtmlResponse(url="http://www.example.com",body=body)
#print(response)       

#选中所有的img标签
selector = response.css("img")
#print(selector)

#选中所有的base和title
selector =  response.css("base,title")
#print(selector)

#选中div后代的img
selector = response.css("div img")
#print(selector)

#选中body后面的div
selector = response.css('body > div')
#print(selector)
#print(len(selector))

#选中包含attr属性的元素
#选中包含style属性的数据
selector = response.css('[style]')
#print(selector)

#选中包含attr属性并且值为value的元素
selector = response.css('[id=images-1]')
#print(selector)

#选中E元素，并且元素必须是其父元素的第n个字元素
#选中每个div的第一个a
selector = response.css('div >a:nth-child(1)')
#print(selector)
#print(len(selector))
#选中第二个div的第一个a
selector = response.css('div:nth-child(2)>a:nth-child(1)')
#print(selector)
#选中E元素，该元素必须是其父级元素的第一个元素
#选中E元素，该元素必须是其父级元素的最后一个元素
#选中第一个div的最后一个a
selector = response.css('div:first-child>a:last-child')
#print(selector)
#选中E元素所有的文本节点
selector = response.css('a::text')
print(selector)





