var1 = 'Hello World!'
var2 = "Python Runoob"
 
print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])

# Python 转义字符
# \(在行尾时)	续行符
# \\	反斜杠符号
# \'	单引号
# \"	双引号
# \a	响铃
# \b	退格(Backspace)
# \e	转义
# \000	空
# \n	换行
# \v	纵向制表符
# \t	横向制表符
# \r	回车
# \f	换页
# \oyy	八进制数，y 代表 0~7 的字符，例如：\012 代表换行。
# \xyy	十六进制数，以 \x 开头，yy代表的字符，例如：\x0a代表换行
# \other	其它的字符以普通格式输出

# Python字符串运算符
# +	字符串连接	
# >>>a + b
# 'HelloPython'
# *	重复输出字符串	
# >>>a * 2
# 'HelloHello'
# []	通过索引获取字符串中字符	
# >>>a[1]
# 'e'
# [ : ]	截取字符串中的一部分	
# >>>a[1:4]
# 'ell'
# in	成员运算符 - 如果字符串中包含给定的字符返回 True	
# >>>"H" in a
# True
# not in	成员运算符 - 如果字符串中不包含给定的字符返回 True	
# >>>"M" not in a
# True
# r/R	原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 
# 原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。	
# >>>print r'\n'
# \n
# >>> print R'\n'
# \n
# %	格式字符串	

a = "Hello"
b = "Python"
 
print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1]) 
print("a[1:4] 输出结果：", a[1:4])
 
if( "H" in a) :
    print("H 在变量 a 中") 
else :
    print("H 不在变量 a 中") 
 
if( "M" not in a) :
    print("M 不在变量 a 中") 
else :
    print("M 在变量 a 中")
 
print(r'\n')
print(R'\n')

#    %c	 格式化字符及其ASCII码
#    %s	 格式化字符串
#    %d	 格式化整数
#    %u	 格式化无符号整型
#    %o	 格式化无符号八进制数
#    %x	 格式化无符号十六进制数
#    %X	 格式化无符号十六进制数（大写）
#    %f	 格式化浮点数字，可指定小数点后的精度
#    %e	 用科学计数法格式化浮点数
#    %E	 作用同%e，用科学计数法格式化浮点数
#    %g	 %f和%e的简写
#    %G	 %F 和 %E 的简写
#    %p	 用十六进制数格式化变量的地址
# *	定义宽度或者小数点精度
# -	用做左对齐
# +	在正数前面显示加号( + )
# <sp>	在正数前面显示空格
# #	在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
# 0	显示的数字前面填充'0'而不是默认的空格
# %	'%%'输出一个单一的'%'
# (var)	映射变量(字典参数)
# m.n.	m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)


errHTML = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''
print(errHTML)


# string.capitalize()   把字符串的第一个字符大写
# string.center(width)  返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
text = "Hello"
width = 20  # 必须是整数
result = text.center(width)
print(result)
print(len(result))

# string.count(str, beg=0, end=len(string))     返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
text = "apple banana apple grape apple"
# 统计 "apple" 出现次数
print(text.count("apple"))          # 输出: 3
# 统计 "a" 出现次数
print(text.count("a"))              # 输出: 7
# 只统计前10个字符中 "a" 的出现次数
print(text.count("a", 0, 10))       # 输出: 3 (apple bana)
# 统计索引5到20之间 "apple" 的出现次数
print(text.count("apple", 5, 20))   # 输出: 1 (banana后面的apple)

# string.decode(encoding='UTF-8', errors='strict')      以 encoding 指定的编码格式解码 string，如果出错默认报一个 ValueError 的 异 常 ， 除非 errors 指 定 的 是 'ignore' 或 者'replace'
# string.encode(encoding='UTF-8', errors='strict')      以 encoding 指定的编码格式编码 string，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
# string.endswith(obj, beg=0, end=len(string))      检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
text = "hello world python"

# 在整个字符串中检查
print(text.endswith("python"))          # 输出: True

# 检查前5个字符是否以 "lo" 结尾 (索引0-4)
print(text.endswith("lo", 0, 5))        # 输出: True ("hello"以"lo"结尾)

# 检查索引5-10是否以 "wor" 结尾
print(text.endswith("wor", 5, 11))      # 输出: True (" world"中"wor"在开头)

# 检查索引6-11是否以 "orld" 结尾
print(text.endswith("orld", 6, 11))     # 输出: True

# string.expandtabs(tabsize=8)      把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8。

# string.find(str, beg=0, end=len(string))      检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
text = "hello world python"
#       0123456789012345678
#       h e l l o   w o r l d   p y t h o n

print(text.find("o"))           # 输出: 4 (第一个o在索引4)
print(text.find("o", 5))        # 输出: 7 (从索引5开始找，找到索引7的o)
print(text.find("o", 0, 5))     # 输出: 4 (在索引0-4范围内找o)
print(text.find("o", 10, 15))   # 输出: -1 (索引10-15没有o)

# string.format()   格式化字符串
# 通过索引指定顺序
print("{1} {0}".format("World", "Hello"))  # 输出: Hello World
print("{0} is {1} years old".format("Alice", 25))  # 输出: Alice is 25 years old

# 重复使用
print("{0} {1} {0}".format("Hello", "World"))  # 输出: Hello World Hello

# 使用变量名
print("{name} is {age} years old".format(name="Bob", age=30))   # 输出: Bob is 30 years old


# string.index(str, beg=0, end=len(string))     跟find()方法一样，只不过如果str不在 string中会报一个异常.


# string.isalnum()   如果 string 至少有一个字符并且所有字符都是字母或数字则返      回 True,否则返回 False

# string.isalpha()  如果 string 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False

# string.isdecimal()    如果 string 只包含十进制数字则返回 True 否则返回 False.
# 只包含十进制数字
print("123".isdecimal())      # 输出: True
print("456789".isdecimal())   # 输出: True
print("0".isdecimal())        # 输出: True

# 包含非数字字符
print("123a".isdecimal())     # 输出: False
print("12.3".isdecimal())     # 输出: False (小数点不是十进制数字)
print("123 ".isdecimal())     # 输出: False (空格不是十进制数字)
print("".isdecimal())         # 输出: False (空字符串)

# string.isdigit()      如果 string 只包含数字则返回 True 否则返回 False.

# string.islower()      如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False

# string.isnumeric()    如果 string 中只包含数字字符，则返回 True，否则返回 False

# string.isspace()  如果 string 中只包含空格，则返回 True，否则返回 False.

# string.istitle()  如果 string 是标题化的(见 title())则返回 True，否则返回 False
# 正确的标题格式：
# 1. 每个单词首字母大写
# 2. 其他字母小写
# 3. 非字母字符（数字、符号）不影响判断
print("Hello World Python".istitle())    # True
print("Hello123 World".istitle())        # True (数字不影响)
print("Hello-World".istitle())           # True (连字符分隔单词)
print("Hello_World".istitle())           # True (下划线分隔单词)

# 不符合的情况：
print("Hello wORLD".istitle())           # False (wORLD格式不对)
print("HELLO World".istitle())           # False (HELLO全大写)
print("hello World".istitle())           # False (hello首字母小写)

# string.isupper()      如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False

# string.join(seq)      以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
# 各种分隔符
data = ["2024", "01", "15"]

print("-".join(data))      # 输出: 2024-01-15
print("/".join(data))      # 输出: 2024/01/15
print(".".join(data))      # 输出: 2024.01.15
print(":".join(data))      # 输出: 2024:01:15
print("  ".join(data))     # 输出: 2024  01  15

# 多字符分隔符
words = ["Hello", "World"]
print("---".join(words))   # 输出: Hello---World
print(" <=> ".join(words)) # 输出: Hello <=> World

# string.ljust(width)       返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
# 基本示例：左对齐，用空格填充
text = "Hello"
print(text.ljust(10))  # 输出: "Hello     " (后面5个空格)

# 查看效果（用边界标记）
print(f"|{text.ljust(10)}|")  # 输出: |Hello     |
print(f"|{text.ljust(15)}|")  # 输出: |Hello          |

# string.lower()        转换 string 中所有大写字符为小写.

# string.lstrip()       截掉 string 左边的空格

# string.maketrans(intab, outtab)       maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
# 创建转换表：将 a->1, b->2, c->3
trans = str.maketrans("abc", "123")
text = "abc def abc"
print(text.translate(trans))  # 输出: 123 def 123

# 对应关系：
# a -> 1
# b -> 2
# c -> 3
# 其他字符保持不变


# max(str)      # 返回字符串 str 中最大的字母。
print(max("apjhcz"))

# min(str)      # 返回字符串 str 中最小的字母。
print(min("apjhcz"))

# string.partition(str)     # 有点像 find()和 split()的结合体,从 str 出现的第一个位置起,把 字 符 串 string 分 成 一 个 3 元 素 的 元 组 (string_pre_str,str,string_post_str),
# 如果 string 中不包含str 则 string_pre_str == string.
# 基本示例：分割字符串
text = "Hello World Python"
result = text.partition("World")
print(result)  # 输出: ('Hello ', 'World', ' Python')

# 查看元组内容
print(f"前: '{result[0]}'")   # 输出: 前: 'Hello '
print(f"分隔符: '{result[1]}'") # 输出: 分隔符: 'World'
print(f"后: '{result[2]}'")   # 输出: 后: ' Python'

# string.replace(str1, str2,  num=string.count(str1))       把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.

# string.rfind(str, beg=0,end=len(string) )     类似于 find() 函数，返回字符串最后一次出现的位置，如果没有匹配项则返回 -1。

# string.rindex( str, beg=0,end=len(string))    类似于 index()，不过是返回最后一个匹配到的子字符串的索引号。

# string.rjust(width)       返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
text = "Hello"

print(f"|{text.ljust(10)}|")    # 左对齐: |Hello     |
print(f"|{text.rjust(10)}|")    # 右对齐: |     Hello|
print(f"|{text.center(10)}|")   # 居中:   |  Hello   |

# string.rpartition(str)    类似于 partition()函数,不过是从右边开始查找
# 基本示例：从右边开始分割
text = "a:b:c:d"
result = text.rpartition(":")
print(result)  # 输出: ('a:b:c', ':', 'd')

# 查看元组内容
print(f"前: '{result[0]}'")   # 输出: 前: 'a:b:c'
print(f"分隔符: '{result[1]}'") # 输出: 分隔符: ':'
print(f"后: '{result[2]}'")   # 输出: 后: 'd'

# string.rstrip()       删除 string 字符串末尾的空格.

# string.split(str="", num=string.count(str))       以 str 为分隔符切片 string，如果 num 有指定值，则仅分隔 num+1 个子字符串
# 基本示例：默认按空格分割
text = "Hello World Python"
result = text.split()
print(result)  # 输出: ['Hello', 'World', 'Python']

# 指定分隔符
text = "apple,banana,orange,grape"
result = text.split(",")
print(result)  # 输出: ['apple', 'banana', 'orange', 'grape']

# string.splitlines([keepends])     按照行('\r', '\r\n', '\n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
# 基本示例：按行分割
text = "Hello\nWorld\nPython"
result = text.splitlines()
print(result)  # 输出: ['Hello', 'World', 'Python']

# 保留换行符
result = text.splitlines(True)
print(result)  # 输出: ['Hello\n', 'World\n', 'Python']

text = "Line1\nLine2\rLine3\r\nLine4"
result = text.splitlines()
print(result)  # 输出: ['Line1', 'Line2', 'Line3', 'Line4']

# 查看换行符类型
text = "Line1\nLine2\rLine3\r\nLine4"
for line in text.splitlines(True):
    print(repr(line))

# 输出:
# 'Line1\n'
# 'Line2\r'
# 'Line3\r\n'
# 'Line4'

# string.startswith(obj, beg=0,end=len(string))     检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查.

# string.strip([obj])   在 string 上执行 lstrip()和 rstrip()

# string.swapcase()     翻转 string 中的大小写

# string.title()        返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())

# string.translate(str, del="")      根据 str 给出的表(包含 256 个字符)转换 string 的字符,  创建转换表    要过滤掉的字符放到 del 参数中
trans = str.maketrans("aeiou", "12345")
text = "hello world"
print(text.translate(trans))  # 输出: h2ll4 w4rld

# 对应关系：
# a->1, e->2, i->3, o->4, u->5
# h e l l o   w o r l d
# h 2 l l 4   w 4 r l d


# string.upper()        转换 string 中的小写字母为大写

# string.zfill(width)       返回长度为 width 的字符串，原字符串 string 右对齐，前面填充0
# 基本示例：用0填充到指定宽度
text = "42"
result = text.zfill(5)
print(result)  # 输出: 00042
""" f 前缀表示这是一个格式化字符串
{result} 是占位符，会被变量 result 的值替换
| 是普通字符，用于标记边界 """
print(f"|{result}|")  # 输出: |00042|

# 查看效果
text = "Hello"
print(text.zfill(10))  # 输出: 00000Hello


