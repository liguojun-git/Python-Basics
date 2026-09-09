# 客户端
# 接下来我们写一个简单的客户端实例连接到以上创建的服务。端口号为 9999。
# socket.connect(hostname, port ) 方法打开一个 TCP 连接到主机为 hostname 端口为 port 的服务商。连接后我们就可以从服务端获取数据，记住，操作完成后需要关闭连接。

# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# 获取本地主机名
host = socket.gethostname() 

# 设置端口号
port = 9999

# 连接服务，指定主机和端口
s.connect((host, port))

# recv() - 从网络缓冲区读取数据到内存
# 接收小于 1024 字节的数据
msg = s.recv(1024)

s.close()

print (msg.decode('utf-8'))


# python Internet 模块
# 以下列出了 Python 网络编程的一些重要模块：

# 协议	    功能用处	                        端口号	        Python 模块
# HTTP	    网页访问	                        80	            httplib, urllib, xmlrpclib
# NNTP	    阅读和张贴新闻文章，俗称为"帖子"	  119	          nntplib
# FTP	    文件传输	                        20	            ftplib, urllib
# SMTP	    发送邮件	                        25	            smtplib
# POP3	    接收邮件	                        110	            poplib
# IMAP4	    获取邮件	                        143	            imaplib
# Telnet	命令行	                            23	            telnetlib
# Gopher	信息查找	                        70	            gopherlib, urllib