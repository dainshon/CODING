import sys

num = []
a, b = map(int, input().split())
flag = 1

while(1):
  for i in range(2,a+2):
    if(i > a):
      num.append(a)
      num.append(b)
      flag = 0  #while 문 탙출
      break
    if(a%i==0 and b%i==0):
      a = a//i
      b = b//i
      num.append(i)
      break
  if(flag == 0):
    break

result = 1
for n in num:
  result *= n
print(result)
  