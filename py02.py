import random
import math
# while循环
numbers = [12,45,67,87,88,98]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop()
    print("number:",number)
    if(number % 2 == 0):
      even.append(number)
    else:
      odd.append(number)
print(numbers)
print(even)
print(odd)

count = 0
while count < 5:
   print(count, " is  less than 5")
   count = count + 1
else:
   print(count, " is not less than 5")


# ------------------------------------------------------------------------------------------------
#  for循环
for i in "python":
    print(i)

fruits = ['banana', 'apple',  'mango']
for i in fruits:
   print(i)

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
    #    %s	占位符，表示"这里将来要放一个字符串"
    #    %	格式化运算符，把右边的值填入左边的占位符
    #    fruits[index]	实际的值，会替换掉 %s
   print ('当前水果 : %s' % fruits[index])
 
print ("Good bye!")

for num in range(10,20):  # 迭代 10 到 20 (不包含) 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print ('%d 等于 %d * %d' % (num,i,j))
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print ('%d 是一个质数' % num)


i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print(i, " 是素数")
   i = i + 1
 
print("Good bye!")


""" Python pass 语句
Python pass 是空语句，是为了保持程序结构的完整性。
pass 不做任何事情，一般用做占位语句。
Python 语言 pass 语句语法格式如下： """



# Python数学函数
# 函数	返回值 ( 描述 )
# abs(x)	返回数字的绝对值，如abs(-10) 返回 10
# ceil(x)	返回数字的上入整数，如math.ceil(4.1) 返回 5
# cmp(x, y)	如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
# exp(x)	返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
# fabs(x)	以浮点数形式返回数字的绝对值，如math.fabs(-10) 返回10.0
# floor(x)	返回数字的下舍整数，如math.floor(4.9)返回 4
# log(x)	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
# log10(x)	返回以10为基数的x的对数，如math.log10(100)返回 2.0
# max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
# min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
# modf(x)	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
# pow(x, y)	x**y 运算后的值。
# round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
# sqrt(x)	返回数字x的平方根

# Python随机数函数
# choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
# randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
# random()	随机生成下一个实数，它在[0,1)范围内。
# seed([x])	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
# shuffle(lst)	将序列的所有元素随机排序
# uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。

# 从 0-9 中随机选一个
num = random.choice(range(10))
print(num)   # 可能是 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 中的任意一个

# 从列表中随机选一个
fruits = ['apple', 'banana', 'cherry', 'durian']
fruit = random.choice(fruits)
print(fruit)   # 可能是 apple / banana / cherry / durian

# 从字符串中随机选一个字符
char = random.choice('Hello')
print(char)    # 可能是 H / e / l / o（注意有两个 l，概率更高）

# 从 0 到 9 中随机选一个（step 默认为 1）
num = random.randrange(10)
print(num)   # 0-9 中随机

# 从 5 到 10 中随机选一个（step 默认为 1）
num = random.randrange(5, 10)
print(num)   # 5, 6, 7, 8, 9 中随机

# 从 0 到 100 中选偶数（步长为 2）
num = random.randrange(0, 100, 2)
print(num)   # 0, 2, 4, 6, ... 98 中随机

# 从 1 到 100 中选奇数（步长为 2）
num = random.randrange(1, 100, 2)
print(num)   # 1, 3, 5, 7, ... 99 中随机

# 生成 0-1 之间的随机小数
num = random.random()
print(num)   # 可能是 0.123456789, 0.987654321, 0.0 等

# 通常配合运算生成其他范围的随机数
# 生成 0-10 之间的随机小数
num = random.random() * 10
print(num)   # 0.0 到 9.9999...

# 生成 5-10 之间的随机小数
num = 5 + random.random() * 5
print(num)   # 5.0 到 9.9999...

# 设置种子为 1
""" random.seed(1)
print(random.random())   # 0.13436424411240122
print(random.random())   # 0.8474337369372327

# 重新设置相同的种子，结果完全一样
random.seed(1)
print(random.random())   # 0.13436424411240122 （和上面一样！）
print(random.random())   # 0.8474337369372327 （和上面一样！）

# 不设置种子，每次运行结果都不同
print(random.random())   # 每次都不一样 """


# 打乱列表
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
random.shuffle(cards)
print(cards)   # 每次运行结果不同，比如 ['K', '3', 'A', 'J', ...]

# 数字列表打乱
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(numbers)
print(numbers)   # 比如 [5, 3, 9, 1, 7, 2, 8, 4, 6, 10]

# 注意：shuffle() 直接修改原列表，不会返回新列表！

# result = random.shuffle(numbers)   # ❌ 不要这样写！result 是 None

# 生成 1 到 10 之间的随机小数
num = random.uniform(1, 10)
print(num)   # 比如 3.456789, 7.123456, 9.999999

# 生成 0 到 100 之间的随机小数
score = random.uniform(0, 100)
print(f"随机分数：{score:.2f}")   # 比如 78.56

# 生成 -10 到 10 之间的随机小数
num = random.uniform(-10, 10)
print(num)   # 比如 -3.45, 5.67, 0.12


# Python三角函数
# acos(x)	返回x的反余弦弧度值。
# asin(x)	返回x的反正弦弧度值。
# atan(x)	返回x的反正切弧度值。
# atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
# cos(x)	返回x的弧度的余弦值。
# hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
# sin(x)	返回的x弧度的正弦值。
# tan(x)	返回x弧度的正切值。
# degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
# radians(x)	将角度转换为弧度

x = 0.5
result = math.acos(x)
print(result)              # 1.0471975511965979（弧度）
print(math.degrees(result)) # 60.0（度）
# 返回 x 的反余弦值，结果范围 [0, π]。
# 检查：cos(60°) = 0.5

x = 0.5
result = math.asin(x)
print(result)              # 0.5235987755982989（弧度）
print(math.degrees(result)) # 30.0（度）
# 返回 x 的反正弦值，结果范围 [-π/2, π/2]。
# 检查：sin(30°) = 0.5


x = 1.0
result = math.atan(x)
print(result)              # 0.7853981633974483（弧度）
print(math.degrees(result)) # 45.0（度）
# 返回 x 的反正切值，结果范围 [-π/2, π/2]。
# 检查：tan(45°) = 1.0

# atan2(y, x) —— 根据坐标求反正切
# 返回 y/x 的反正切值，能正确处理象限，结果范围 [-π, π]。
# # 点 (1, 1) 在 45°
x, y = 1, 1
result = math.atan2(y, x)
print(result)              # 0.7853981633974483（弧度）
print(math.degrees(result)) # 45.0（度）

# 点 (-1, 1) 在 135°（atan 无法区分）
x, y = -1, 1
result = math.atan2(y, x)
print(math.degrees(result)) # 135.0（度）

# 点 (-1, -1) 在 -135°（或 225°）
x, y = -1, -1
result = math.atan2(y, x)
print(math.degrees(result)) # -135.0（度）


# 计算 60° 的余弦
angle_rad = math.radians(60)
result = math.cos(angle_rad)
print(result)              # 0.5

# 计算 π 的余弦   math.pi就是π
result = math.cos(math.pi)
print(result)              # -1.0

# 计算 0 的余弦
result = math.cos(0)
print(result)              # 1.0

# hypot(x, y) —— 欧几里得距离
# 两点间的距离
x, y = 3, 1
distance = math.hypot(x, y)
print(distance)            # 5.0（勾股定理 3-4-5）

# 实际应用：计算二维距离
x1, y1 = 1, 1
x2, y2 = 4, 5
dist = math.hypot(x2 - x1, y2 - y1)
print(dist)                # 5.0（从 (1,1) 到 (4,5) 的距离）

# sin(x) —— 正弦
# 计算 30° 的正弦
angle_rad = math.radians(30)
result = math.sin(angle_rad)
print(result)              # 0.5

# 计算 π/2 的正弦（90°）
result = math.sin(math.pi / 2)
print(result)              # 1.0

# 计算 0 的正弦
result = math.sin(0)
print(result)              # 0.0


# tan(x) —— 正切
# 计算 45° 的正切
angle_rad = math.radians(45)
result = math.tan(angle_rad)
print(result)              # 1.0

# 计算 60° 的正切
angle_rad = math.radians(60)
result = math.tan(angle_rad)
print(result)              # 1.7320508075688767（√3）

# 计算 90° 的正切（接近无穷大）
angle_rad = math.radians(90)
result = math.tan(angle_rad)
print(result)              # 1.633123935319537e+16（非常大，但不精确）

# degrees(x) —— 弧度转角度
# π 弧度 = 180°
result = math.degrees(math.pi)
print(result)              # 180.0

# π/2 弧度 = 90°
result = math.degrees(math.pi / 2)
print(result)              # 90.0

# 1 弧度 ≈ 57.3°
result = math.degrees(1)
print(result)              # 57.29577951308232

# radians(x) —— 角度转弧度
# 180° = π 弧度
result = math.radians(180)
print(result)              # 3.141592653589793（π）

# 90° = π/2 弧度
result = math.radians(90)
print(result)              # 1.5707963267948966（π/2）

# 45° = π/4 弧度
result = math.radians(45)
print(result)              # 0.7853981633974483（π/4）

# 弧度 = 角度 × π / 180
# 角度 = 弧度 × 180 / π