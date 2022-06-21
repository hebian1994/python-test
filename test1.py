

import requests
# 引入 requests，实现请求

URL = 'http://c.biancheng.net/uploads/course/python_spider/191009.html'
# 输入在浏览器的网址

res = requests.get(URL)
# 发送 GET 方式的请求，并把返回的结果(响应)存储在 res 变量里头
# 答第二个问题，get() 方法需要输入一个网页链接

print(type(res))

# 是时候回答第三个问题了，通过 type 查看返回的数据是什么对象。