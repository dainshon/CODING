import sys
import math

prime = {}

def cal(n):
  result = 0
  for i in range(2,n//2+1):
    if(prime[i]==0 and prime[n-i]==0):
      result+=1
  return result



T = int(sys.stdin.readline())
num = []
max_num =  1000000
for i in range(T):
  number = int(sys.stdin.readline())
  num.append(number)
  if(number > max_num):
    max_num = number

# 가장 큰 애로 에라토스테네스 체
for i in range(max_num+1):
  prime[i] = 0 #다 소수다
for i in range(2, int(math.sqrt(max_num)) + 1):
  if(prime[i]==0):   # 소수일떄(남은거일떄)
    j = 2
    while(i*j<=max_num):
      prime[i*j] = 1
      j+=1

for n in num:
  print(cal(n))

