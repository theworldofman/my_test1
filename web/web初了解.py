# web网站由三个核心部分构成:前端程序,服务端程序,数据库.

# 前端:界面展示--->服务端:业务逻辑--->数据库:数据存储
# 前端程序:负责前端页面的开发,网页由HTML(负责网页的结构),css(负责网页的表现),javascript(互动)组成

# 服务端程序:基于FastAPI来进行开发

# 使用步骤
# 1.导入FastAPI
# 2.创建FastAPI实例对象
# 3.创建路径操作函数,定义访问路路径
# 4.运行FastAPI服务
# 4.1.可以用fastapi dev "  .py"--------------在终端运行
# 4.2.uvicorn ....:app --reload-------------在终端运行
# 4.3.运用py里的轻量启动服务uvicorn
# 导入uvicorn import uvicorn
# uvicorn.run(FastAPI对象,host,port)




from fastapi import FastAPI

# 创建FastAPi实例
app=FastAPI()
# 定义api接口-------------函数返回值是接口的响应数据
@app.get('/')
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

# Restful指的是遵循REST架构风格的API接口服务,也就是url简洁化,是约定方式,不是强制,描述模块功能通常使用复数形式,比如/users表示用户模块











