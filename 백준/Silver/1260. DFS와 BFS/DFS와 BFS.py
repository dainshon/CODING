import sys
from collections import deque

N, M, V= map(int, sys.stdin.readline().split())
graph = [[] for i in range(N+1)]
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

for i in range(M):
  a, b = map(int , sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(1,N+1):
  graph[i].sort()




def dfs(v):
  print(v, end=' ')
  visited_dfs[v] = True
  for node in graph[v]:
    if not visited_dfs[node]:
      dfs(node)

def bfs(v):
  visited_bfs[v] = True
  
  while dq:
    current= dq.popleft()
    print(current, end=' ')

    for node in graph[current]:
      if not visited_bfs[node]:
        dq.append(node)
        visited_bfs[node] = True
        

dfs(V)
print()
dq = deque()
dq.append(V)
bfs(V)
  