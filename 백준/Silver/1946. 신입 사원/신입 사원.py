import sys

T = int(sys.stdin.readline())
for i in range(T):
  N = int(sys.stdin.readline())
  arr = [[-1,-1]]
  for j in range(N):
    a, b = map(int, sys.stdin.readline().split())
    arr.append([a,b])
  arr.sort(key=lambda x:x[0])

  result = 1
  second_rank_min = arr[1][1]
  for j in range(2, N+1):
    if arr[j][1] < second_rank_min:
      result+=1
      second_rank_min = arr[j][1]
  print(result)
    