# Python selenium 库
# Selenium 是一个用于自动化 Web 浏览器操作的强大工具，广泛应用于 Web 应用程序测试、网页数据抓取和任务自动化等场景。
# Selenium 为各种编程语言提供了 API，用作测试。 目前的官方 API 文档有 C#、JavaScript、Java、Python、Ruby。

# 安装 Selenium 和 WebDriver
# 安装 Selenium
# 要开始使用 Selenium，首先需要安装 selenium 库，并下载适用于你浏览器的 WebDriver。
# 使用 pip 安装 Selenium：
# pip install selenium
# 安装完成后，可以使用以下命令查看 selenium 的版本信息：
# pip show selenium
# 也可以使用 Python 代码查看：
# import selenium
# print(selenium.__version__)

# 下载WebDriver
# Selenium 需要一个 WebDriver 来与浏览器进行交互。

# 不同的浏览器需要不同的 WebDriver，例如 Chrome 浏览器需要 ChromeDriver，你需要根据你使用的浏览器下载相应的 WebDriver，并确保它在你的系统 PATH 中。

# Chrome: ChromeDriver
# Firefox: GeckoDriver
# Edge: EdgeDriver
# Safari: SafariDriver
# 选择浏览器并初始化 WebDriver：

# 实例
# from selenium import webdriver

# 使用 Chrome 浏览器
# driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# 或者使用 Firefox 浏览器
# driver = webdriver.Firefox(executable_path='/path/to/geckodriver')

# 或者使用 Edge 浏览器
# driver = webdriver.Edge(executable_path='/path/to/msedgedriver')