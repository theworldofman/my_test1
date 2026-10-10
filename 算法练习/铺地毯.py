# 1. 正确读取 n
n = int(input().strip())

carpets = []
# 2. 正确读取 n 张地毯的信息
for _ in range(n):
    # a, b 为左下角坐标，g, k 为横向和纵向长度
    a, b, g, k = map(int, input().split())
    # 存入列表：左下角 x, 左下角 y, 右上角 x, 右上角 y
    carpets.append((a, b, a + g, b + k))

# 3. 最后读取查询点坐标 (x, y)
x, y = map(int, input().split())

# 4. 核心逻辑：倒序遍历
ans = -1  # 默认没有地毯覆盖，输出 -1
for i in range(n - 1, -1, -1):  # 从 n-1 遍历到 0，即从最后一张地毯往前找
    lx, ly, rx, ry = carpets[i]
    # 判断点 (x,y) 是否在地毯范围内
    if lx <= x <= rx and ly <= y <= ry:
        ans = i + 1  # 地毯编号从 1 开始
        break  # 找到了最上面的一张，直接跳出循环

# 5. 输出答案
print(ans)