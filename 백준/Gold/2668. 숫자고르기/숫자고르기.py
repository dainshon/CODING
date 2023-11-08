import sys
sys.setrecursionlimit(10**6)

num_dict = {}
N = int(input())
result = []

for i in range(N):
  num = int(input())
  if(num == i+1):
    result.append(num)
  elif(num not in num_dict):
    num_dict[num] = [i+1]
  else:
    num_dict[num].append(i+1)

remove_num = []


# 중복된거 remove에 추가
for n in result:
  if(n in num_dict):
    remove_num.extend(num_dict[n])
    del(num_dict[n])

  
# remove_num 만들기
for i in range(1,N+1):
  if(i not in num_dict):
    remove_num.append(i)

while(1):
  # remove_num에 있는거 제거
  for n in remove_num:
    for set in num_dict.items():
      key = set[0]
      value = set[1]
      if(n in value):
        value.remove(n)
        num_dict[key] = value
        break
  
  remove_num = []
  # 빈거있는지 검사해서 remove_num 만듦
  for set in num_dict.items():
    if(len(set[1])==0):
      remove_num.append(set[0])
      
  if(len(remove_num)==0):
    break
    
  for n in remove_num:
    del(num_dict[n])
  # 다시 만들어진 remove_num으로 삭제

for n in num_dict.keys():
  result.append(n)
result.sort()

# 출력
print(len(result))
for i in range(len(result)):
  print(result[i])
  