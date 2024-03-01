import sys

N, L = map(int, sys.stdin.readline().split())
lst = list(map(int, input().split()))
lst.sort()

result = 0
s = lst[0]

for i in range(1, N):
  if lst[i] - s + 1 > L:
    result+=1
    s = lst[i]

result+=1

print(result)

