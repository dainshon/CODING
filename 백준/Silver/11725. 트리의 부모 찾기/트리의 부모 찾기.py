import sys
import copy
sys.setrecursionlimit(10**8)
N = int(sys.stdin.readline())
graph = {}
for i in range(1,N+1):
    graph[i] = []
parents = [0] * (N+1)
for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(node):
    for i in graph[node]:
        if parents[i] == 0:
            parents[i] = node
            dfs(i)


dfs(1)

for i in range(2,N+1):
    print(parents[i])
