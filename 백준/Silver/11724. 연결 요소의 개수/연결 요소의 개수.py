import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())

graph = [[] for i in range(N+1)]
visited = [False for i in range(N+1)]
stack = []

for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

def dfs(n):
    visited[n] = True

    for i in graph[n]:
        if not visited[i]:
            dfs(i)

result = 0
for i in range(1,N+1):
    if not visited[i]:
        result+=1
        dfs(i)

print(result)