str = input()
str_list = list(str)
num = []
operator = []
p = 0  #문자열에서 전 연산자의 index
number = ''  #각 숫자

for i in range(len(str_list)):
  if(str_list[i]=='+' or str_list[i]=='-'):
    num.append(int(number))
    operator.append(str_list[i])
    number = ''
  else:
      number += str_list[i]

num.append(int(number))

while(1):
  if('+' not in operator):
    break
  for i in range(len(operator)):
    if(operator[i]=='+'):
      sum = num[i] + num[i+1]
      num[i] = sum
      del num[i+1]
      del operator[i]
      break
result = num[0]
for i in range(1,len(num),1):
  result-=num[i]

print(result)

