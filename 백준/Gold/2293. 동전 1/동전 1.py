import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
for i in range(n):
    coin = int(sys.stdin.readline())
    coins.append(coin)
coins.sort()

dp = [0] * (k+1)

# 점화식 => dp[n] = dp[n] + dp[n- 동전크기]
for i in range(0,n): # n번 전체 돌면서 갱신
    coin = coins[i]
    if coin > k:
        continue
    dp[coin] += 1
    for j in range(coin,k+1):
        dp[j] += dp[j-coin]

print(dp[k])
