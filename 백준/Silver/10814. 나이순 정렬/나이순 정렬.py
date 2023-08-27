count = int(input())
lst = []
for i in range(count):
  age, name = input().split()
  info = [int(age),name]
  lst.append(info)

lst.sort(key=lambda x: x[0])
for i in range(count):
  print(lst[i][0],lst[i][1])