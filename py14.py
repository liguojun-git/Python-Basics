# Python2.x 版本中，使用 cmp() 函数来比较两个列表、数字或字符串等的大小关系。
# Python 3.X 的版本中已经没有 cmp() 函数，如果你需要实现比较功能，需要引入 operator 模块，适合任何对象，包含的方法有：
import operator


# 数字
x = 10
y = 20

print("x:",x, ", y:",y)
print("operator.lt(x,y): ", operator.lt(x,y))
print("operator.gt(y,x): ", operator.gt(y,x))
print("operator.eq(x,x): ", operator.eq(x,x))
print("operator.ne(y,y): ", operator.ne(y,y))
print("operator.le(x,y): ", operator.le(x,y))
print("operator.ge(y,x): ", operator.ge(y,x))
print()

# 字符串
x = "Google"
y = "Runoob"

print("x:",x, ", y:",y)
print("operator.lt(x,y): ", operator.lt(x,y))
print("operator.gt(y,x): ", operator.gt(y,x))
print("operator.eq(x,x): ", operator.eq(x,x))
print("operator.ne(y,y): ", operator.ne(y,y))
print("operator.le(x,y): ", operator.le(x,y))
print("operator.ge(y,x): ", operator.ge(y,x))
print()

# 查看返回值
print("type((operator.lt(x,y)): ", type(operator.lt(x,y)))

a = [1, 2]
b = [2, 3]
c = [2, 3]
print("operator.eq(a,b): ", operator.eq(a,b))
print("operator.eq(c,b): ", operator.eq(c,b))

# 初始化变量
a = 4
b = 3
 
# 使用 add() 让两个值相加
print ("add() 运算结果 :",end="");
print (operator.add(a, b))
 
# 使用 sub() 让两个值相减
print ("sub() 运算结果 :",end="");
print (operator.sub(a, b))
 
# 使用 mul() 让两个值相乘
print ("mul() 运算结果 :",end="");
print (operator.mul(a, b))

# /   → 真除法（浮点数除法）
# //  → 地板除法（向下取整除法）

# 运算              语法            函数
# 加法              a + b           add(a, b)
# 字符串拼接        seq1 + seq2     concat(seq1, seq2)
# 包含测试          obj in seq      contains(seq, obj)
# 除法              a / b           truediv(a, b)
# 除法              a // b          floordiv(a, b)
# 按位与            a & b           and_(a, b)
# 按位异或          a ^ b           xor(a, b)
# 按位取反          ~ a             invert(a)
# 按位或            a | b           or_(a, b)
# 取幂              a ** b          pow(a, b)
# 标识              a is b          is_(a, b)
# 标识              a is not b      is_not(a, b)
# 索引赋值          obj[k] = v      setitem(obj, k, v)
# 索引删除          del obj[k]      delitem(obj, k)
# 索引取值          obj[k]          getitem(obj, k)
# 左移              a << b          lshift(a, b)
# 取模              a % b           mod(a, b)
# 乘法              a * b           mul(a, b)
# 矩阵乘法          a @ b           matmul(a, b)
# 取反（算术）      - a             neg(a)
# 取反（逻辑）      not a           not_(a)
# 正数              + a             pos(a)
# 右移              a >> b          rshift(a, b)
# 切片赋值          seq[i:j] = v    setitem(seq, slice(i, j), v)
# 切片删除          del seq[i:j]    delitem(seq, slice(i, j))
# 切片取值          seq[i:j]        getitem(seq, slice(i, j))
# 字符串格式化      s % obj         mod(s, obj)
# 减法              a - b           sub(a, b)
# 真值测试          obj             truth(obj)
# 比较（小于）      a < b           lt(a, b)
# 比较（小于等于）  a <= b          le(a, b)
# 比较（等于）      a == b          eq(a, b)
# 比较（不等于）    a != b          ne(a, b)
# 比较（大于等于）  a >= b          ge(a, b)
# 比较（大于）      a > b           gt(a, b)




import random
# 生成随机数
print(random.random())
random.seed()
print ("使用默认种子生成随机数：", random.random())
print ("使用默认种子生成随机数：", random.random())

random.seed(10)
print ("使用整数 10 种子生成随机数：", random.random())
random.seed(10)
print ("使用整数 10 种子生成随机数：", random.random())

random.seed("hello",2)
print ("使用字符串种子生成随机数：", random.random())



# 方法	描述
# seed()	初始化随机数生成器
# getstate()	返回捕获生成器当前内部状态的对象。
# setstate()	state 应该是从之前调用 getstate() 获得的，并且 setstate() 将生成器的内部状态恢复到 getstate() 被调用时的状态。
# getrandbits(k)	返回具有 k 个随机比特位的非负 Python 整数。 此方法随 MersenneTwister 生成器一起提供，其他一些生成器也可能将其作为 API 的可选部分提供。 在可能的情况下，getrandbits() 会启用 randrange() 来处理任意大的区间。
# randrange()	从 range(start, stop, step) 返回一个随机选择的元素。
# randint(a, b)	返回随机整数 N 满足 a <= N <= b。
# choice(seq)	从非空序列 seq 返回一个随机元素。 如果 seq 为空，则引发 IndexError。
# choices(population, weights=None, *, cum_weights=None, k=1)	从 population 中选择替换，返回大小为 k 的元素列表。 如果 population 为空，则引发 IndexError。
# shuffle(x[, random])	将序列 x 随机打乱位置。
# sample(population, k, *, counts=None)	返回从总体序列或集合中选择的唯一元素的 k 长度列表。 用于无重复的随机抽样。
# random()	返回 [0.0, 1.0) 范围内的下一个随机浮点数。
# uniform()	返回一个随机浮点数 N ，当 a <= b 时 a <= N <= b ，当 b < a 时 b <= N <= a 。
# triangular(low, high, mode)	返回一个随机浮点数 N ，使得 low <= N <= high 并在这些边界之间使用指定的 mode 。 low 和 high 边界默认为零和一。 mode 参数默认为边界之间的中点，给出对称分布。
# betavariate(alpha, beta)	Beta 分布。 参数的条件是 alpha > 0 和 beta > 0。 返回值的范围介于 0 和 1 之间。
# expovariate(lambd)	指数分布。 lambd 是 1.0 除以所需的平均值，它应该是非零的。
# gammavariate()	Gamma 分布（ 不是伽马函数） 参数的条件是 alpha > 0 和 beta > 0。
# gauss(mu, sigma)	正态分布，也称高斯分布。 mu 为平均值，而 sigma 为标准差。 此函数要稍快于下面所定义的 normalvariate() 函数。
# lognormvariate(mu, sigma)	对数正态分布。 如果你采用这个分布的自然对数，你将得到一个正态分布，平均值为 mu 和标准差为 sigma 。 mu 可以是任何值，sigma 必须大于零。
# normalvariate(mu, sigma)	正态分布。 mu 是平均值，sigma 是标准差。
# vonmisesvariate(mu, kappa)	冯·米塞斯分布。 mu 是平均角度，以弧度表示，介于0和 2*pi 之间，kappa 是浓度参数，必须大于或等于零。 如果 kappa 等于零，则该分布在 0 到 2*pi 的范围内减小到均匀的随机角度。
# paretovariate(alpha)	帕累托分布。 alpha 是形状参数。
# weibullvariate(alpha, beta)	威布尔分布。 alpha 是比例参数，beta 是形状参数。