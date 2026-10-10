# 本地部署:将大模型部署在自己电脑上.
# 官方提供API:不需要知道内部细节,可以使用其功能
# 云服务平台:

# 本地部署Ollama

# 使用官方开放API
# IP:IP地址相当于设备在互联网中的唯一身份证,用来定位在互联网的位置
# 域名:是由一串用点分割的英文字母,是用来简易化IP的,通过DNS(域名服务器)来与IP互相映射,便于记忆和访问
# 端口是用来标识计算机设备的运行程序(0-65535)
# 网络模型
# HTTP超文本传输协议,规定了请求和响应的统一的规则

#客户端<--------响应--------客户端
#         HTTP协议
#客户端---------请求------->服务器端

# 请求数据规则:分为三部分:
# 1.第一行请求行(请求方式,资源路径,协议)
# 请求方式分为两部分GET请求:请求参数在请求行里没有请求体(请求参数有限制)和POST请求:请求参数在请求体里(无限制)
# 2.请求头:格式(key:value)
# 注意2和3里有空行
# 3.请求体请求参数部分(POST可以有,GET无)

# 响应数据规则
# 1.第一行响应行(协议,状态码)
# 状态码:1.200:客户端请求成功 2.400:请求参数错误 3.404:请求资源不存在,url输入错误,或者资源被删除了 4.500:服务器发生不可预期的错误
# 2.响应头(也是key:value形式)
# 3.响应体(存放服务器相应的数据)

# 会话记忆:滚雪球方式

# 提示词:引导大模型进行内容生产的,为了更好的使其生成符合预期的内容
# 1.给大模型设定角色和能力
# 2.明确任务和请求
# 3.按照步骤拆解复杂任务
# 4.指定风格和语气
# 5.明确要求输出格式
# 6.提供输入输出的示例


# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "你是一个有点腹黑和傲娇的邻家妹妹"},
        {"role": "user", "content": "我喜欢你"},
    ],
    stream=False,
    # reasoning_effort="high",
    # extra_body={"thinking": {"type": "enabled"}}
)

print(response.choices[0].message.content)

