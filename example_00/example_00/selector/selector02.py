# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

body = '''
       <html>
       <body>
        <h1>hello wolrd</h1>
        <h1>hello scrapy</h1>
        <h1>hello python</h1>

        <ul>
            <li>c++</li>
            <li>java</li>
            <li>python</li>
        </ul>
       </body>
       </html>
       '''
response = HtmlResponse(url='http://www.example.com',body=body)
print(response)
selector = Selector(response=response)
print(selector)       
