import sys

count = int(sys.stdin.readline())
num = [0 for i in range(10001)]

for i in range(count):
  n = int(sys.stdin.readline())
  num[n]+=1

for i in range(10001):
  if(num[i]!=0):
    for j in range(num[i]):
      print(i)

  