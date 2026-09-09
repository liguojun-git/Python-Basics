# 读取键盘输入
""" str = input("请输入：")
print("你输入的内容是: ", str) """

# open 函数
# 你必须先用Python内置的open()函数打开一个文件，创建一个file对象，相关的方法才可以调用它进行读写。
# 语法：
# file object = open(file_name [, access_mode][, buffering])
# 各个参数的细节如下：
# file_name：file_name变量是一个包含了你要访问的文件名称的字符串值。
# access_mode：access_mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
# buffering:如果buffering的值被设为0，就不会有寄存。如果buffering的值取1，访问文件时会寄存行。
# 如果将buffering的值设为大于1的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。
# 最简单的用法：以只读方式打开文件
# 最简单的用法：以只读方式打开文件
""" file = open("py05.py")  # 默认是只读模式 (r)
# # 或
# file = open("test.txt", "r")

# 读取内容
content = file.read()
print(content)

# 关闭文件
file.close()
 """
import os


file = open("py05.py", "r", encoding="utf-8")
content = file.read()
print(content)
file.close()


""" 模式	描述
t	文本模式 (默认)。
x	写模式，新建一个文件，如果该文件已存在则会报错。
b	二进制模式。
+	打开一个文件进行更新(可读可写)。
U	通用换行模式（不推荐）。
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
r+	打开一个文件用于读写。文件指针将会放在文件的开头。
rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。
w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。 """



# File对象的属性
# file.closed	返回true如果文件已被关闭，否则返回false。
# file.mode	返回被打开文件的访问模式。
# file.name	返回文件的名称。
# file.softspace	如果用print输出后，必须跟一个空格符，则返回false。否则返回true。
# fo = open("data/py05.txt", "w")  # 子目录  需要写路径
# 打开一个文件
fo = open("py05.txt", "w")
print("文件名: ", fo.name)
print("是否已关闭 : ", fo.closed)
print("访问模式 : ", fo.mode)

# close()方法
# File 对象的 close（）方法刷新缓冲区里任何还没写入的信息，并关闭该文件，这之后便不能再进行写入。
# 当一个文件对象的引用被重新指定给另一个文件时，Python 会关闭之前的文件。用 close（）方法关闭文件是一个很好的习惯。
fo.close()
print("是否已关闭 : ", fo.closed)


# write()方法
# write()方法可将任何字符串写入一个打开的文件。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。
# write()方法不会在字符串的结尾添加换行符('\n')：
# 打开一个文件
fo = open("test.txt", "w")
fo.write( "www.runoob.com!\nVery good site!\n")
 
# 关闭打开的文件
fo.close()

# read()方法
# read（）方法从一个打开的文件中读取一个字符串。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。
# 打开一个文件
fo = open("test.txt", "r+")
str = fo.read(10)
print("读取的字符串是 : ", str)
# 关闭打开的文件
fo.close()

# 文件定位
# tell()方法告诉你文件内的当前位置, 换句话说，下一次的读写会发生在文件开头这么多字节之后。
# seek（offset [,from]）方法改变当前文件的位置。Offset变量表示要移动的字节数。From变量指定开始移动字节的参考位置。
# 如果from被设为0，这意味着将文件的开头作为移动字节的参考位置。如果设为1，则使用当前的位置作为参考位置。如果它被设为2，那么该文件的末尾将作为参考位置。
fo = open("test.txt", "r+")
str = fo.read(10)
print("读取的字符串是 : ", str)
 
# 查找当前位置
position = fo.tell()
print("当前文件位置 : ", position)
 
# 把指针再次重新定位到文件开头
# seek(offset, from)
# offset: 移动多少字节
# from: 从哪开始移动
#   0 = 从文件开头
#   1 = 从当前位置
#   2 = 从文件末尾
position = fo.seek(5, 0)
str = fo.read(15)
print("重新读取字符串 : ", str)
# 关闭打开的文件
fo.close()


# 重命名和删除文件
# rename() 方法
# rename() 方法需要两个参数，当前的文件名和新文件名。
# os.rename("test.txt","test1.txt")

# w 模式：如果文件不存在就创建，存在就覆盖
# fo = open("myfile.txt", "w")
fo = open("myfile.txt", "w", encoding="utf-8")
fo.write("这是文件内容")
fo.close()
print("文件创建成功！")

# remove()方法
# 你可以用remove()方法删除文件，需要提供要删除的文件名作为参数。
""" os.remove("myfile.txt")
 """

# mkdir()方法
# 可以使用os模块的mkdir()方法在当前目录下创建新的目录们。你需要提供一个包含了要创建的目录名称的参数。
""" os.mkdir("newdir") """

# chdir()方法
# 可以用chdir()方法来改变当前的目录。chdir()方法需要的一个参数是你想设成当前目录的目录名称。
# 将当前目录改为"/home/newdir"
""" os.chdir("newdir/")
 """

# getcwd() 方法
# getcwd()方法显示当前的工作目录。
print(os.getcwd())

# rmdir()方法
# rmdir()方法删除目录，目录名称以参数传递。
# 在删除这个目录之前，它的所有内容应该先被清除。
""" os.rmdir("newdir") """


# open() 方法
# Python open() 方法用于打开一个文件，并返回文件对象，在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError。
# 注意：使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。
# open() 函数常用形式是接收两个参数：文件名(file)和模式(mode)。
# open(file, mode='r')
# 完整的语法格式为：
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

# 参数说明:
# file: 必需，文件路径（相对或者绝对路径）。
# mode: 可选，文件打开模式
# buffering: 设置缓冲
# encoding: 一般使用utf8
# errors: 报错级别
# newline: 区分换行符
# closefd: 传入的file参数类型
# opener: 设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。

# mode 参数有：
# 模式	描述
# t	文本模式 (默认)。
# x	写模式，新建一个文件，如果该文件已存在则会报错。
# b	二进制模式。
# +	打开一个文件进行更新(可读可写)。
# U	通用换行模式（不推荐）。
# r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
# r+	打开一个文件用于读写。文件指针将会放在文件的开头。
# rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。
# w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
# w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
# a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
# 默认为文本模式，如果要以二进制模式打开，加上 b 。

# file 对象
# file 对象使用 open 函数来创建，下表列出了 file 对象常用的函数：
# 1	file.close()    关闭文件。关闭后文件不能再进行读写操作。
# 2	file.flush()    刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。
# 3	file.fileno()   返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。
# 打开文件
fo = open("test.txt", "w")

# 获取文件描述符
fd = fo.fileno()
print(f"文件描述符: {fd}")

fo.close()

# 4 file.isatty()   如果文件连接到一个终端设备返回 True，否则返回 False。
# 5 file.next()     返回文件下一行。
# Python 3
fo = open("test1.txt", "r")

line = fo.readline()  # 读取第一行
print(f"第一行: {line}")

line = fo.readline()  # 读取第二行
print(f"第二行: {line}")

fo.close()

# 6	file.read([size])   从文件读取指定的字节数，如果未给定或为负则读取所有。
# 7	file.readline([size])   读取整行，包括 "\n" 字符。
fo = open("test1.txt", "r")

line = fo.readline(3) 
print(f"第一行: {line}")
fo.close()


# 8	file.readlines([sizeint])   读取所有行并返回列表，若给定sizeint>0，则是设置一次读多少字节，这是为了减轻读取压力。
fo = open("test1.txt", "r")

line = fo.readlines(3) 
print(f"第一行: {line}")
fo.close()


# 9	file.seek(offset[, whence])     设置文件当前位置
# 10 file.tell()    返回文件当前位置。
fo = open("test1.txt", "r")
tell = fo.tell()
print(tell)
fo.close()

# 11	file.truncate([size])   截取文件，截取的字节通过size指定，默认为当前文件位置。
# 准备一个文件
fo = open("test.txt", "w")
fo.write("0123456789")  # 10个字符
truncate = fo.truncate(5)

# 查看结果
fo = open("test.txt", "r")
result = fo.read()  # 读取内容
print(result)  # "01234"
fo.close()

# ✅ 使用 with 自动管理文件
# with 会自动关闭文件，不需要手动 close()。
# 1. 写入
with open("test.txt", "w") as fo:
    fo.write("0123456789")

# 2. 截断
with open("test.txt", "r+") as fo:
    fo.truncate(5)

# 3. 读取
with open("test.txt", "r") as fo:
    result = fo.read()
    print(result)  # "01234"



# 12	file.write(str) 将字符串写入文件，返回的是写入的字符长度。
# 13	file.writelines(sequence)   向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。
# 准备数据
lines = ["第一行", "第二行", "第三行"]

# ❌ 不换行
with open("test.txt", "w") as fo:
    fo.writelines(lines)

with open("test.txt", "r") as fo:
    print(fo.read())  # "第一行第二行第三行"（都在一行）

# ✅ 加上换行符
lines = ["第一行\n", "第二行\n", "第三行\n"]
with open("test.txt", "w") as fo:
    fo.writelines(lines)

with open("test.txt", "r") as fo:
    print(fo.read())  # "第一行\n第二行\n第三行\n"