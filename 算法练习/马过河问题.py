def solve():
    # 1. 读取输入
    n, m, x, y = map(int, input().split())

    # 2. 初始化标记数组 (n+1) x (m+1)
    blocked = [[False] * (m + 1) for _ in range(n + 1)]

    # 马跳跃的偏移量（包含自身 0,0）
    dx = [0, -1, -1, 1, 1, -2, -2, 2, 2]
    dy = [0, -2, 2, -2, 2, -1, 1, -1, 1]

    # 标记马的控制点
    for i in range(9):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx <= n and 0 <= ny <= m:
            blocked[nx][ny] = True

    # 如果起点被马控制，直接输出 0
    if blocked[0][0]:
        print(0)
        return

    # 3. 初始化 DP 数组
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    # 初始化第一列
    for i in range(1, n + 1):
        if not blocked[i][0]:
            dp[i][0] = dp[i - 1][0]

    # 初始化第一行
    for j in range(1, m + 1):
        if not blocked[0][j]:
            dp[0][j] = dp[0][j - 1]

    # 4. 状态转移
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if not blocked[i][j]:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            # else 默认为 0，无需额外操作

    # 5. 输出结果
    print(dp[n][m])


if __name__ == "__main__":
    solve()

# 这道题就是用动态规划解决的
# 动态规划（Dynamic Programming，简称 DP）就是一种“用空间换时间”的算法思想,主要思想:拆解问题，记住答案
# 每个点只算一次，算完就记在账本上。下次谁再问这个点，直接查账本，绝不再算第二次。
# 比递归快很多
# 在这套题里我们使用两个二维数组一个记录是否被马控制，一个记录到达该点的路径数


















