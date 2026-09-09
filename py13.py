# JSON 解码为 Python 类型转换对应表：
# JSON	                Python
# object	            dict
# array	                list
# string	            str
# number (int)      	int
# number (real)     	float
# true              	True
# false             	False
# null              	None


import json
 
# Python 字典类型转换为 JSON 对象
data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'https://www.runoob.com'
}
 
json_str = json.dumps(data)
print ("Python 原始数据：", repr(data))
print ("JSON 对象：", json_str)

 
# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])