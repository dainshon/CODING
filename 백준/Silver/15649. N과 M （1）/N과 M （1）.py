# 어렵군여

import sys

N, M = map(int,sys.stdin.readline().split())
result = []
visited = [False] * N

def recursion(count,N,M):
    if(count == M):
        print(' '.join(map(str, result)))
        return
    for i in range(N):
        if not (visited[i]):
            result.append(i+1)
            visited[i] = True
            recursion(count+1, N, M)
            visited[i] = False
            result.pop()



recursion(0, N, M)