n,m=map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(0,n+1):
    dp[i]=list(map(int, input().split()))
num=0
for i in range(0,n+1):
    num+=max(dp[i])*pow(2,m)
for j in range(0,m):
    for i in range(0,n+1):
        