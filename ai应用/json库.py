# json库是用来把json和字典相互转换的
# 1. json.dumps()：Python 对象 ➡️ JSON 字符串
# 2. json.loads()：JSON 字符串 ➡️ Python 对象
# 3. json.dump()：Python 对象 ➡️ 写入文件
# 4. json.load()：读取文件 ➡️ Python 对象

# resp.json() 是 requests 库的方法，它底层就是调用了 json.loads(resp.text)，把服务器返回的 JSON 字符串转成了 Python 字典。
# python
# # 这两行效果是一样的
# results = resp.json()
# results = json.loads(resp.text)


# ============================================================
# 补充知识点
# ============================================================
import json
from datetime import datetime

# ------------------------------------------------------------
# 知识点 5：json.dumps() 的常用参数
# ------------------------------------------------------------
data = {"name": "小明", "age": 18, "skills": ["Python", "AI"]}

# 默认输出：紧凑、无缩进、中文被转成 \uXXXX
print(json.dumps(data))
# {"name": "\u5c0f\u660e", "age": 18, "skills": ["Python", "AI"]}

# indent=4：带缩进，更易读（写给人看的）
print(json.dumps(data, indent=4))

# ensure_ascii=False：中文不再转成 \uXXXX，直接显示中文
print(json.dumps(data, ensure_ascii=False))
# {"name": "小明", "age": 18, "skills": ["Python", "AI"]}

# sort_keys=True：字典的 key 按字母顺序排序输出
print(json.dumps(data, indent=4, ensure_ascii=False, sort_keys=True))

# separators：去掉冒号/逗号后的空格，让输出更紧凑（减少网络传输体积）
print(json.dumps(data, separators=(",", ":")))
# {"name":"\u5c0f\u660e","age":18,"skills":["Python","AI"]}


# ------------------------------------------------------------
# 知识点 6：JSON 类型 ↔ Python 类型 对照
# ------------------------------------------------------------
# JSON        Python
# object      dict
# array       list
# string      str
# number      int / float
# true        True
# false       False
# null        None
s = '{"a": 1, "b": [true, false, null]}'
print(json.loads(s))
# {'a': 1, 'b': [True, False, None]}


# ------------------------------------------------------------
# 知识点 7：序列化特殊对象（datetime / 自定义类）会报错
# ------------------------------------------------------------
# 直接序列化 datetime 会抛 TypeError
try:
    json.dumps({"now": datetime.now()})
except TypeError as e:
    print("报错:", e)  # Object of type datetime is not JSON serializable

# 解决方式一：default 参数传一个转换函数
print(json.dumps({"now": datetime.now()}, default=str))

# 解决方式二：自定义编码器类（继承 json.JSONEncoder）
class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        return super().default(obj)

print(json.dumps({"now": datetime.now()}, cls=MyEncoder))


# ------------------------------------------------------------
# 知识点 8：解析非法 JSON 会抛 json.JSONDecodeError
# ------------------------------------------------------------
bad_json = "{name: 小明}"  # 非法 JSON：key 没加双引号
try:
    json.loads(bad_json)
except json.JSONDecodeError as e:
    print("解析失败:", e)


# ------------------------------------------------------------
# 知识点 9：object_hook 把 JSON 对象转成自定义类实例
# ------------------------------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age!r})"

s2 = '{"name": "小明", "age": 18}'
p = json.loads(s2, object_hook=lambda d: Person(**d))
print(p)  # Person(name='小明', age=18)


# ------------------------------------------------------------
# 知识点 10：文件读写配合 with 语句（推荐，自动关闭文件）
# ------------------------------------------------------------
# 写入文件：dump
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

# 读取文件：load
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded)  # {'name': '小明', 'age': 18, 'skills': ['Python', 'AI']}
