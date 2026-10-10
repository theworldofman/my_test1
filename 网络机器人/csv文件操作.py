# csv(Comma-Separated Values,逗号分隔值)是一种简单,通用的文本文件格式,用于储存表格数据,可以直接用Excel打开,注意使用逗号隔开的
# csv使用系统编码注意更改
# 基于python代码

# 文件操作
# 三个步骤1.打开文件 2.操作文件 3.关闭文件
# open()打开模式
# 三个参数(name:要打开的目标文件名的字符串,mode设置打开文件方式,encoding:编码格式,一般为UTF-8)
# open() 的 mode 常用模式：
# r 只读（默认）、w 只写（会清空原内容）、a 追加
# b 二进制（如 rb/wb）、+ 读写（如 r+）

# read() 作用:一次性读取全部（或指定字节数）返回:一个字符串
# readline() 作用:读取一行 返回:字符串
# readlines() 作用:读取所有行 返回:一个字符串列表
# write() 作用:写入字符串
# writelines() 作用:写入字符串列表
# seek() 作用:移动文件读取指针到指定位置
# tell() 作用:返回当前文件指针位置
# flush() 作用:刷新缓冲区，把内容立即写入磁盘
# with open(r"C:\Users\lenovo\Desktop\deepseek-APIkey.txt","r+",encoding="utf-8") as f:
#     print(f.read())
# 为了防止我们忘记关闭,可以用with open方式.自动关闭,在执行完之中的代码后直接关闭

# csv文件打开方式
# 1.原始文件操作
# with open("01.csv","r+",encoding="UTF-8") as f:
#     f.write("姓名,年龄,性别\n")
#     f.write("张三,13,男\n")

# 2.csv操作 方式二:csv
# 首先引入csv库
# import csv
# 一:with open打开文件
# 二:定义一个操作对象 对象名 = csv函数
# csv.reader(文件对象)-按行读取 CSV文件 返回一个列表
# csv.writer(文件对象)-写入 CSV文件 用 writerow()一行 / writerows()多行
# csv.DictReader(文件对象)-按行读取 CSV文件 返回一个字典
# csv.DictWriter(文件对象, fieldnames=)-csv.DictWriter(文件对象, fieldnames=)-可写表头，按字段名对应写入
# 三:对对象进行操作
# import csv
# with open("02.csv","r+",encoding="UTF-8") as f:
#     my_writer =csv.writer(f)
#     my_writer.writerow(["李四",22,"女"])

