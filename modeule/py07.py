from importlib import reload
import support
import mymodule

# Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中。语法如下：
# from support import print_func

# from…import* 语句
# 把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：

# from support import *

# 在 Windows 系统，典型的 PYTHONPATH 如下：
# set PYTHONPATH=c:\python27\lib;
# 在 UNIX 系统，典型的 PYTHONPATH 如下：
# set PYTHONPATH=/usr/local/lib/python


# print_func("小明")


# 命名空间和作用域
# 变量是拥有匹配对象的名字（标识符）。命名空间是一个包含了变量名称们（键）和它们各自相应的对象们（值）的字典。
# 一个 Python 表达式可以访问局部命名空间和全局命名空间里的变量。如果一个局部变量和一个全局变量重名，则局部变量会覆盖全局变量。
# 每个函数都有自己的命名空间。类的方法的作用域规则和通常函数的一样。
# Python 会智能地猜测一个变量是局部的还是全局的，它假设任何在函数内赋值的变量都是局部的。
# 因此，如果要给函数内的全局变量赋值，必须使用 global 语句。
# global VarName 的表达式会告诉 Python， VarName 是一个全局变量，这样 Python 就不会在局部命名空间里寻找这个变量了。
# 例如，我们在全局命名空间里定义一个变量 Money。我们再在函数内给变量 Money 赋值，然后 Python 会假定 Money 是一个局部变量。
# 然而，我们并没有在访问前声明一个局部变量 Money，结果就是会出现一个 UnboundLocalError 的错误。取消 global 语句前的注释符就能解决这个问题。

""" Money = 2000  # 全局变量

# Python 看到这里有赋值: Money = Money + 1
# 所以 Python 决定 Money 是局部变量
# 但 print(Money) 想要读取这个局部变量
# 可是这个局部变量还没有被赋值！
# → UnboundLocalError
def AddMoney():
    print(Money)  # ❌ 先读取
    Money = Money + 1  # 然后赋值

AddMoney()
# 报错: UnboundLocalError: local variable 'Money' referenced before assignment """


""" Money = 2000  # 全局变量

def AddMoney():
    global Money  # 告诉 Python: "Money 是全局变量，不是局部变量"
    print(Money)  # 读取全局变量 → 2000
    Money = Money + 1  # 修改全局变量
    print(Money)  # 2001

AddMoney()
print(Money)  # 2001 (全局变量被修改了)
 """
Money = 2000

def AddMoney(money):
    # 使用参数，不修改全局变量
    money = money + 1
    print(money)
    return money

Money = AddMoney(Money)  # 接收返回值
print(Money)  # 2001

# dir()函数
# dir() 函数一个排好序的字符串列表，内容是一个模块里定义过的名字。
# 返回的列表容纳了在一个模块里定义的所有模块，变量和函数。如下一个简单的实例：
content = dir(support)
print(content)


# globals() 和 locals() 函数
# 根据调用地方的不同，globals() 和 locals() 函数可被用来返回全局和局部命名空间里的名字。
# 如果在函数内部调用 locals()，返回的是所有能在该函数里访问的命名。
# 如果在函数内部调用 globals()，返回的是所有在该函数里能访问的全局名字。
# 两个函数的返回类型都是字典。所以名字们能用 keys() 函数摘取。

# globals() - 返回全局命名空间的字典
# locals() - 返回局部命名空间的字典

x = 10  # 全局变量
y = 20

def test():
    a = 1  # 局部变量
    b = 2
    print("局部变量:", locals())
    print("全局变量:", globals())

test()


# reload() 函数
# 当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。
# 因此，如果你想重新执行模块里顶层部分的代码，可以用 reload() 函数。该函数会重新导入之前导入过的模块。语法如下：
print("=" * 40)
print("1. 第一次导入")
print("=" * 40)
# 此时会输出：模块被加载了！
mymodule.say_hello()  # 你好，我是小明

print("\n" + "=" * 40)
print("2. 直接再次导入（不会重新执行）")
print("=" * 40)
import mymodule  # 不会有任何输出
mymodule.say_hello()  # 还是：你好，我是小明

print("\n" + "=" * 40)
print("3. 使用 reload() 重新加载")
print("=" * 40)
reload(mymodule)  # 重新执行 mymodule.py
mymodule.say_hello()  # 如果是修改后的版本，会输出新内容