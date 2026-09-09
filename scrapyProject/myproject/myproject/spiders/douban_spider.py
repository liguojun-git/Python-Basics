import scrapy


class DoubanSpiderSpider(scrapy.Spider):

# 代码说明：
# name：定义爬虫的名称，必须是唯一的。
# allowed_domains：限制爬虫的访问域名，防止爬虫爬取其他域名的网页。
# start_urls：定义爬虫的起始页面，爬虫将从这些页面开始抓取。
# parse：parse 方法是每个爬虫的核心部分，用于处理响应并提取数据。它接收一个 response 对象，表示服务器返回的页面内容。
    name = "douban_spider"
    allowed_domains = ["movie.douban.com"]
    start_urls = [
        'https://movie.douban.com/top250',
    ]

    # ===== 3. 自定义请求头（伪装浏览器） =====
    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Referer': 'https://movie.douban.com/',
        }
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers, callback=self.parse)

    # ===== 4. 解析页面 =====
    def parse(self, response):
        for movie in response.css('div.item'):
            # yield 的作用：
            # yield 不是 return。它不会结束函数，而是产生一个数据并继续执行
            # 每循环到一个电影，就 yield 一次，相当于一边爬一边输出
            yield {
                'title': movie.css('span.title::text').get(),
                'rating': movie.css('span.rating_num::text').get(),
                'quote': movie.css('span.inq::text').get(),
            }

        # 处理分页
        next_page = response.css('span.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)



# 代码解析：
# name = "douban_spider": 定义爬虫的名称。
# start_urls: 定义爬虫开始爬取的初始 URL（豆瓣电影 Top 250 页面）。
# parse 方法:
# 使用 CSS 选择器提取每部电影的标题、评分和简介。
# span.title::text：提取电影标题。
# span.rating_num::text：提取电影评分。
# span.inq::text：提取电影简介。
# 分页处理:
# 使用 span.next a::attr(href) 提取下一页的链接。
# 如果存在下一页，使用 response.follow 继续爬取。
    



