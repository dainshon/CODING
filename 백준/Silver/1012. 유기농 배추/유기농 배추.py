import sys
from collections import deque

T = int(sys.stdin.readline())

def get_result(arr, N, M, lst):
    cnt = 0
    for (x, y) in lst:
        if arr[x][y] == 1:
            arr = bfs(arr, x, y, N, M)
            cnt += 1
    return cnt



def bfs(arr, x, y, N, M):
    queue = deque()
    queue.append((x,y))

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if arr[nx][ny]==0:
                continue

            if arr[nx][ny]==1:
                arr[nx][ny]=0
                queue.append((nx, ny))
    return arr

result = []
for i in range(T):
    N, M, K = map(int, sys.stdin.readline().split())
    arr = [[0]*M for j in range(N)]
    lst = []
    for j in range(K):
        x,y = map(int, sys.stdin.readline().split())
        lst.append((x,y))
        arr[x][y] = 1
    result.append(get_result(arr, N, M, lst))

# 정답 출력
for i in result:
    print(i)

