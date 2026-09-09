# Python statistics 模块
# 在数据分析和科学计算中，统计学是一个非常重要的工具。
# Python 提供了一个内置的 statistics 模块，专门用于处理基本的统计计算。本文将详细介绍 statistics 模块的功能和使用方法，帮助初学者快速掌握如何使用这个模块进行基本的统计分析。
# statistics 模块提供了许多常用的统计函数，如均值、中位数、方差、标准差等。


# 常用的统计函数
# 均值（Mean）
# 均值是数据集中所有数值的平均值。statistics 模块提供了 mean() 函数来计算均值。
import statistics
data = [1, 7, 5, 4, 5]
mean_value = statistics.mean(data)
print("均值:", mean_value)


# 中位数（Median）
# 中位数是将数据集按大小顺序排列后位于中间位置的数值。statistics 模块提供了 median() 函数来计算中位数。
data = [1, 2, 3, 4, 5]
median_value = statistics.median(data)
print("中位数:", median_value)

# 如果数据集的长度为偶数，median() 函数会自动计算中间两个数的平均值。
data = [1, 2, 3, 4]
median_value = statistics.median(data)
print("中位数:", median_value)

# 众数（Mode）
# 众数是数据集中出现频率最高的数值。statistics 模块提供了 mode() 函数来计算众数。
data = [1, 2, 2, 3, 4]
mode_value = statistics.mode(data)
print("众数:", mode_value)

# 方差（Variance）
# 第1步：求平均值，第2步：每个数减去平均值，得到离差，第3步：将每个离差平方，第4步：求平方和，第5步：除以 (n-1) 得到样本方差
# 方差是衡量数据集中数值离散程度的指标。statistics 模块提供了 variance() 函数来计算方差。
data = [1, 2, 3, 4, 5]
variance_value = statistics.variance(data)
print("方差:", variance_value)

# 标准差（Standard Deviation）
# 标准差是方差的平方根，用于衡量数据集的离散程度。statistics 模块提供了 stdev() 函数来计算标准差。
data = [1, 2, 3, 4, 5]
stdev_value = statistics.stdev(data)
print("标准差:", stdev_value)

# 调和平均数（Harmonic Mean）
# 第1步：每个数取倒数，第2步：求倒数的和，第3步：用数据个数 n 除以这个和
# 调和平均数是一种特殊的平均数，适用于计算速率等场景。statistics 模块提供了 harmonic_mean() 函数来计算调和平均数。
data = [1, 2, 4]
harmonic_mean_value = statistics.harmonic_mean(data)
print("调和平均数:", harmonic_mean_value)

# 几何平均数（Geometric Mean）
# 第1步：所有数相乘，第2步：开 n 次方（n = 3）
# 几何平均数是一种用于计算增长率或比例的平均数。statistics 模块提供了 geometric_mean() 函数来计算几何平均数。
data = [1, 2, 4]
geometric_mean_value = statistics.geometric_mean(data)
print("几何平均数:", geometric_mean_value)

# 其他常用函数
# 中位数低（Median Low）和中位数高（Median High）
# statistics 模块还提供了 median_low() 和 median_high() 函数，分别用于计算数据集的中位数低和中位数高。
data = [1, 2, 3, 4]
median_low_value = statistics.median_low(data)
median_high_value = statistics.median_high(data)
print("中位数低:", median_low_value)
print("中位数高:", median_high_value)

# 分位数（Quantiles）
# Q1（第1四分位数） = 中位数左边一半的中位数  左边一半数据：[1, 2]（不包括中位数3本身）
# [1, 2] 的中位数 = (1+2)/2 = 1.5 Q3（第3四分位数） = 中位数右边一半的中位数
# 右边一半数据：[4, 5]    [4, 5] 的中位数 = (4+5)/2 = 4.5
# 分位数是将数据集分成若干等份的数值。statistics 模块提供了 quantiles() 函数来计算分位数。
# index=k × n+1/4

data = [1, 2, 3, 4, 5]
quantiles_value = statistics.quantiles(data, n=4)
print("四分位数:", quantiles_value)