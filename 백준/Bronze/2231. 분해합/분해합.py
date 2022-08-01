num = int(input())

for i in range(num+1):
  length = len(str(i))  #자릿수
  result = i
  temp = i

  if(length>0):
    for j in range(length-1, -1, -1):
      result += i//(10**j)
      i = i-(i//(10**j)*(10**j))
    if(result == num):
      print(temp)
      break
    elif(temp == num):
      print('0')
      break