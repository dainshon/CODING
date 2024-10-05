import sys
from collections import deque

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

apple = {}
for i in range(K):
    r,c = map(int, sys.stdin.readline().split())
    apple[(r,c)] = 1

L = int(sys.stdin.readline())
change_d = deque()
for i in range(L):
    x, c = sys.stdin.readline().split()
    change_d.append((int(x), c))

# print(apple)
# print(change_d)

snake = deque()

dx = [-1,0,1,0]
dy = [0,1,0,-1]

#turn_dict = {}  # key: 좌표, value: 방향
snake.append((1,1))

head_d = 1 # 머리가 향하는 방향. 처음엔 오른쪽(1)
head_x = 1
head_y = 1

second = 0
while(1):

    # 방향 전환
    if len(change_d)>0 and second == change_d[0][0]:
      #  print("seconde, direction: ", second, change_d[0][1])
        if change_d[0][1] == 'L':  # 왼쪽
            head_d -= 1
            if head_d<0:
                head_d+=4
        else:  # 오른쪽
            head_d += 1
            if head_d>3:
                head_d-=4
        change_d.popleft()
      #  turn_dict[(head_x, head_y)] = head_d

    nx = head_x + dx[head_d]
    ny = head_y + dy[head_d]
   # print(snake[0],snake[-1], second)
    second+=1
    # 앞에 벽 or 자기자신 있는지
    if nx>N or nx<1 or ny>N or ny<1 or (nx, ny) in snake:
        print(second)
        break

    # 이동
    snake.append((nx,ny))
    head_x = nx
    head_y = ny
    # 앞에 사과있으면 걍 머리 추가(꼬래 없애지 X)
    if (nx,ny) not in apple:
        snake.popleft()
    else:
        del apple[(nx,ny)]



