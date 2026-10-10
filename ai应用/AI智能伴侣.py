import streamlit as st
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

st.set_page_config(
    page_title="ai智能伴侣",
    page_icon="🥰",
    layout="wide",
    # 控制侧边栏
    initial_sidebar_state="expanded",
    # 设置页面的设置功能
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "#这是一个AI智能伴侣页面!"
    }
)

#首先创建一个会话信息储存缓存起来
if 'messages' not in st.session_state:
    st.session_state.messages = []
# 缓存昵称
if 'nick_name' not in st.session_state:
    st.session_state.nick_name = "小妹"
# 缓存性格
if 'nick_character' not in st.session_state:
    st.session_state.nick_character = "有点腹黑和傲娇的邻家妹妹"

# 大标题
st.title("AI智能伴侣")

# logo
st.logo('ai应用/resource/img_1.png',size='large')

# 把缓存的重新放上去
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])


# 左侧侧边栏编写
# st.sidebar.subheader 第一种方法所有操作加上.siderbar,不简便
# 第二种:with上下文管理器
with st.sidebar:
    st.subheader("伴侣信息")

    # 伴侣名称
    nick_name = st.text_input('昵称',placeholder='请输入昵称',value=st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name

    # 伴侣性格
    nick_character = st.text_area("伴侣性格",placeholder='请输入性格',value=st.session_state.nick_character)
    if nick_character:
        st.session_state.nick_character = nick_character

# ai提示词编写
system_prompt = f"""
       你叫{st.session_state.nick_name},现在是用户的真实伴侣,请完全代入角色:
       规则:
            1.每次只回复一条消息
            2.禁止任何场景或者状态描述词
            3.匹配用户语言
            4.像微信聊天一样回复
            5.可以使用表情
            6.回复的内容要充分体现伴侣特征                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        伴侣特征:
          {st.session_state.nick_character}
       你必须遵守上述规则
"""



# 输入框
prompt = st.chat_input("请输入您的问题?")
if prompt:#字符串自动转化为布尔值,空则false
    # 保存用户的身份和提示词
    st.session_state.messages.append({"role":"user","content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt},
            *st.session_state.messages,
        ],
        stream=False,
    )
    # 非流式输出的数据格式response.choices[0].message.content
    st.chat_message("assistant").write(response.choices[0].message.content)
    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})




