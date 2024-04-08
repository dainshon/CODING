import sys
from collections import deque
# 최단경로 -> BFS
N = int(sys.stdin.readline())
arr = []
shark_size = 2
num_shark_eat = 0
cur_x = 0
cur_y = 0
INF = 1e9

for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if lst[j] == 9:
            cur_x = i
            cur_y = j
    arr.append(lst)
arr[cur_x][cur_y] = 0

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# 얜 재귀로 돌리는게 아님
def BFS(x, y): # 이 시작점에서 모든 점까지의 거리 구함
    distace_map = [[-1 for i in range(N)] for j in range(N)]
    distace_map[x][y] = 0

    queue = deque()
    queue.append((x,y))
    #print(queue)

    while queue:
        pos = queue.popleft()
        #print("post: ",pos)
        x = pos[0]
        y = pos[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if arr[nx][ny] > shark_size:
                continue

            if distace_map[nx][ny] == -1 and arr[nx][ny] <= shark_size:
                distace_map[nx][ny] = distace_map[x][y]+1
                queue.append((nx,ny))
        #print(queue)
    return distace_map


min_distance = INF
# 가장 가까운 물고기 찾기
def find_close_fish(distance_map):
    global min_distance
    global cur_x, cur_y

    for i in range(N):
        for j in range(N):
            if distance_map[i][j] == -1:
                continue
            if distance_map[i][j] < min_distance and 0 < arr[i][j] < shark_size:
                min_distance = distance_map[i][j]
                cur_x = i
                cur_y = j
    return min_distance

result = 0
while(1):
    min_distance = INF
    value = find_close_fish(BFS(cur_x, cur_y))
    if value == INF:
        break

    # 먹고 비워주기
    num_shark_eat+=1
    arr[cur_x][cur_y] = 0

    if num_shark_eat >= shark_size:
        shark_size+=1
        num_shark_eat = 0
    result += value

print(result)


