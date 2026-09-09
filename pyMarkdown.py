# Python Markdown 生成 HTML
# Markdown 是一种轻量级的标记语言，它允许你使用易读易写的纯文本格式来编写文档，然后将其转换为结构化的 HTML 文档。
# Markdown 的语法简单直观，常用于编写博客、文档、README 文件等。
# 更多 Markdown 内容参考：Markdown 教程
# Python 可以使用 markdown 模块将 Markdown 文本转换为 HTML。

# 将 Markdown 转换为 HTML 的步骤
# 1. 安装 markdown 库
# 首先，我们需要安装 Python 的 markdown 库，可以使用 pip 来安装它：

# pip install markdown

import markdown

# 定义 Markdown 文本
md_text = """
# 这是标题
这是 **加粗** 的文本。
这是 *斜体* 的文本。

- 列表项 1
- 列表项 2

[点击这里](https://www.runoob.com) 访问网站。
"""

# 转换为 HTML
html_output = markdown.markdown(md_text)

# 输出 HTML
print(html_output)



# 读取 Markdown 文件
with open('example.md', 'r', encoding='utf-8') as file:
    markdown_text = file.read()

# 将 Markdown 转换为 HTML
html = markdown.markdown(markdown_text)

# 将 HTML 写入文件
with open('example.html', 'w', encoding='utf-8') as file:
    file.write(html)

print("Markdown 文件已成功转换为 HTML 文件！")


# 代码说明：
# import markdown：这行代码导入了 markdown 库，它提供了将 Markdown 文本转换为 HTML 的功能。
# with open('example.md', 'r', encoding='utf-8') as file:
#     markdown_text = file.read()
# 这段代码使用 open 函数打开 example.md 文件，并读取其内容到 markdown_text 变量中。
# html = markdown.markdown(markdown_text) ：这行代码使用 markdown.markdown() 函数将 Markdown 文本转换为 HTML 文本。
# with open('example.html', 'w', encoding='utf-8') as file:
#     file.write(html)
# 这段代码将转换后的 HTML 文本写入 example.html 文件中。


# 扩展功能
# markdown 库支持多种扩展，例如表格、代码高亮等。你可以通过以下方式启用扩展：
# html = markdown.markdown(markdown_text, extensions=['tables', 'fenced_code'])