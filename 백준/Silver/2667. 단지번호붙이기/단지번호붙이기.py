import sys
from collections import deque

N = int(sys.stdin.readline())
arr = []
visited = []

for i in range(N):
    str = sys.stdin.readline()
    lst = list(str.strip())
    v_lst = [-1 for j in range(N)]
    arr.append(lst)
    visited.append(v_lst)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(s_x, s_y):
    house_num = 1
    queue = deque([])
    queue.append((s_x,s_y))

    while queue:
        pos = queue.popleft()
        x = pos[0]
        y = pos[1]
        arr[x][y] = '-1'

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            if visited[nx][ny] != -1 or arr[nx][ny] != '1':
                continue

            queue.append((nx, ny))
            visited[nx][ny] = 0  # 큐에 넣을때 방문처리 해줘야됨
            house_num+=1
    return house_num


result = 0
house_num_list = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1':
            house_num_list.append(BFS(i,j))
            result += 1
house_num_list.sort()
print(result)
for n in house_num_list:
    print(n)
