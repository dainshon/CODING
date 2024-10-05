import sys
n, k = map(int, sys.stdin.readline().split())

coins_dict = {}
for i in range(n):
    coin = int(sys.stdin.readline())
    coins_dict[coin] = 0
coins = list(coins_dict.keys())
coins.sort()

dp = [0]
for i in range(k):
    dp.append(100000000000)

for coin in coins:
#    print(coin, k)

    for num in range(coin, k+1):
        # quotient = num//coin
        # remain = num%coin
        # if dp[num] == 0:
        #
        #     dp[num] = dp[remain] + quotient
        # else:
        dp[num] = min(dp[num-coin] + 1, dp[num])
if dp[-1] >= 100000000000:
    print(-1)
else:
    print(dp[-1])


