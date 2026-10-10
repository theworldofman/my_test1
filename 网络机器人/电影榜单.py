import csv
from lxml import html
import requests

with open("05.csv","w",encoding="utf-8",newline='') as f:
    writer = csv.writer(f)
    writer.writerow([ "Title", "Rating", "Introduction"])
target_url = "https://www.themoviedb.org/movie/top-rated"
base_url = "https://www.themoviedb.org"

resp = requests.get(target_url)
document = html.fromstring(resp.text)
Rankings = document.xpath("//div[@class='media-list-results contents']/div[position()<21]")

for i in Rankings:
    j = requests.get(base_url + i.xpath(".//a/@href")[0])
    p = html.fromstring(j.text)
    with open("05.csv", "a", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        arr = p.xpath('//head/title/text()')[0], p.xpath('//div[@class="outer_ring"]/div[@class="user_score_chart"]/@data-percent')[0], p.xpath('//div[@class="header_info"]/div[1]/p/text()')[0]
        if arr[0] != "<null>":
            writer.writerow(arr)

