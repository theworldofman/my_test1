# 自定抓取网络数据的程序或脚本
# 网络页面由三部分组成分别是HTML,CSS,JS
# HTMl:超文本标记语言,负责网页的结构(页面元素和内容)
# CSS:层叠样式表负责网页的表现(页面元素的外观,位置等样式,如颜色,大小等)
# JS:负责页面的行为(交互效果)

# 超文本:超越了文本的限制比文本更加强大(可以定义图片.音频,超链接)
# 标记语言:由标签"<标签名>"构成的语言:1.HTML标签都是预定好的 2.HTMl代码直接在浏览器中运行,由浏览器解析
import requests
from lxml import html
# requests是Python中一个非常流行的HTTP请求库，用于发送HTTP请求并获取响应，常用于爬虫、API测试等场景
# 常用方法有get、post、put、delete等

# get:发送GET请求，用于从服务器获取数据
# resp = requests.get(
#     url="https://httpbin.org/get",
#     headers={"User-Agent":"Mozilla/5.0"},
#     params={"city":"xi'an"}, # 自动拼接url查询参数
#     timeout=10 # 超时时间，单位秒，防止卡死
# )

# post:发送POST请求，用于向服务器提交数据
# resp = requests.post(
#     url="https://api.deepseek.com/v1/chat/completions",
#     headers={"Authorization":"Bearer sk-xxx", "Content-Type":"application/json"},
#     json={"model":"deepseek-chat", "messages":[{"role":"user","content":"你好"}]},
#     timeout=30
# )

# put:发送PUT请求，用于更新服务器上的数据
# esp = requests.put(url, json={...})

# delete:发送DELETE请求，用于删除服务器上的数据
# esp = requests.delete(url,headers={...})

# 调用 get/post 之后得到`resp`，下面是最常用属性
# 1. `resp.status_code` 状态码，200 成功；401 无权限；404 不存在；429 限流；500 服务错误
# 2. `resp.text` 响应内容，**字符串**（网页 HTML）
# 3. `resp.json()` 方法！把返回的 JSON 字符串，直接转成 Python 字典（AI 接口必用）,只有服务器返回 JSON 才能调用，否则报错
# 4. `resp.content` 原始二进制 bytes，下载图片、文件用
# 5. `resp.headers` 服务器返回的**响应头**（字典）
# 6. `resp.request.headers` 查看你本次发出去的请求头，调试用
# 7. `resp.url` 最终访问的真实 url（看是否发生重定向）




target_url = "https://www.tiobe.com/tiobe-index/"
response = requests.get(target_url)

document = html.fromstring(response.text)
a = document.xpath("//table[@id='top20']/thead/tr/th/text()")
print(a)
b = document.xpath("//table[@id='top20']/tbody/tr[position()<21] ")
for c in b:
    print(c.xpath("./td/text()"))















