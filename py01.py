""" 在 Python 里，标识符由字母、数字、下划线组成。
在 Python 中，所有标识符可以包括英文、数字以及下划线(_)，但不能以数字开头。
Python 中的标识符是区分大小写的。 
以下划线开头的标识符是有特殊意义的。以单下划线开头 _foo 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入。
以双下划线开头的 __foo 代表类的私有成员，以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。"""
# A = 1;
# a = 2;
# print(a);
# print(A);

# 缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。
""" a = 6
if a<5:
    print ("True")
    a += 1 
    else:
    print ("False") 报错
 """

""" Python语句中一般以新行作为语句的结束符。
但是我们可以使用斜杠（ \）将一行的语句分为多行显示，如下所示： """
item_one = 1
item_two = 2
item_three = 3
total = item_one + \
        item_two + \
        item_three
print(total)

# 语句中包含 [], {} 或 () 括号就不需要使用多行连接符。如下实例：
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

# 等待用户输入
# user_input = input("按下 enter 键退出，其他任意键显示...\n")

# 判断用户输入了什么
""" if user_input == "":
    print("你按了 Enter 键，程序退出")
else:
    # 在字符串里直接嵌入变量
    print(f"你按了其他键：{user_input}")

# 程序结束
print("程序已退出") """

#!/usr/bin/python
# sys.stdout.write直接调用底层输出流的方法
import sys; x = 'runoob'; sys.stdout.write(x + '\n')

# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号。
""" a = 1
b = 2
# 换行输出
print(a)
print(b)
# 不换行输出
print(a, end=" ")
print(b, end=" ")
print(a,b) """

""" Python 中的变量赋值不需要类型声明。
每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。
每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
等号 = 用来给变量赋值。
等号 = 运算符左边是一个变量名，等号 = 运算符右边是存储在变量中的值。 """
counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串
 
print (counter)
print (miles)
print (name)

# 多个变量赋值
# a = b = c = 1
""" a, b, c = 1, 2, "john"
print(a)
print(b)
print(c) """

""" Python有五个标准的数据类型：
Numbers（数字）
String（字符串）
List（列表）
Tuple（元组）
Dictionary（字典） """

var1 = 1
var2 = 10
var1 = "123231w"
print(var1)

# del语句的用法
a = 10
b = 20
c = 30
# 使用del语句删除一些对象的引用
""" del a, b, c   # 一次删除 3 个变量

print(a)  # 报错：a 已经被删了
print(b)  # 报错：b 已经被删了
print(c)  # 报错：c 已经被删了 """

# 删除列表中的元素
list_ = [1, 2, 3, 4, 5]

del list_[0]      # 删除第 1 个元素
print(list_)      # [2, 3, 4, 5]

# 起始索引 1（包含）结束索引 3（不包含）
del list_[1:3]    # 删除第 2 到第 3 个元素
print(list_)      # [2, 5]


# 删除字典中的键值对
dict_ = {"name": "张三", "age": 18, "city": "北京"}

del dict_["age"]  # 删除 age 这个键值对
print(dict_)      # {"name": "张三", "city": "北京"}
# Python 3 整数 long合并到 int  整数都是int

""" str = 'HelloWorld!'
 
print (str)  # 输出完整字符串
print (str[0])  # 输出字符串中的第一个字符
print (str[2:5])  # 输出字符串中第三个至第六个之间的字符串
print (str[2:])  # 输出从第三个字符开始的字符串
print (str * 2)  # 输出字符串两次
print (str + "TEST")  # 输出连接的字符串 """

""" List（列表） 是 Python 中使用最频繁的数据类型。
列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。
列表用 [ ] 标识，是 python 最通用的复合数据类型。
列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。 """
""" list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
 
print (list)               # 输出完整列表
print (list[0])            # 输出列表的第一个元素
print (list[1:3])          # 输出第二个至第三个元素 
print (list[2:])           # 输出从第三个开始至列表末尾的所有元素
print (tinylist * 2)       # 输出列表两次
print (list + tinylist)    # 打印组合的列表
print (list[1:4:2])        # list[起始索引 : 结束索引 : 步长] """

# 元组是有序的、不可变的、可以存放任意类型数据的序列。
""" tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tuple[2] = 1000    # 元组中是非法应用
list[2] = 1000     # 列表中是合法应用 """


 
""" 字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典用"{ }"标识。字典由索引(key)和它对应的值value组成。 """
""" dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'runoob','code':6734, 'dept': 'sales'}

print (dict['one'])          # 输出键为'one' 的值
print (dict[2])              # 输出键为 2 的值
print(dict)
print (tinydict)             # 输出完整的字典
print (tinydict.keys())      # 输出所有键
print (tinydict.values())    # 输出所有值 """

# 转整数
a = "123"
print(int(a))
print(int("1a", 16))  # 26（十六进制转十进制）
print(int("1010", 2))  # 10（二进制转十进制）

# 整数转浮点
print(float(3))    # 3.0
print(float("3.14"))    # 3.14
print(float(True))  # 1.0
print(float(False)) # 0.0

# 几乎所有类型都能转字符串
print(str(123))         # "123"
print(str(3.14))        # "3.14"
print(str(True))        # "True"
print(str([1, 2, 3]))   # "[1, 2, 3]"
print(str({'a': 1}))    # "{'a': 1}"

# 转为布尔值 bool()
# 以下情况返回 False
print(bool(0))         # False
print(bool(0.0))       # False
print(bool(""))        # False
print(bool([]))        # False
print(bool({}))        # False
print(bool(None))      # False
print(bool(False))     # False

# 其他所有值都返回 True
print(bool(1))         # True
print(bool(-1))        # True
print(bool("abc"))     # True
print(bool([1, 2]))    # True

# 转为列表 list()
# 字符串 → 列表（每个字符变成元素）
print(list("hello"))    # ['h', 'e', 'l', 'l', 'o']

# 元组 → 列表
print(list((1, 2, 3)))  # [1, 2, 3]

# 集合 → 列表
print(list({1, 2, 3}))  # [1, 2, 3]

# 字典 → 列表（只转键）
print(list({'a': 1, 'b': 2}))  # ['a', 'b']

# 范围 → 列表
# range 是 Python 中的一个内置函数，用来生成一个整数序列。它本身不存储所有数字，而是按需生成，非常节省内存。
print(list(range(5)))   # [0, 1, 2, 3, 4]

# 转为元组 tuple()
# 列表 → 元组
print(tuple([1, 2, 3]))  # (1, 2, 3)

# 字符串 → 元组
print(tuple("hello"))    # ('h', 'e', 'l', 'l', 'o')

# 集合 → 元组
print(tuple({1, 2, 3}))  # (1, 2, 3)

# 转为集合 set()
# 列表 → 集合（自动去重）
print(set([1, 2, 2, 3]))  # {1, 2, 3}

# 字符串 → 集合
print(set("hello"))       # {'h', 'e', 'l', 'o'}

# 转为字典 dict()
# 从键值对列表转换
print(dict([('a', 1), ('b', 2)]))  # {'a': 1, 'b': 2}

# 从关键字参数转换
print(dict(a=1, b=2))  # {'a': 1, 'b': 2}

a=10
b=3
# 幂 - 返回x的y次幂
print(a**b)
print(b**a)

# 取整除 - 返回商的整数部分(向下取整)
print(a//b)


if a == b:
    print(a,"等于",b)
else:
    print(a,"不等于",b,sep="")

a = 10
b = 20
 
if  a and b :
   print("1 - 变量 a 和 b 都为 True")
else:
   print("1 - 变量 a 和 b 有一个不为 True")
 
if  a or b :
   print("2 - 变量 a 和 b 都为 True，或其中一个变量为 True")
else:
   print("2 - 变量 a 和 b 都不为 True")
 
# 修改变量 a 的值
a = 0
b = 0
if  a and b :
   print("3 - 变量 a 和 b 都为 True")
else:
   print("3 - 变量 a 和 b 有一个不为 True")
 
if  a or b :
   print("4 - 变量 a 和 b 都为 True，或其中一个变量为 True")
else:
   print("4 - 变量 a 和 b 都不为 True")
 
if not( a and b ):
   print("5 - 变量 a 和 b 都为 False，或其中一个变量为 False")
else:
   print("5 - 变量 a 和 b 都为 True")

a=10
b=20
list = [1,2,3,4,5]

if a in list:
   print("1 - 变量 a 在给定的列表中 list 中")
else:
   print("1 - 变量 a 不在给定的列表中 list 中")

if b not in list:
   print("2 - 变量 b 不在给定的列表中 list 中")
else:
   print("2 - 变量 b 在给定的列表中 list 中")

# 修改变量 a 的值
a = 2
if ( a in list ):
   print("3 - 变量 a 在给定的列表中 list 中")
else:
   print("3 - 变量 a 不在给定的列表中 list 中")


a = 20
b = 20
 
# is 是判断两个标识符是不是引用自一个对象
if ( a is b ):
   print("1 - a 和 b 有相同的标识")
else:
   print("1 - a 和 b 没有相同的标识")

# is not 是判断两个标识符是不是引用自不同对象
if a is not b:
   print("2 - a 和 b 没有相同的标识")
else:
   print("2 - a 和 b 有相同的标识")

b = 30
if a is b:
   print("3 - a 和 b 有相同的标识")
else:
   print("3 - a 和 b 没有相同的标识")

if ( a is not b ):
   print("4 - a 和 b 没有相同的标识")
else:
   print("4 - a 和 b 有相同的标识")


""" is 与 == 区别：
is 用于判断两个变量引用对象是否为同一个(同一块内存空间)， == 用于判断引用变量的值是否相等。 """
a = [1, 2, 3]

# 方式1：直接赋值（引用）
b = a
# b 和 a 指向同一个对象，修改 b 会影响 a
print(a is b)
print(a == b)

# 方式2：切片复制（新对象）
b = a[:]
# b 是 a 的副本，指向不同的内存地址，修改 b 不影响 a
print(a is b)
print(a == b)

a = 1
while(a<7):
   if(a % 2 == 0):
      print(a,"is even")
   else:
      print(a,"is odd")
   a+=1
num = 5
if num == 3:
   print("boss")
elif num == 2:
   print("user")
elif num == 1:
   print("worker")
elif num < 0: 
   print("error")
else:
   print("roadman")


# 由于 python 并不支持 switch 语句，所以多个条件判断，只能用 elif 来实现，如果判断需要多个条件需同时判断时，
# 可以使用 or （或），表示两个条件有一个成立时判断条件成功；使用 and （与）时，表示只有两个条件同时成立的情况下，判断条件才成功。
num = 9
if num >= 0 and num <= 10:    # 判断值是否在0~10之间
    print('hello')
# 输出结果: hello
 
num = 10
if num < 0 or num > 10:    # 判断值是否在小于0或大于10
    print('hello')
else:
    print('undefine')
# 输出结果: undefine
 
num = 8
# 判断值是否在0~5或者10~15之间
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):    
    print('hello')
else:
    print('undefine')
# 输出结果: undefine

var = 100 
if ( var  == 100 ) : print("变量 var 的值为",var,sep="")