from filecmp import cmp
# Python列表函数&方法

# 1	cmp(list1, list2)   比较两个列表的元素
# Python 2 中的 cmp() 行为
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 4]
list4 = [1, 2]

# Python 3 中直接使用比较运算符
print(list1 == list2)  # True (相等)
print(list1 == list3)  # False (不相等)
print(list1 < list3)   # True (小于)
print(list3 > list1)   # True (大于)
print(list1 > list4)   # True (list1 > list4，因为长度更长)
# Python 2 中直接使用比较运算符
""" print(cmp(list1, list2))  # 0  (相等)
print(cmp(list1, list3))  # -1 (小于)
print(cmp(list3, list1))  # 1  (大于)
print(cmp(list1, list4))  # 1  (list1 > list4，因为长度更长) """

# 2	len(list)   列表元素个数
# 3	max(list)   返回列表元素最大值
# 4	min(list)   返回列表元素最小值
# 5	list(seq)   将元组转换为列表
# 将元组转换为列表
tuple_data = (1, 2, 3, 4, 5)
list_data = list(tuple_data)
print(list_data)  # 输出: [1, 2, 3, 4, 5]
print(type(list_data))  # 输出: <class 'list'>
print(type(tuple_data))  # 输出: <class 'list'>


# 1	list.append(obj)    在列表末尾添加新的对象
# 2	list.count(obj)     统计某个元素在列表中出现的次数
# 3	list.extend(seq)    在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# 基本示例：扩展列表
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  # 输出: [1, 2, 3, 4, 5, 6]

# 4	list.index(obj)     从列表中找出某个值第一个匹配项的索引位置
# 5	list.insert(index, obj)     将对象插入列表
# insert(index, obj)
# index: 要插入的位置（索引）
# obj: 要插入的对象

list1 = ['a', 'b', 'c', 'd']
# 在开头插入
list1.insert(0, 'start')
print(list1)  # ['start', 'a', 'b', 'c', 'd']

# 在中间插入
list1.insert(3, 'middle')
print(list1)  # ['start', 'a', 'b', 'middle', 'c', 'd']

# 在末尾插入（相当于 append）
list1.insert(len(list1), 'end')
print(list1)  # ['start', 'a', 'b', 'middle', 'c', 'd', 'end']

# 6	list.pop([index=-1])    移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list1 = [1, 2, 3, 4, 5]

# 连续 pop()
print(list1.pop())  # 5
print(list1)        # [1, 2, 3, 4]
print(list1.pop())  # 4
print(list1)        # [1, 2, 3]
print(list1.pop())  # 3
print(list1)        # [1, 2]
print(list1.pop())  # 2
print(list1)        # [1]
print(list1.pop())  # 1
print(list1)        # []

list1 = [10, 20, 30, 40, 50]

# 移除索引0的元素
removed = list1.pop(0)
print(removed)  # 10
print(list1)    # [20, 30, 40, 50]

# 移除索引2的元素
removed = list1.pop(2)
print(removed)  # 40
print(list1)    # [20, 30, 50]

# 移除索引-1（最后一个）
removed = list1.pop(-1)
print(removed)  # 50
print(list1)    # [20, 30]

# 移除索引-2（倒数第二个）
removed = list1.pop(-2)
print(removed)  # 20
print(list1)    # [30]


# 7	list.remove(obj)    移除列表中某个值的第一个匹配项
# 基本示例：移除第一个匹配项
fruits = ['apple', 'banana', 'orange', 'banana', 'grape']
fruits.remove('banana')
print(fruits)  # 输出: ['apple', 'orange', 'banana', 'grape']
# 注意：只移除了第一个 'banana'

# 8	list.reverse()      反向列表中元素
# 基本示例：反转列表
fruits = ['apple', 'banana', 'orange', 'grape']
fruits.reverse()
print(fruits)  # 输出: ['grape', 'orange', 'banana', 'apple']


# 9	list.sort(cmp=None, key=None, reverse=False)    对原列表进行排序
# 基本示例：升序排序
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers)  # 输出: [1, 1, 2, 3, 4, 5, 9]

# 字符串排序
fruits = ['banana', 'apple', 'grape', 'orange']
fruits.sort()
print(fruits)  # 输出: ['apple', 'banana', 'grape', 'orange']

# 升序（默认）
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 9]

# 降序
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort(reverse=True)
print(numbers)  # [9, 5, 4, 3, 2, 1, 1]

# 字符串降序
fruits = ['banana', 'apple', 'grape', 'orange']
fruits.sort(reverse=True)
print(fruits)  # ['orange', 'grape', 'banana', 'apple']

# 按长度排序
words = ['python', 'java', 'c', 'javascript', 'go']
words.sort(key=len)
print(words)  # ['c', 'go', 'java', 'python', 'javascript']

# 按长度降序
words.sort(key=len, reverse=True)
print(words)  # ['javascript', 'python', 'java', 'go', 'c']

# 按第二个字符排序
words = ['apple', 'banana', 'grape', 'orange']
words.sort(key=lambda x: x[1])
print(words)  # ['banana', 'apple', 'grape', 'orange']

# 按多个条件排序
students = [
    ('Alice', 25, 95),
    ('Bob', 25, 88),
    ('Charlie', 23, 92),
    ('David', 23, 85)
]

# 先按年龄，再按分数
students.sort(key=lambda x: (x[1], x[2]))
print(students)
# [('David', 23, 85), ('Charlie', 23, 92), ('Bob', 25, 88), ('Alice', 25, 95)]

# 按年龄升序，分数降序
students.sort(key=lambda x: (x[1], -x[2]))
print(students)
# [('Charlie', 23, 92), ('David', 23, 85), ('Alice', 25, 95), ('Bob', 25, 88)]

# --------------------------------------------------------------------------------------------------------------

# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下实例:
tup1 = (12,34.56)
tup2 = ('abc', 'xyz')
 
# 以下修改元组元素操作是非法的。
# tup1[0] = 100
 
# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)

# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下实例:
tup = ('physics', 'chemistry', 1997, 2000)
 
print(tup)
del tup
print("After deleting tup : ")
# print(tup)


# 元组内置函数
# 1	cmp(tuple1, tuple2)     比较两个元组元素。
# Python 3 推荐方式：直接比较
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
tuple3 = (1, 2, 4)
tuple4 = (1, 2)

print(tuple1 == tuple2)  # True
print(tuple1 == tuple3)  # False
print(tuple1 < tuple3)   # True
print(tuple3 > tuple1)   # True
print(tuple1 > tuple4)   # True

# 2	len(tuple)      计算元组元素个数。
# 3	max(tuple)      返回元组中元素最大值。
# 4	min(tuple)      返回元组中元素最小值。
# 5	tuple(seq)      将列表转换为元组。
# 列表 → 元组
list1 = [1, 2, 3]
print(tuple(list1))  # (1, 2, 3)

list2 = ['a', 'b', 'c']
print(tuple(list2))  # ('a', 'b', 'c')

list3 = [1, 'hello', 3.14, True]
print(tuple(list3))  # (1, 'hello', 3.14, True)

# 嵌套列表
list4 = [[1, 2], [3, 4], [5, 6]]
print(tuple(list4))  # ([1, 2], [3, 4], [5, 6])

# -------------------------------------------------------------------------------
# 修改字典
# 向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:
tinydict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
 
tinydict['Age'] = 8 # 更新
tinydict['School'] = "RUNOOB" # 添加
 
 
print("tinydict['Age']: ", tinydict['Age'])
print("tinydict['School']: ", tinydict['School'])

# 删除字典元素
# 能删单一的元素也能清空字典，清空只需一项操作。
# 显示删除一个字典用del命令，如下实例：
tinydict = {'Name': 'Zara', 'Age': 9, 'Class': 'First'}
 
del tinydict['Name']  # 删除键是'Name'的条目
print("tinydict['Age']: ", tinydict['Age'])
# clear() - 清空字典内容，但字典对象保留
tinydict.clear()      # 清空字典所有条目
print(tinydict)  # 输出: {} (空字典，对象还在)

# del - 删除整个字典对象
""" del tinydict          # 删除字典
 
print("tinydict['Age']: ", tinydict['Age'])   # 报错: NameError: name 'tinydict' is not defined
print("tinydict['School']: ", tinydict['School']) """

# 字典键的特性
# 字典值可以没有限制地取任何 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。
# 两个重要的点需要记住：
# (1)不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
tinydict = {'Name': 'Runoob', 'Age': 7, 'Name': 'Manni'} 
 
print("tinydict['Name']: ", tinydict['Name'])

# (2)键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行，如下实例：
""" tinydict = {['Name']: 'Zara', 'Age': 7} 
 
print("tinydict['Name']: ", tinydict['Name']) #TypeError: unhashable type: 'list' """

# 字典内置函数&方法

# 1	cmp(dict1, dict2)   比较两个字典元素。
dict1 = {"a":"123","b":"456"}
dict2 = {"a":"123","b":"456"}
print(dict1 == dict2)
dict2 = {"a":"123","b":"4567"}
print(dict1 == dict2)

# 2	len(dict)   计算字典元素个数，即键的总数。
# 3	str(dict)   输出字典可打印的字符串表示。
# 4	type(variable)  返回输入的变量类型，如果变量是字典就返回字典类型。

# 不同数据类型
data = {
    'dict_var': {'name': 'Alice'},
    'list_var': [1, 2, 3],
    'str_var': 'Hello',
    'int_var': 42,
    'float_var': 3.14,
    'bool_var': True,
    'tuple_var': (1, 2),
    'set_var': {1, 2, 3}
}

for name, value in data.items():
    print(f"{name}: {type(value)}")
# 输出:
# dict_var: <class 'dict'>
# list_var: <class 'list'>
# str_var: <class 'str'>
# int_var: <class 'int'>
# float_var: <class 'float'>
# bool_var: <class 'bool'>
# tuple_var: <class 'tuple'>
# set_var: <class 'set'>


# 1	dict.clear()    删除字典内所有元素
# 2	dict.copy()     返回一个字典的浅复制
# 基本示例：浅复制字典
dict1 = {'name': 'Alice', 'age': 25}
dict2 = dict1.copy()
print(dict2)  # 输出: {'name': 'Alice', 'age': 25}

# 验证是否独立
dict2['age'] = 30
print(dict1)  # {'name': 'Alice', 'age': 25} (原字典不变)
print(dict2)  # {'name': 'Alice', 'age': 30} (只改变了副本)


# 3	dict.fromkeys(seq[, val])   创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
# 使用列表
keys = ['a', 'b', 'c']
dict1 = dict.fromkeys(keys)
print(dict1)  # {'a': None, 'b': None, 'c': None}

# 使用元组
keys = (1, 2, 3)
dict2 = dict.fromkeys(keys, 0)
print(dict2)  # {1: 0, 2: 0, 3: 0}

# 使用字符串
keys = 'ABC'
dict3 = dict.fromkeys(keys, 'value')
print(dict3)  # {'A': 'value', 'B': 'value', 'C': 'value'}

# 使用 range
keys = range(5)
dict4 = dict.fromkeys(keys, 'empty')
print(dict4)  # {0: 'empty', 1: 'empty', 2: 'empty', 3: 'empty', 4: 'empty'}

# 使用集合（顺序不保证）
keys = {1, 2, 3}
dict5 = dict.fromkeys(keys)
print(dict5)  # {1: None, 2: None, 3: None}

# 4	dict.get(key, default=None)     返回指定键的值，如果值不在字典中返回default值
# 5	dict.has_key(key)   如果键在字典dict里返回true，否则返回false。Python3 不支持。
# 6	dict.items()    以列表返回可遍历的(键, 值) 元组数组
# 基本示例：获取所有键值对
dict1 = {'name': 'Alice', 'age': 25, 'city': 'NYC'}
items = dict1.items()
print(items)  # 输出: dict_items([('name', 'Alice'), ('age', 25), ('city', 'NYC')])
print(type(items))  # 输出: <class 'dict_items'>

dict1 = {'name': 'Alice', 'age': 25, 'city': 'NYC'}

# 遍历所有键值对
for key, value in dict1.items():
    print(f"{key}: {value}")
# 输出:
# name: Alice
# age: 25
# city: NYC

# 使用索引遍历
for i, (key, value) in enumerate(dict1.items()):
    print(f"{i}: {key} = {value}")
# 输出:
# 0: name = Alice
# 1: age = 25
# 2: city = NYC

# 7	dict.keys()     以列表返回一个字典所有的键
# 8	dict.setdefault(key, default=None)      和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
# 9	dict.update(dict2)      把字典dict2的键/值对更新到dict里
# 基本示例：更新字典
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)
print(dict1)  # 输出: {'a': 1, 'b': 3, 'c': 4}
print(dict2)  # 输出: {'b': 3, 'c': 4}


# 10	dict.values()       以列表返回字典中的所有值
# 11	pop(key[,default])      删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
# 基本示例：删除并返回指定键的值
dict1 = {'name': 'Alice', 'age': 25, 'city': 'NYC'}
removed = dict1.pop('age')
print(removed)  # 输出: 25
print(dict1)    # 输出: {'name': 'Alice', 'city': 'NYC'}

# 12	popitem()       返回并删除字典中的最后一对键和值。
# 基本示例：删除并返回最后一对键值对
dict1 = {'a': 1, 'b': 2, 'c': 3}
item = dict1.popitem()
print(item)    # 输出: ('c', 3)  (注意：Python 3.7+ 保证返回最后一项)
print(dict1)   # 输出: {'a': 1, 'b': 2}