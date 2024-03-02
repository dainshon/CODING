import sys

N = int(sys.stdin.readline())

def next_num(A):
  
  A_list = list(map(int, str(A)))
  last = A_list[-1]
  sub = [last]
  index = -1
  for i in range(len(A_list)-2, -1, -1):
    if A_list[i] < last:
      index = i
      break
    else:
      last = A_list[i]
      sub.append(A_list[i])
      
  if index == -1:
    return "BIGGEST"

  min_diff = 10
  sub_index = -1
  for i in range(len(sub)):
    diff = sub[i] - A_list[index]
    if diff > 0 and min_diff > diff:
      min_diff = diff
      sub_index = i
      if min_diff == 1:
        break

  A_list[index], sub[sub_index] = sub[sub_index], A_list[index]
  sub.sort()
  A_list[index+1:] = sub

  return(''.join(map(str, A_list)))
  


  

for i in range(N):
  A = int(sys.stdin.readline())
  print(next_num(A))
  