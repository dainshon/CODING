import sys
sys.setrecursionlimit(10**6)
N, M, R = map(int,sys.stdin.readline().split())

# graph는 N 인덱스까지 (N+1개)
# dict는 알빠?
# turn은 방문한 숫자갯수만큼
# result는 N 인덱스까지 (N+1개)

graph = []
dict = {}
turn = []

def dfs(root):
    if(dict[root]==0):
        turn.append(root)
    dict[root] = 1 # 방문check
    for g in graph[root]:
        if(dict[g]==0):  # 방문 안했을경우
            dfs(g)

for i in range(N+1):
    graph.append([])
    dict[i+1] = 0   #unchecked로 기본 표시

for i in range(M):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()

dfs(R)

result=[-1 for j in range(N+1)]

for i in range(len(turn)):
    result[turn[i]] = i+1

for i in range(1, N+1):
    if(result[i]==-1): 
        print('0')
    else: 
        print(result[i])
        
