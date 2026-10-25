simple-static-crawler
Python实现简易静态网页爬虫，使用requests发起HTTP请求，BeautifulSoup4解析HTML，提取页面标题与超链接信息。

功能清单
- 自定义请求头模拟浏览器访问
- 获取静态网页HTML源码
- 解析提取页面标题、所有超链接文本与地址
- 异常捕获，处理请求超时、访问失败

技术栈
Python3，requests、BeautifulSoup4
```bash
pip install -r requirements.txt

运行方式
python crawler.py
可修改代码内 target_url，采集其他公开静态页面。

项目结构
├── crawler.py          # 爬虫主程序
├── requirements.txt    # 依赖声明
├── README.md
