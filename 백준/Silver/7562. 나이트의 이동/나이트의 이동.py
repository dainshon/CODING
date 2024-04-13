import copy
from collections import deque

T = int(input())
dx = [-2,-2,-1,1,2,2,1,-1]
dy = [-1,1,2,2,1,-1,-2,-2,-2]

def BFS(cur_x, cur_y, target_x, target_y, I, arr):
    queue = deque([])
    queue.append((cur_x, cur_y))
    arr[cur_x][cur_y] = 0

    while(queue):

        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=I or ny<0 or ny >= I:
                continue
            if arr[nx][ny]==-1:
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx, ny))

        if arr[target_x][target_y] != -1:
            print(arr[target_x][target_y])
            return




for i in range(T):
    I = int(input())
    visited = [[False for p in range(I)] for q in range(I)]
    arr = [[-1 for p in range(I)] for q in range(I)]
    cur_x, cur_y = map(int,input().split())
    target_x, target_y = map(int,input().split())

    BFS(cur_x, cur_y, target_x, target_y, I, arr)

