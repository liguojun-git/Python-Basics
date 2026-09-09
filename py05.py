import calendar
import os
import time  # 引入time模块
 
# 时间戳（Timestamp） 是指从 1970年1月1日 00:00:00 UTC（Unix纪元）开始，到指定时间点所经过的秒数（包括小数部分）。
# 1970年1月1日被称为 Unix 纪元（Unix Epoch），这是计算机领域的一个重要时间起点。
ticks = time.time()
print("当前时间戳为:", ticks)

# 获取当前时间
localtime = time.localtime(time.time())
print("本地时间为 :", localtime)

# 获取格式化的时间
localtime = time.asctime( time.localtime(time.time()) )
print("本地时间为 :", localtime)

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) 
 
# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00-59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身

cal = calendar.month(2016, 1)
print("以下输出2016年1月份的日历:")
print(cal)

# Time 模块
# 1	time.altzone    返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。
# 2	time.asctime([tupletime])   接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
# 基本示例：将时间元组转换为可读字符串
t = (2026, 8, 5, 13, 49, 58, 2, 217, 0)  # 时间元组
result = time.asctime(t)
print(result)  # 输出: Wed Aug  5 13:49:58 2026

# 3	time.clock( )   用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。
# Python 3
start = time.perf_counter()

# 执行需要计时的代码
total = sum(range(1000000))

end = time.perf_counter()
print(f"耗时: {end - start:.6f} 秒")
print(f"耗时: {(end - start) * 1000:.3f} 毫秒")


# 4	time.ctime([secs])      作用相当于asctime(localtime(secs))，未给参数相当于asctime()

# 基本示例：将时间戳转换为可读字符串
timestamp = 1785916198
result = time.ctime(timestamp)
print(result)  # 输出: Wed Aug  5 13:49:58 2026

# 无参数时使用当前时间
current = time.ctime()
print(current)  

# 5	time.gmtime([secs])     接收时间戳（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0
timestamp = 1785916198
result = time.gmtime(timestamp)
print(result)  
# 输出: time.struct_time(tm_year=2026, tm_mon=8, tm_mday=5, 
#        tm_hour=5, tm_min=49, tm_sec=58, tm_wday=2, tm_yday=217, tm_isdst=0)


# 6	time.localtime([secs])      接收时间戳（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）。
timestamp = 1785916198
result = time.localtime(timestamp)
print(result)  
# 输出: time.struct_time(tm_year=2026, tm_mon=8, tm_mday=5, 
#        tm_hour=13, tm_min=49, tm_sec=58, tm_wday=2, tm_yday=217, tm_isdst=0)


# 7	time.mktime(tupletime)      接受时间元组并返回时间戳（1970纪元后经过的浮点秒数）。
# 基本示例：将时间元组转换为时间戳
t = (2026, 8, 5, 7, 49, 58, 2, 217, 0)
#   年  月  日 时 分 秒 周几 第几天 夏令时

timestamp = time.mktime(t)
print(timestamp)  # 输出: 1785916198.0

# 8	time.sleep(secs)    推迟调用线程的运行，secs指秒数。
# 9	time.strftime(fmt[,tupletime])      接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。
# 基本示例：将时间元组格式化为字符串
t = (2026, 8, 6, 10, 10, 0, 3, 218, 0)
#   年  月  日 时 分 秒 周几 第几天 夏令时

result = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(result)  # 输出: 2026-08-06 10:10:00

# 10	time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')   根据fmt的格式把一个时间字符串解析为时间元组。
# 基本示例：将时间字符串解析为时间元组
time_str = "2026-08-06 10:10:00"
result = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
print(result)  
# 输出: time.struct_time(tm_year=2026, tm_mon=8, tm_mday=6, 
#        tm_hour=10, tm_min=10, tm_sec=0, tm_wday=3, tm_yday=218, tm_isdst=-1)


# 11	time.time( )    返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
# 12	time.tzset()    根据环境变量TZ重新初始化时间相关设置。
# time.tzset() 是 Unix/Linux 系统的专属功能，Windows 上不支持。

# 1	time.timezone   属性 time.timezone 是当地时区（未启动夏令时）距离格林威治的偏移秒数（>0，美洲<=0大部分欧洲，亚洲，非洲）。
# 获取本地时区偏移（秒）
offset_seconds = time.timezone
print(f"时区偏移（秒）: {offset_seconds}")
print(f"时区偏移（小时）: {offset_seconds / 3600}")

# 2	time.tzname     属性time.tzname包含一对根据情况的不同而不同的字符串，分别是带夏令时的本地时区名称，和不带的。
# 获取时区名称
tz_names = time.tzname
print(tz_names)  # 输出: ('CST', 'CDT') 或类似
print(f"标准时区名称: {tz_names[0]}")
print(f"夏令时时区名称: {tz_names[1]}")


# 1	calendar.calendar(year,w=2,l=1,c=6)     返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。
print(calendar.calendar(2026,w=2,l=1,c=6))

# 2	calendar.firstweekday( )        返回当前每周起始日期的设置。默认情况下，首次载入 calendar 模块时返回 0，即星期一。
# 获取当前每周起始日期的设置
first_day = calendar.firstweekday()
print(first_day)  # 输出: 0 (0 代表星期一)
print(f"每周起始日: {calendar.day_name[first_day]}")  # Monday
# '中国': 0,    # 星期一
# '美国': 6,    # 星期日
# '英国': 0,    # 星期一
# '日本': 0,    # 星期一
# '以色列': 6,  # 星期日
# '印度': 0,    # 星期一
# '德国': 0,    # 星期一
# '加拿大': 6,  # 星期日

# 3	calendar.isleap(year)       是闰年返回 True，否则为 False。
print(calendar.isleap(2026))
print(calendar.isleap(2000))


# 4	calendar.leapdays(y1,y2)        返回在Y1，Y2两年之间的闰年总数。
print(calendar.leapdays(2000,2026))


# 5	calendar.month(year,month,w=2,l=1)      返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。
print(calendar.month(2026,8,2,1))

# 6	calendar.monthcalendar(year,month)      返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
result = calendar.monthcalendar(2026, 8)
print(result)

# 7	calendar.monthrange(year,month)     返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。日从0（星期一）到6（星期日）;月从1到12。
result = calendar.monthrange(2026, 8)
print(result)  # 输出: (5, 31)
# 第一个值: 5 (表示8月1日是星期六, 0=周一, 5=周六)
# 第二个值: 31 (表示8月有31天)


# 8	calendar.prcal(year,w=2,l=1,c=6)        相当于 print calendar.calendar(year,w=2,l=1,c=6)。
calendar.prcal(2026)

# 9	calendar.prmonth(year,month,w=2,l=1)        相当于 print calendar.month(year,month,w=2,l=1) 。
calendar.prmonth(2026,6,2,1)

# 10	calendar.setfirstweekday(weekday)       设置每周的起始日期码。0（星期一）到6（星期日）。
# 查看当前设置
print(f"当前起始日: {calendar.firstweekday()} ({calendar.day_name[calendar.firstweekday()]})")

# 设置为星期日（美国标准）
calendar.setfirstweekday(6)  # 6 = 星期日
print(f"修改后起始日: {calendar.firstweekday()} ({calendar.day_name[calendar.firstweekday()]})")

# 恢复为星期一（中国标准）
calendar.setfirstweekday(0)  # 0 = 星期一
print(f"恢复后起始日: {calendar.firstweekday()} ({calendar.day_name[calendar.firstweekday()]})")


# 11	calendar.timegm(tupletime)      和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间戳（1970纪元后经过的浮点秒数）。
# 将 UTC 时间元组转换为时间戳
utc_tuple = (2026, 8, 6, 10, 10, 0)  # 年,月,日,时,分,秒
timestamp = calendar.timegm(utc_tuple)
print(timestamp)  # 输出: 1785916200.0

# 12	calendar.weekday(year,month,day)    返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。
print(calendar.weekday(2026,8,6))