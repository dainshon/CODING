import sys
N, d, k, c = map(int, sys.stdin.readline().split())

num_list = []

for i in range(N):
  n = int(sys.stdin.readline())
  num_list.append(n)

result = []
num_dict = {}

max_len = 0

# 첫번째만
for i in range(k):
  if(num_list[i] in num_dict):
    num_dict[num_list[i]]+=1
  else:
    num_dict[num_list[i]] = 1
copy_ = num_dict.copy()
result.append(copy_)
r = 0
n = k

for i in range(N-1):
  if(n>=N):
    n = n%N
  
  remove_num = num_list[r]
  new_num = num_list[n]
  
  # 앞 삭제
  if(num_dict[remove_num]==1):
    del num_dict[remove_num]
  else:
    num_dict[remove_num]-=1
  # 뒤 추가
  if(new_num in num_dict):
    num_dict[new_num]+=1
  else:
    num_dict[new_num]=1

  if(max_len < len(num_dict)):
    max_len = len(num_dict)

  r+=1
  n+=1
  
  if(len(num_dict)<max_len):
    continue
  copy_ = num_dict.copy()
  result.append(copy_)

max_ = 0
for s in result:
  l = len(s)
  if(c not in s):
    l+=1
  max_ = max(max_, l)

  if(max_>k):
    break
print(max_)
