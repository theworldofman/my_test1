# Matplotlib是一个功能强大的数据可视化Python库,可以创建静态,动态和交互式的图表
# 一般我们引入matplotlib.pyplot库
import matplotlib.pyplot as plt
# 创建一个简单的折线图

#!!设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei'] # 设置中文字体


# plt.plot([1,2,3,4,5],[1,4,9,16,25])
# 创建一个简单的折线图,前面是x轴数据,后面是y轴数据,注意x,y的个数必须一致
# plt.show()
# 显示图表
# 图标是呈现在画布(Figure)上,当然我们可以为图标附上相关信息
#1.首先我们自己设置画布,如果不设置则自动创建
# plt.figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True)
# 主要用figsize调整大小(宽,高)
#2.设置详细信息
# 设置标题 plt.title("文本")(注意他不识别中文,所以我们需要配置)
# 设置x轴 plt.xlabel("文本")
# 设置y轴 plt.ylabel("文本")
# 显示刻度 plt.xticks() plt.yticks() 设置刻度样式:plt.tick_params()
# plt.xticks(ticks=None, labels=None, rotation=0, fontsize=None,...)
# 1. ticks：刻度位置（数字坐标），决定在哪些坐标点放上刻度
# 2. labels：刻度对应的显示文本，长度必须和 ticks 一致；不写就默认显示 ticks 的数字
# 3. rotation：文字旋转角度，x 轴文字太长经常用 `rotation=45`
# 4. fontsize：刻度文字大小（和 `tick_params(labelsize)` 效果一样）
# 显示网格plt.grid()
# 如果不设置-创建新画布或分割,则所有的线都会划到一个图中,他会自动分割开颜色
# plt.legend()展示图例,如果你在绘制是指定了label,则不用在写入参数,没有则需要
# --------------------------------------------------------------------------------------------
# 我们之前用plt是以过程为主,接下来我们以面向对象为主,axes对象可以画出多个图形
# 使用时我们先导入Axes
# from matplotlib.axes import Axes
# 我们可以用plt.subplots创建图表以及axes(可能是axes列表)
fig, axes = plt.subplots(nrows=1, ncols=2)
# 因为plt.subplots返回值是元组,先返回fig画布,再返回axes列表,当然可以在里面传参调试画布大小
# nrows, ncols 分别表示行数和列数
# 例如 nrows=2, ncols=3 表示创建一个 2 行 3 列的图表,返回的 axes 列表长度为 6
# 绘制柱状图-bar()
axes[0].bar([1,2,3,4,5],[1,4,9,16,25])
axes[0].set_title("柱状图")
axes[0].set_xlabel("X轴")
axes[0].set_ylabel("Y轴")
# 饼状图,分析比例-pie()
# 参数:x-各块的数值(可以是绝对值,matplotlib 会自动按总和算比例)
# labels-每块的名称,个数必须和 x 一致
# autopct-显示百分比格式,如 '%.1f%%',startangle-起始角度等
# %在autopct里有特殊含义所以要在前后加上%