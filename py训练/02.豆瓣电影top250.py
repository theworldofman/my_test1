import csv, re, time, requests
from lxml import html

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://movie.douban.com/top250",
    "Cookie": "bid=BlKhHwx939A; ct=y",
}

def safe_first(lst, default=""):
    return lst[0].strip() if lst else default

def get_movie(doc):
    name   = safe_first(doc.xpath('//*[@id="content"]/h1/span[1]/text()'))
    time_  = safe_first(doc.xpath('//*[@id="content"]/h1/span[2]/text()'))
    rating = safe_first(doc.xpath('//strong[@class="ll rating_num"]/text()'))
    genres = doc.xpath('//span[@property="v:genre"]/text()')
    runtime= safe_first(doc.xpath('//span[@property="v:runtime"]/text()'))
    summary= safe_first(doc.xpath('//span[@property="v:summary"]/text()'))
    director = safe_first(doc.xpath('//a[@rel="v:directedBy"]/text()'))

    m = re.search(r"\d{4}", time_)
    return {
        "电影名称": name,
        "上映时间": m.group() if m else "",
        "导演": director,
        "评分": rating,
        "类型": "/".join(genres),
        "时长": runtime,
        "简介": summary,
    }

movie_list = []
for page_num in range(1, 2):
    start = (page_num - 1) * 25
    print(f"第 {page_num} 页 ...")
    r = requests.get(f"https://movie.douban.com/top250?start={start}&filter=",
                     headers=headers, timeout=10)
    doc = html.fromstring(r.text)

    # ⚠️ 注意这里：@class 没空格
    items = doc.xpath("//ol[@class='grid_view']/li")
    print(f"  找到 {len(items)} 部电影")

    for it in items:
        href = it.xpath('.//div[@class="pic"]//a/@href')
        if not href:
            continue
        detail = html.fromstring(requests.get(href[0], headers=headers, timeout=10).text)
        movie_list.append(get_movie(detail))
        time.sleep(2)

with open("豆瓣top.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=["电影名称","上映时间","导演","评分","类型","时长","简介"])
    writer.writeheader()
    writer.writerows(movie_list)








