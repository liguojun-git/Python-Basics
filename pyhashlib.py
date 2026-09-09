# Python hashlib 模块
# Python hashlib 模块主要用于进行哈希（hash）操作。
# 哈希（Hash）是一种将任意长度的输入数据映射为固定长度输出数据的算法。
# 哈希通常用于验证数据的完整性、安全存储密码等场景。
# 哈希函数的输出通常是一串看似随机的字母和数字。
# hashlib 模块提供了常见的哈希算法的实现，如 MD5、SHA-1、SHA-256 等。

# hashlib.new(name, data=None): 创建一个哈希对象。
# name 参数是哈希算法的名称，data 参数是要被哈希的数据。
import hashlib

sha256_hash = hashlib.new('sha256')
sha256_hash.update(b'RUNOOB')
print(sha256_hash.hexdigest())


md5_hash = hashlib.md5(b'RUNOOB')
print(md5_hash.hexdigest())


# 哈希对象方法
# update(data): 更新哈希对象的消息内容。
sha256_hash = hashlib.sha256()
sha256_hash.update(b'Hello, ')
sha256_hash.update(b'Runoob!')
print(sha256_hash.hexdigest())

# hexdigest(): 获取十六进制表示的哈希值。
md5_hash = hashlib.md5(b'RUNOOB')
print(md5_hash.hexdigest())


# digest(): 获取二进制表示的哈希值。
sha1_hash = hashlib.sha1(b'RUNOOB')
print(sha1_hash.digest())


# 常见哈希算法
# MD5
md5_hash = hashlib.md5(b'RUNOOB')
print(md5_hash.hexdigest())

# SHA-1
sha1_hash = hashlib.sha1(b'RUNOOB')
print(sha1_hash.hexdigest())

# SHA-256
sha256_hash = hashlib.sha256(b'RUNOOB')
print(sha256_hash.hexdigest())

# SHA-512
sha512_hash = hashlib.sha512(b'RUNOOB')
print(sha512_hash.hexdigest())


# 在实际应用中，选择合适的哈希算法取决于具体的需求。需要注意的是，MD5 和 SHA-1 已经被认为不安全，特别是在安全领域，推荐使用更强大的算法，如 SHA-256 或 SHA-512。

# Python hashlib 模块中常见的哈希算法及其含义：

# 算法名称	    摘要长度（位）	输出长度（字节）	安全性	        用途
# md5	        128	                16	        不安全	    数据完整性验证、密码存储等
# sha1	        160	                20	        不安全	    数据完整性验证、密码存储等
# sha224	    224	                28	        低	        数据完整性验证、数字签名等
# sha256	    256	                32	        中等	    数据完整性验证、数字签名等
# sha384	    384	                48	        高	        数字签名、加密算法等
# sha512	    512	                64	        高	        数字签名、加密算法等
# sha3_224	    224	                28	        高	        未来标准的 SHA-3 家族成员，适用于数字签名等
# sha3_256	    256	                32	        高	        未来标准的 SHA-3 家族成员，适用于数字签名等
# sha3_384	    384	                48	        高	        未来标准的 SHA-3 家族成员，适用于数字签名等
# sha3_512	    512	                64	        高	        未来标准的 SHA-3 家族成员，适用于数字签名等
# shake_128	    可变	            可变	    高	        SHAKE 系列是 SHA-3 家族的可变长度版本，适用于各种应用
# shake_256	    可变	            可变	    高	        SHAKE 系列是 SHA-3 家族的可变长度版本，适用于各种应用
# 说明：

# 摘要长度（位）： 表示哈希算法输出的摘要长度，以位为单位。
# 输出长度（字节）： 表示哈希算法输出的摘要长度，以字节为单位。
# 安全性： 表示哈希算法的安全性级别，包括 "不安全"、"低"、"中等"、"高"。这是一个一般性的分类，具体的安全性还要考虑算法的用途和具体的攻击场景。


