import sys

T = int(sys.stdin.readline())

for i in range(T):
  N = int(sys.stdin.readline())
  total = 0

  d = 1
  while(1):
    num = 5**d
    if(num > N):
      break
    total += N//num
    d+=1

  print(total)
