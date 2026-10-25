import requests
from bs4 import BeautifulSoup

def crawl_static_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        resp.encoding = resp.apparent_encoding
        soup = BeautifulSoup(resp.text, "html.parser")

        # 提取页面标题
        title = soup.find("title").get_text(strip=True)
        print(f"页面标题：{title}")
        print("-" * 50)

        # 提取所有超链接
        a_list = soup.find_all("a")
        link_result = []
        for a in a_list:
            link_text = a.get_text(strip=True)
            href = a.get("href")
            if link_text and href:
                link_result.append({"text": link_text, "url": href})

        # 打印结果
        for item in link_result:
            print(f"文字：{item['text']}  | 链接：{item['url']}")
        return link_result

    except Exception as e:
        print(f"请求出错：{e}")
        return None

if __name__ == "__main__":
    # 示例：可以换成任意公开静态页面，推荐用静态测试站
    target_url = "https://example.com"
    crawl_static_page(target_url)
