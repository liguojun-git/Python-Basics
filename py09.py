# Python 异常处理
# BaseException	所有异常的基类
# SystemExit	解释器请求退出
# KeyboardInterrupt	用户中断执行(通常是输入^C)
# Exception	常规错误的基类
# StopIteration	迭代器没有更多的值
# GeneratorExit	生成器(generator)发生异常来通知退出
# StandardError	所有的内建标准异常的基类
# ArithmeticError	所有数值计算错误的基类
# FloatingPointError	浮点计算错误
# OverflowError	数值运算超出最大限制
# ZeroDivisionError	除(或取模)零 (所有数据类型)
# AssertionError	断言语句失败
# AttributeError	对象没有这个属性
# EOFError	没有内建输入,到达EOF 标记
# EnvironmentError	操作系统错误的基类
# IOError	输入/输出操作失败
# OSError	操作系统错误
# WindowsError	系统调用失败
# ImportError	导入模块/对象失败
# LookupError	无效数据查询的基类
# IndexError	序列中没有此索引(index)
# KeyError	映射中没有这个键
# MemoryError	内存溢出错误(对于Python 解释器不是致命的)
# NameError	未声明/初始化对象 (没有属性)
# UnboundLocalError	访问未初始化的本地变量
# ReferenceError	弱引用(Weak reference)试图访问已经垃圾回收了的对象
# RuntimeError	一般的运行时错误
# NotImplementedError	尚未实现的方法
# SyntaxError	Python 语法错误
# IndentationError	缩进错误
# TabError	Tab 和空格混用
# SystemError	一般的解释器系统错误
# TypeError	对类型无效的操作
# ValueError	传入无效的参数
# UnicodeError	Unicode 相关的错误
# UnicodeDecodeError	Unicode 解码时的错误
# UnicodeEncodeError	Unicode 编码时错误
# UnicodeTranslateError	Unicode 转换时错误
# Warning	警告的基类
# DeprecationWarning	关于被弃用的特征的警告
# FutureWarning	关于构造将来语义会有改变的警告
# OverflowWarning	旧的关于自动提升为长整型(long)的警告
# PendingDeprecationWarning	关于特性将会被废弃的警告
# RuntimeWarning	可疑的运行时行为(runtime behavior)的警告
# SyntaxWarning	可疑的语法的警告
# UserWarning	用户代码生成的警告


# 异常处理
# 捕捉异常可以使用try/except语句。
# try/except语句用来检测try语句块中的错误，从而让except语句捕获异常信息并处理。
# 如果你不想在异常发生时结束你的程序，只需在try里捕获它。
# try:
# <语句>        #运行别的代码
# except <名字>：
# <语句>        #如果在try部份引发了'name'异常
# except <名字>，<数据>:
# <语句>        #如果引发了'name'异常，获得附加的数据
# else:
# <语句>        #如果没有异常发生
# try的工作原理是，当开始一个try语句后，python就在当前程序的上下文中作标记，这样当异常出现时就可以回到这里，try子句先执行，接下来会发生什么依赖于执行时是否出现异常。
# 如果当try后的语句执行时发生异常，python就跳回到try并执行第一个匹配该异常的except子句，异常处理完毕，控制流就通过整个try语句（除非在处理异常时又引发新的异常）。
# 如果在try后的语句里发生了异常，却没有匹配的except子句，异常将被递交到上层的try，或者到程序的最上层（这样将结束程序，并打印默认的出错信息）。
# 如果在try子句执行时没有发生异常，python将执行else语句后的语句（如果有else的话），然后控制流通过整个try语句。
# 下面是简单的例子，它打开一个文件，在该文件中的内容写入内容，且并未发生异常：

try:
    fh = open("testfile", "w",encoding="utf-8")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()

try:
    # 不设置utf-8
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except Exception:
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()


# 使用except而带多种异常类型
# 你也可以使用相同的except语句来处理多个异常信息，如下所示：

# try:
#     正常的操作
#    ......................
# except(Exception1[, Exception2[,...ExceptionN]]):
#    发生以上多个异常中的一个，执行这块代码
#    ......................
# else:
#     如果没有异常执行这块代码


try:
    # 不设置utf-8
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except Exception:
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()
finally:
    print("我是finally")


# Python OS 文件/目录方法
# os 模块提供了非常丰富的方法用来处理文件和目录。常用的方法如下表所示：
# 1	os.access(path, mode)   检验权限模式
# 2	os.chdir(path)  改变当前工作目录
# 3	os.chflags(path, flags)     设置路径的标记为数字标记。
# 4	os.chmod(path, mode)    更改权限
# 5	os.chown(path, uid, gid)    更改文件所有者
# 6	os.chroot(path)     改变当前进程的根目录
# 7	os.close(fd)    关闭文件描述符 fd
# 8	os.closerange(fd_low, fd_high)  关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略
# 9	os.dup(fd)  复制文件描述符 fd
# 10	os.dup2(fd, fd2)    将一个文件描述符 fd 复制到另一个 fd2
# 11	os.fchdir(fd)   通过文件描述符改变当前工作目录
# 12	os.fchmod(fd, mode)     改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。
# 13	os.fchown(fd, uid, gid)     修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。
# 14	os.fdatasync(fd)    强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。
# 15	os.fdopen(fd[, mode[, bufsize]])    通过文件描述符 fd 创建一个文件对象，并返回这个文件对象
# 16	os.fpathconf(fd, name)  返回一个打开的文件的系统配置信息。name为检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。
# 17	os.fstat(fd)    返回文件描述符fd的状态，像stat()。
# 18	os.fstatvfs(fd)     返回包含文件描述符fd的文件的文件系统的信息，像 statvfs()
# 19	os.fsync(fd)    强制将文件描述符为fd的文件写入硬盘。
# 20	os.ftruncate(fd, length)    裁剪文件描述符fd对应的文件, 所以它最大不能超过文件大小。
# 21	os.getcwd()     返回当前工作目录
# 22	os.getcwdu()    返回一个当前工作目录的Unicode对象
# 23	os.isatty(fd)   如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。
# 24	os.lchflags(path, flags)    设置路径的标记为数字标记，类似 chflags()，但是没有软链接
# 25	os.lchmod(path, mode)   修改连接文件权限
# 26	os.lchown(path, uid, gid)   更改文件所有者，类似 chown，但是不追踪链接。
# 27	os.link(src, dst)   创建硬链接，名为参数 dst，指向参数 src
# 28	os.listdir(path)    返回path指定的文件夹包含的文件或文件夹的名字的列表。
# 29	os.lseek(fd, pos, how)  设置文件描述符 fd当前位置为pos, how方式修改: SEEK_SET 或者 0 设置从文件开始的计算的pos; SEEK_CUR或者 1 则从当前位置计算; os.SEEK_END或者2则从文件尾部开始. 在unix，Windows中有效
# 30	os.lstat(path)  像stat(),但是没有软链接
# 31	os.major(device)    从原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。
# 32	os.makedev(major, minor)    以major和minor设备号组成一个原始设备号
# 33    os.makedirs(path[, mode])   递归文件夹创建函数。像mkdir(), 但创建的所有intermediate-level文件夹需要包含子文件夹。
# 34	os.minor(device)    从原始的设备号中提取设备minor号码 (使用stat中的st_dev或者st_rdev field )。
# 35	os.mkdir(path[, mode])  以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)。
# 36	os.mkfifo(path[, mode])     创建命名管道，mode 为数字，默认为 0666 (八进制)
# 37	os.mknod(filename[, mode=0600, device])     创建一个名为filename文件系统节点（文件，设备特别文件或者命名pipe）。
# 38    os.open(file, flags[, mode])    打开一个文件，并且设置需要的打开选项，mode参数是可选的
# 39	os.openpty()    打开一个新的伪终端对。返回 pty 和 tty的文件描述符。
# 40	os.pathconf(path, name)     返回相关文件的系统配置信息。
# 41	os.pipe()   创建一个管道. 返回一对文件描述符(r, w) 分别为读和写
# 42	os.popen(command[, mode[, bufsize]])    从一个 command 打开一个管道
# 43	os.read(fd, n)  从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，文件描述符 fd对应文件已达到结尾, 返回一个空字符串。
# 44	os.readlink(path)   返回软链接所指向的文件
# 45	os.remove(path)     删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。
# 46	os.removedirs(path) 递归删除目录。
# 47	os.rename(src, dst) 重命名文件或目录，从 src 到 dst
# 48	os.renames(old, new)    递归地对目录进行更名，也可以对文件进行更名。
# 49	os.rmdir(path)  删除path指定的空目录，如果目录非空，则抛出一个OSError异常。
# 50	os.stat(path)   获取path指定的路径的信息，功能等同于C API中的stat()系统调用。
# 51	os.stat_float_times([newvalue]) 决定stat_result是否以float对象显示时间戳
# 52	os.statvfs(path)    获取指定路径的文件系统统计信息
# 53	os.symlink(src, dst)    创建一个软链接
# 54	os.tcgetpgrp(fd)    返回与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组
# 55	os.tcsetpgrp(fd, pg)    设置与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组为pg。
# 56	os.tempnam([dir[, prefix]])     返回唯一的路径名用于创建临时文件。
# 57	os.tmpfile()    返回一个打开的模式为(w+b)的文件对象 .这文件对象没有文件夹入口，没有文件描述符，将会自动删除。
# 58	os.tmpnam()     为创建一个临时文件返回一个唯一的路径
# 59	os.ttyname(fd)  返回一个字符串，它表示与文件描述符fd 关联的终端设备。如果fd 没有与终端设备关联，则引发一个异常。
# 60	os.unlink(path) 删除文件
# 61	os.utime(path, times)   返回指定的path文件的访问和修改的时间。
# 62	os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])   输出在文件夹中的文件名通过在树中游走，向上或者向下。
# 63	os.write(fd, str)   写入字符串到文件描述符 fd中. 返回实际写入的字符串长度
# 64	os.path 模块    获取文件的属性信息。

# Python 内置函数
# 内置函数		
# abs()	divmod()	input()	open()	staticmethod()
# all()	enumerate()	int()	ord()	str()
# any()	eval()	isinstance()	pow()	sum()
# basestring()	execfile()	issubclass()	print()	super()
# bin()	file()	iter()	property()	tuple()
# bool()	filter()	len()	range()	type()
# bytearray()	float()	list()	raw_input()	unichr()
# callable()	format()	locals()	reduce()	unicode()
# chr()	frozenset()	long()	reload()	vars()
# classmethod()	getattr()	map()	repr()	xrange()
# cmp()	globals()	max()	reverse()	zip()
# compile()	hasattr()	memoryview()	round()	__import__()
# complex()	hash()	min()	set()	
# delattr()	help()	next()	setattr()	
# dict()	hex()	object()	slice()	
# dir()	id()	oct()	sorted()	exec 内置表达式