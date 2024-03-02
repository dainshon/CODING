import sys

V = int(sys.stdin.readline())
E = int(sys.stdin.readline())

graph = [[] for i in range(V+1)]
visited = [False] * (V+1)

for i in range(E):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(start):
  visited[start] = True
  for v in graph[start]:
    if not visited[v]:
      dfs(v)
      
dfs(1)

result=0
for i in range(2,V+1):
  if visited[i]:
    result+=1

print(result)


  