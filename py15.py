# Python requests 模块
# Python requests 是一个常用的 HTTP 请求库，可以方便地向网站发送 HTTP 请求，并获取响应结果。
# requests 模块比 urllib 模块更简洁。
# 使用 requests 发送 HTTP 请求需要先导入 requests 模块：

# 导入 requests 包
import requests

# 发送请求
x = requests.get('https://www.runoob.com/')

# 返回网页内容
# print(x.text)
print(x.status_code)  # 获取响应状态码
print(x.headers)  # 获取响应头
# print(x.content)  # 获取响应内容

# apparent_encoding	            编码方式
# close()	                    关闭与服务器的连接
# content	                    返回响应的内容，以字节为单位
# cookies	                    返回一个 CookieJar 对象，包含了从服务器发回的 cookie
# elapsed	                    返回一个 timedelta 对象，包含了从发送请求到响应到达之间经过的时间量，可以用于测试响应速度。比如 r.elapsed.microseconds 表示响应到达需要多少微秒。
# encoding	                    解码 r.text 的编码方式
# headers	                    返回响应头，字典格式
# history	                    返回包含请求历史的响应对象列表（url）
# is_permanent_redirect	        如果响应是永久重定向的 url，则返回 True，否则返回 False
# is_redirect	                如果响应被重定向，则返回 True，否则返回 False
# iter_content()	            迭代响应
# iter_lines()	                迭代响应的行
# json()	                    返回结果的 JSON 对象 (结果需要以 JSON 格式编写的，否则会引发错误)
# links	                        返回响应的解析头链接
# next	                        返回重定向链中下一个请求的 PreparedRequest 对象
# ok	                        检查 "status_code" 的值，如果小于400，则返回 True，如果不小于 400，则返回 False
# raise_for_status()	        如果发生错误，方法返回一个 HTTPError 对象
# reason	                    响应状态的描述，比如 "Not Found" 或 "OK"
# request	                    返回请求此响应的请求对象
# status_code	                返回 http 的状态码，比如 404 和 200（200 是 OK，404 是 Not Found）
# text	                        返回响应的内容，unicode 类型数据
# url	                        返回响应的 URL

# 响应状态的描述
print(x.reason)

# 返回编码
print(x.apparent_encoding)

j = requests.get('https://www.runoob.com/try/ajax/json_demo.json')
# 返回 json 数据
print(j.json())


# delete(url, args)	发送 DELETE 请求到指定 url
# get(url, params, args)	发送 GET 请求到指定 url
# head(url, args)	发送 HEAD 请求到指定 url
# patch(url, data, args)	发送 PATCH 请求到指定 url
# post(url, data, json, args)	发送 POST 请求到指定 url
# put(url, data, args)	发送 PUT 请求到指定 url
# request(method, url, args)	向指定的 url 发送指定的请求方法


kw = {'s':'python 教程'}

# 设置请求头
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
 
# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
response = requests.get("https://www.runoob.com/", params = kw, headers = headers)

# 查看响应状态码
print (response.status_code)

# 查看响应头部字符编码
print (response.encoding)

# 查看完整url地址
print (response.url)

# 查看响应内容，response.text 返回的是Unicode格式的数据
# print(response.text)


# post() 方法可以发送 POST 请求到指定 url，一般格式如下：
# requests.post(url, data={key: value}, json={key: value}, args)
# url 请求 url。
# data 参数为要发送到指定 url 的字典、元组列表、字节或文件对象。
# json 参数为要发送到指定 url 的 JSON 对象。
# args 为其他参数，比如 cookies、headers、verify等

# 发送请求
x = requests.post('https://www.runoob.com/try/ajax/demo_post.php')

# 返回网页内容
print(x.text)


# 表单参数，参数名为 fname 和 lname
myobj = {'fname': 'RUNOOB','lname': 'Boy'}

# 发送请求
x = requests.post('https://www.runoob.com/try/ajax/demo_post2.php', data = myobj)

# 返回网页内容
print(x.text)

# headers = {'User-Agent': 'Mozilla/5.0'}  # 设置请求头
# params = {'key1': 'value1', 'key2': 'value2'}  # 设置查询参数
# data = {'username': 'example', 'password': '123456'}  # 设置请求体
# response = requests.post('https://www.runoob.com', headers=headers, params=params, data=data)