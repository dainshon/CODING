import sys
from itertools import combinations
from collections import deque
import copy

N, M = map(int, sys.stdin.readline().split())
arr = []
virus = []
empty = []

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

final_result = 0

def cnt_empty(lab):
    result = 0
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                result+=1
    return result

def spread_virus(lab):
    for (vx, vy) in virus:
        #초기
        queue = deque()
        queue.append((vx, vy))

        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx<0 or nx>=N or ny<0 or ny>=M:
                    continue
                # if lab[nx][ny] != 0:
                #     continue
                if lab[nx][ny] == 0:
                    lab[nx][ny] = 2
                    queue.append((nx, ny))
    result = cnt_empty(lab)
    return result



for i in range(N):
    row = list(map(int,  sys.stdin.readline().split()))
    arr.append(row)
    for j in range(M):
        if row[j] == 1:
            continue
        elif row[j] == 0:
            empty.append((i,j))
        elif row[j] == 2:
            virus.append((i,j))

for loc in combinations(empty, 3):
    lab = copy.deepcopy(arr)
    for (x, y) in loc:
        lab[x][y] = 1

    final_result = max(spread_virus(lab), final_result)

print(final_result)
