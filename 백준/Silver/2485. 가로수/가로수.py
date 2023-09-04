import sys
import math

cnt = int(sys.stdin.readline())
num = []
space = []
result = 0

for i in range(cnt):
  num.append(int(sys.stdin.readline()))
  if(i!=0):
    space.append(num[i]-num[i-1])

if(len(space)>1):
  k = math.gcd(space[0], space[1])
  #space의 최대공약수 구하면됨
  for i in range(2,len(space)):
    k_ = math.gcd(k,space[i])
    if(k_ < k):
      k = k_

  for n in space:
    result += n//k - 1

print(result)
