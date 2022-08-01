a, b = map(int, input().split())
arr = []

sample1 = [['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W']]

sample2 = [['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],]

def count(a, b):
  result1 = 0
  result2 = 0
  for i in range(a, a+8, 1):
    for j in range(b, b+8, 1):
      if(arr[i][j]!=sample1[i-a][j-b]):
        result1+=1
      if(arr[i][j]!=sample2[i-a][j-b]):
        result2+=1
  if(result1<result2):
    return result1
  return result2
  
for i in range(a):  #입력받는 과정
  line = []
  line = input()
  line = list(line)
  arr.append(line)

result = 64

for i in range(0, a-7, 1):
  for j in range(0, b-7, 1):   
    if(count(i, j)<result):
      result = count(i, j)
print(result)
    