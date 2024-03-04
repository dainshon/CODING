import sys

N = int(sys.stdin.readline())
A, B = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())

graph = [[] for i in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

result = -1
terminate = False

def dfs(current, target, count):
  global terminate
  global result
  
  count+=1
  
  if current == target:
    terminate = True
    result = count
    return
 
  visited[current] = True
  for node in graph[current]:
    if terminate:
      break
    if not visited[node]:
      dfs(node, target, count)

  return


dfs(A,B,-1)
print(result)
