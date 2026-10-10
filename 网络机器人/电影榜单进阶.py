import csv
import requests
import re
from lxml import html

# 0.设计一个函数获得电影信息
def get_movie_info(Ranking):
    # 获得名字
    movie_name = Ranking.xpath('//*[@id="original_header"]/div[2]/section/div[1]/h2/a/text()')[0].strip() if Ranking.xpath('//*[@id="original_header"]/div[2]/section/div[1]/h2/a/text()') else "暂无"
    # 获得上映时间
    movie_time = Ranking.xpath('//*[@id="original_header"]/div[2]/section/div[1]/h2/span/text()')[0].strip() if Ranking.xpath('//*[@id="original_header"]/div[2]/section/div[1]/h2/span/text()') else "暂无"
    # 获得时长
    movie_duration = Ranking.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[4]/text()')[0].strip() if Ranking.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[4]/text()') else "暂无"
    # 获得简介
    movie_Introduction =Ranking.xpath('//*[@id="original_header"]/div[2]/section/div[3]/div/p/text()')[0].strip() if Ranking.xpath('//*[@id="original_header"]/div[2]/section/div[3]/div/p/text()') else "暂无"
    # 获得标语
    movie_slogan = Ranking.xpath('//*[@id="original_header"]/div[2]/section/div[3]/h3[1]/text()')[0].strip() if Ranking.xpath('//*[@id="original_header"]/div[2]/section/div[3]/h3[1]/text()') else "暂无"
    # 获得导演
    movie_director = Ranking.xpath('//*[@id="original_header"]/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()')[0].strip() if Ranking.xpath('//*[@id="original_header"]/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()') else "暂无"

    dict1={"电影名字":movie_name,"上映时间":re.search(r'\d{4}',movie_time).group(),"时长":movie_duration,"简介":movie_Introduction,"标语":movie_slogan,"导演":movie_director}
    return dict1


# 1.发送请求得到url
target_url_1 = "https://www.themoviedb.org/movie/top-rated" #访问第一页,我们用个体请求
target_url_2 = "https://www.themoviedb.org/discover/movie/items"#注意这是第二个页面用post请求
base_url = "https://www.themoviedb.org"#基本url

movie_list = []

for page_mun in range(1,6      ):
    if page_mun ==1:
        response = requests.get(target_url_1)
        print("我们请求了第",page_mun,"页")
    else:
        response = requests.post(target_url_2,
                               f"air_date.gte=&air_date.lte=&certification=&certification_country=CN&debug=&first_air_date.gte=&first_air_date.lte=&include_adult=false&include_softcore=false&latest_ceremony.gte=&latest_ceremony.lte=&page={page_mun}&primary_release_date.gte=&primary_release_date.lte=&region=&release_date.gte=&release_date.lte=2027-03-26&show_me=everything&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=300&vote_count.lte=&watch_region=CN&with_genres=&with_keywords=&with_networks=&with_origin_country=&with_original_language=&with_watch_monetization_types=&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400&view=&discover_preset=top-rated"
                                 )
        print("我们请求了第",page_mun,"页")
    document=html.fromstring(response.text)

# 2.html解析数据
    Rankings = document.xpath("//div[@class='media-list-results contents']/div")
    for Ranking in Rankings:
        j = requests.get(base_url + Ranking.xpath(".//a/@href")[0])
        print(f"正在请求第{page_mun}页中的{Ranking.xpath('.//a/@href')[0]}")
        p = html.fromstring(j.text)
        movie_list.append(get_movie_info(p))


# 3.放入csv文件中
with open("电影榜单.csv","w",encoding="UTF-8",newline="") as f:
    my_writer = csv.DictWriter(f,fieldnames=["电影名字","上映时间",'时长','简介','标语','导演'])
    my_writer.writeheader()
    my_writer.writerows(movie_list)