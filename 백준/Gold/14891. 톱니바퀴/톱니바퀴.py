wheel = [[]]
wheel_dict = [{}]

for i in range(4):
  num_str = input()
  num_list = list(map(int, num_str))
  wheel.append(num_list)

for i in range(1,5):
  dict = {}
  dict[0] = 0
  dict[2] = 2
  dict[4] = 4
  dict[6] = 6
  
  wheel_dict.append(dict)


def change_wheel(d):
  for i in range(1, 5):
    if d[i] == 1:   # 시계방향
      for j in range(0,7,2):
        if wheel_dict[i][j]<=0:
          wheel_dict[i][j] = 7
        else:
          wheel_dict[i][j]-=1

    elif d[i] == -1:
      for j in range(0,7,2):
        if wheel_dict[i][j]>=7:
          wheel_dict[i][j] = 0
        else:
          wheel_dict[i][j]+=1

K = int(input())
for i in range(K):
  N, D = map(int, input().split())
  d = [0,0,0,0,0]
  direction = D
  d[N] = D

  # 오른쪽꺼
  for j in range(N+1, 5):
    if wheel[j-1][wheel_dict[j-1][2]] != wheel[j][wheel_dict[j][6]]:
      direction = -direction
      d[j] = direction
    else:
      break

  direction = D
  
  # 왼쪽꺼
  for j in range(N-1,0,-1):
    if wheel[j][wheel_dict[j][2]] != wheel[j+1][wheel_dict[j+1][6]]:
      direction = -direction
      d[j] = direction
    else:
      break
  
  change_wheel(d)

result = 0
for i in range(1,5):
  m = wheel_dict[i][0]
  if m < 0:
    left = (-m)%8
    m = 8 - left
  elif m >7:
    left = m%8
    m = 8 - left
  if wheel[i][m] == 1:
    result += 2**(i-1)
print(result)
  
  
  