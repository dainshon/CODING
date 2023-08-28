count = int(input())
num = list(map(int, input().split()))
num_1 = num[:]
num_1.sort()

num_dic = {}
i=0
for n in num_1:
  if(n not in num_dic):
    num_dic[n] = i
    i+=1


for n in num:
  print(num_dic[n], end = " ")