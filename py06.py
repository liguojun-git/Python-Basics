
import modeule.support
# 定义一个函数
# 你可以定义一个由自己想要功能的函数，以下是简单的规则：

# 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
# 任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
# 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
# 函数内容以冒号起始，并且缩进。
# return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

# 定义函数


def PrName(name):
    print(name)
    return

PrName("小明")
PrName("小红")

# python 传不可变对象实例
# 当 a = 10 时，变量 a 指向了一个新的内存地址，而原来的 b 仍然指向原来的地址。
def ChangeInt( a ):
    a = 10
 
b = 2
ChangeInt(b)
print(b) # 结果是 2


# 传可变对象实例
def changeme( mylist2 ):
   mylist2.append([1,2,3,4])
   print("函数内取值: ", mylist2)
   return
 
# 调用changeme函数
mylist1 = [10,20,30]
changeme( mylist1 )
print("函数外取值: ", mylist1)

#可写函数说明
def printinfo( name, age ):
   "打印任何传入的字符串"
   print("Name: ", name)
   print("Age ", age)
   return
 
#调用printinfo函数
printinfo( age=50, name="miki" )

# 加了星号（*）的变量名会存放所有未命名的变量参数。不定长参数实例如下：
# 可写函数说明
def printinfo( arg1, *vartuple ):
   print("输出: ")
   print(arg1)
   for var in vartuple:
      print(var)
   return
 
# 调用printinfo 函数
printinfo( 10 )
printinfo( 70, 60, 50 )


# 匿名函数
# python 使用 lambda 来创建匿名函数。
# lambda只是一个表达式，函数体比def简单很多。
# lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
# lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
# 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
# 语法
# lambda函数的语法只包含一个语句，如下：
# lambda [arg1 [,arg2,.....argn]]:expression

# lambda 语法
# lambda 参数: 表达式

# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2
 
# 调用sum函数
print("相加后的值为 : ", sum( 10, 20 ))
print("相加后的值为 : ", sum( 20, 20 ))

# 全局变量的 total和 局部变量定义的total是俩个不同的变量
total = 0 # 这是一个全局变量
# 可写函数说明
def sum( arg1, arg2 ):
   #返回2个参数的和."
   total = arg1 + arg2 # total在这里是局部变量.
   print("函数内是局部变量 : ", total)
   return total
 
#调用sum函数
sum( 10, 20 )
print("函数外是全局变量 : ", total)


result = modeule.support.print_func("123")
