# Python 量化
# Python 量化是指利用 Python 编程语言以及相关的库和工具来进行金融市场数据分析、策略开发和交易执行的过程。
# Python 由于其简洁、易学、强大的生态系统和丰富的金融库而成为量化交易的首选编程语言之一。
# 量化交易在金融领域得到广泛应用，它允许交易者通过系统性的方法来制定和执行交易策略，提高交易效率和决策的科学性。
# 量化主要是通过数学和统计学的方法，利用计算机技术对金融市场进行量化分析，从而制定和执行交易策略。


# 实例应用
# 接下来我们先看一个 Python 量化简单的应用实例，可以使用移动平均策略，使用雅虎金融数据来实现。
# 该策略的基本思想是通过比较短期和长期移动平均线来生成买入和卖出信号。
# 在进行这个简单实例前，需要先安装三个包：
# pip install pandas yfinance matplotlib
# 包说明：
# Pandas 是一个功能强大的开源数据处理和分析库，专门设计用于高效地进行数据分析和操作。
# yfinance 是一个用于获取金融数据的库，支持从 Yahoo Finance 获取股票、指数和其他金融市场数据。
# Matplotlib 是一个二维绘图库，用于创建静态、动态和交互式的数据可视化图表。


import yfinance as yf

# 获取股票数据
# 600519 是贵州茅台的股票代码（A股）
# .SS 表示上海证券交易所（Shanghai Stock Exchange）
# .SZ 表示深圳证券交易所（Shenzhen）
symbol = "600519.SS"
start_date = "2022-01-01"
end_date = "2023-01-01"

data = yf.download(symbol, start=start_date, end=end_date)
print(data.head())
# Open	开盘价（当天第一笔交易价格）
# High	最高价（当天最高价格）
# Low	最低价（当天最低价格）
# Close	收盘价（当天最后一笔交易价格）
# Adj Close	调整收盘价（考虑分红、拆股等因素后的价格）
# Volume	成交量（当天成交的股票数量）


# 简单的数据分析和可视化
# 使用 pandas 进行数据分析和 matplotlib 进行可视化：

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 获取股票数据
symbol = "600519.SS"
start_date = "2022-01-01"
end_date = "2023-01-01"

data = yf.download(symbol, start=start_date, end=end_date)
# 简单的数据分析
# describe() 会输出数据的统计摘要
print(data.describe())
# 统计量	含义
# count	有效数据个数（多少个交易日）
# mean	平均值
# std	标准差（波动性）
# min	最小值
# 25%	第25百分位数（Q1）
# 50%	第50百分位数（中位数）
# 75%	第75百分位数（Q3）
# max	最大值

# 绘制股价走势图
# 取出收盘价这一列数据; # 画图：图片大小10x6英寸，图例标签用股票代码
data['Close'].plot(figsize=(10, 6), label=symbol)
plt.title(f"{symbol} Stock Price")  # 图表标题：显示股票代码
plt.xlabel("Date")                   # X轴标签：日期
plt.ylabel("Price")                  # Y轴标签：价格
plt.legend()                         # 显示图例
plt.show()                           # 显示图片

# 移动平均交叉策略回测
# 回测是在历史市场数据上模拟和评估一个交易策略的过程。
# 以下是一个简单的移动平均交叉策略回测的实例代码，策略是在 50 日均线上穿越 200 日均线时买入，下穿越时卖出，策略的表现输出了总收益、年化收益和最大回撤等指标。
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 获取股票数据
symbol = "600519.SS"
start_date = "2021-01-01"
end_date = "2023-01-01"

data = yf.download(symbol, start=start_date, end=end_date)

# 计算移动平均
# 计算50日简单移动平均线（SMA_50）
# 含义：过去50个交易日收盘价的平均值  代表短期趋势
data['SMA_50'] = data['Close'].rolling(window=50).mean()

# 计算200日简单移动平均线（SMA_200）
# 含义：过去200个交易日收盘价的平均值
# 代表长期趋势
data['SMA_200'] = data['Close'].rolling(window=200).mean()
# 当短期均线 上穿 长期均线时 → 金叉（买入信号） → 看涨
# 当短期均线 下穿 长期均线时 → 死叉（卖出信号） → 看跌


# 初始化交叉信号列
# 创建一列 Signal，初始值全为 0
# Signal 的含义：
# 1 = 买入（持有多头仓位）
# -1 = 卖出（空仓或做空）
# 0 = 中性（不操作）
data['Signal'] = 0

# 计算交叉信号
# 第1行：当 50日均线 > 200日均线（金叉）时，Signal = 1（买入持仓）
# 第2行：当 50日均线 < 200日均线（死叉）时，Signal = -1（卖出/空仓）
data.loc[data['SMA_50'] > data['SMA_200'], 'Signal'] = 1
data.loc[data['SMA_50'] < data['SMA_200'], 'Signal'] = -1

# 计算每日收益率
data['Daily_Return'] = data['Close'].pct_change()
# pct_change()：计算每个交易日相对于前一个交易日的收益率（百分比变化）
# 公式：(今日收盘价 - 昨日收盘价) / 昨日收盘价

# 计算策略信号的收益率（shift(1) 是为了避免未来数据的偏差）
# data['Signal'].shift(1)：将信号向后移一天
# 原因：避免未来数据偏差（Look-ahead Bias）
# 今天的信号，只能明天开盘时执行，不能今天就赚到今天的收益
# shift(1) 的意思是：用昨天的信号乘以今天的收益率
# signal * Daily_Return：
# 如果信号为 1（买入）：策略收益 = 当日收益率（赚了跟股票一样，亏了也一样）
# 如果信号为 -1（卖出）：策略收益 = -当日收益率（做空，股票跌了反而赚钱）
# 如果信号为 0（中性）：策略收益 = 0（空仓，不赚不亏）
data['Strategy_Return'] = data['Signal'].shift(1) * data['Daily_Return']

# 计算累计收益
data['Cumulative_Return'] = (1 + data['Strategy_Return']).cumprod()

# 输出策略表现
# 指标1：总收益率
# python
# 'Total Return': data['Cumulative_Return'].iloc[-1] - 1
# iloc[-1]：取最后一个值（最终净值）
# 减去 1 得到总收益率
# 例如：净值从 1 变成 1.25 → 总收益 25%
# 指标2：年化收益率
# python
# 'Annualized Return': (data['Cumulative_Return'].iloc[-1] ** (252 / len(data))) - 1
# 252 / len(data)：252 个交易日/年，按比例折算
# 公式：(最终净值) ^ (252 / 总天数) - 1
# 例如：1.25 ^ (252/500) - 1 ≈ 11.8%（年化收益）
# 指标3：最大回撤（Max Drawdown）
# python
# 'Max Drawdown': (data['Cumulative_Return'] / data['Cumulative_Return'].cummax() - 1).min()
# cummax()：累计最大值（历史最高净值）
# 净值 / 历史最高 - 1：当前从最高点下跌了多少
# .min()：取最差的情况（最大回撤）
strategy_performance = {
    'Total Return': data['Cumulative_Return'].iloc[-1] - 1,
    'Annualized Return': (data['Cumulative_Return'].iloc[-1] ** (252 / len(data))) - 1,
    'Max Drawdown': (data['Cumulative_Return'] / data['Cumulative_Return'].cummax() - 1).min(),
}
# 净值: 1.0 → 1.2 → 1.1 → 1.5 → 1.3
# 历史最高: 1.0 → 1.2 → 1.2 → 1.5 → 1.5
# 回撤:  0% → 0% → -8.3% → 0% → -13.3%
# 最大回撤 = -13.3%（从1.5跌到1.3）


print("策略表现:")
for key, value in strategy_performance.items():
    print(f"{key}: {value:.4f}")

# 绘制累计收益曲线
# plt.figure(figsize=(10, 6))	创建图片，大小 10×6 英寸
# plt.plot(..., color='b')	画蓝色线：策略的累计收益
# plt.plot(data['Close'] / data['Close'].iloc[0], color='g')	画绿色线：单纯持有股票的累计收益
# data['Close'] / data['Close'].iloc[0]	将股价归一化（从1开始），便于和策略对比
# plt.title(...)	标题
# plt.legend()	显示图例
# plt.show()	显示图表
plt.figure(figsize=(10, 6))
plt.plot(data['Cumulative_Return'], label='Strategy Cumulative Return', color='b')
plt.plot(data['Close'] / data['Close'].iloc[0], label='Stock Cumulative Return', color='g')
plt.title("Cumulative Return of Strategy vs. Stock")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.legend()
plt.show()
