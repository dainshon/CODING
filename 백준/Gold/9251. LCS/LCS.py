import sys

str1_list = list(input())
str2_list = list(input())


str1 = ['a'] + str1_list
str2 = ['a'] + str2_list


map = []


for i in range(len(str1)):
  lst = [0 for j in range(len(str2))]
  map.append(lst)

for i in range(1,len(str1)):
  for j in range(1,len(str2)):
    if str1[i] == str2[j]:
      map[i][j] = map[i-1][j-1] + 1
    else:
      map[i][j] = max(map[i][j-1], map[i-1][j])

print(map[-1][-1])


