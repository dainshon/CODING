N = int(input())
time = list(map(int, input().split()))

time.sort()
sum = 0
time_sum = []

for i in range(N):
  sum += time[i]
  time_sum.append(sum)

result = 0
for i in range(N):
  result += time_sum[i]

print(result)
