# streamlit是一个开源py库可以快速基于py代码构建交互式的web网站
# 使用步骤:1.引用streamlit模块
# 2.基于streamlit中的API来构建web应用
# 3.运行streamlit run xxxx.py 必须在终端里运行
import streamlit as st
import streamlit as st

# 设置页面

st.set_page_config(
    # 这是给这个页面命名,比如百度
    page_title="李恒鑫 App",
    # 这是设置前面页面图标
    page_icon="🧊",
    # 设置页面布局
    layout="wide",
    # 控制侧边栏
    initial_sidebar_state="expanded",
    # 设置页面的设置功能
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# 我丢你老某!"
    }
)


# 定义标题
st.title("入门演示")
st.header("一级标题")
st.subheader("二级标题")

# 段落文字
st.write("滴答滴答斗殴案涉及滴哦")


# 引入图片
# .代表当前目录
st.image("ai应用/resource/img.png")

# 引入音频
# st.audio

# 引入视频
# st.video

# 设计logo
# st.logo

# 引入表格
# st.table
#可以传入一个大字典value是列表按列排放

# 输入框
hh=st.text_input("我帅不帅","帅")
st.write(hh)

#密码输入框 输入框关键字type=password

# 单选按钮
ac = st.radio("我帅不帅",["帅","特别帅"])
st.write(ac)






