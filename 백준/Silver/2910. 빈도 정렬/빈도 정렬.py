N, C = map(int, input().split())
num_list = list(map(int, input().split()))

first_index = {}
num_count = {}

for i in range(len(num_list)):
  num = num_list[i]
  if(num not in num_count):
    num_count[num] = 1
    first_index[num] = i
  else:
    num_count[num]+=1
num_count = sorted(num_count.items(), key=lambda x: x[1], reverse=True)

# 출력
for i in range(len(num_count)):
  for j in range(num_count[i][1]):
    print(num_count[i][0], end=" ")