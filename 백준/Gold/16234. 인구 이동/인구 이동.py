import sys
from collections import deque
#10:!3 ~
N, L, R = map(int, sys.stdin.readline().split())
arr = []
result = 0

def init_graph():
    graph = {}
    for i in range(0,N*N):
        graph[i] = []
    return graph

def bfs(graph, node, visited):
    global arr
    dq = deque()
    union = []
    dq.append(node)
    visited[node] = True
    total = 0

    while(1):
        if len(dq)==0:
            break
        union_node = dq.popleft()
        union.append(union_node)
        # total에 더함
        x = union_node//N
        y = union_node%N
        total += arr[x][y]
        for n in graph[union_node]:
            if not visited[n]:
                dq.append(n)
                visited[n] = True

    # 평균으로 arr 수정
    union_len = len(union)
    union_population = total//union_len
    for union_node in union:
        x = union_node//N
        y = union_node%N
        arr[x][y] = union_population
    return visited


# 인구이동 & 결과 arr 반환
def move(graph):
    global arr
    visited = [False] * (N*N)

    for i in range(N*N):
        if not visited[i]: # 시작노드 방문 안했으면 보냄
            visited = bfs(graph,i,visited)

for i in range(N):
    lst = list(map(int, sys.stdin. readline().split()))
    arr.append(lst)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 열려있는거 췤해서 graph 만들기
while(1):
    # graph 만들기 (열려있는거 체크)
    graph = init_graph()
    for i in range(N):
        for j in range(N):

            if j<N-1:
            # 가로
                diff = abs(arr[i][j]-arr[i][j+1])
                if diff>=L and diff<=R:
                    graph[N*i+j].append(N*i+j+1)
                    graph[N*i+j+1].append(N*i+j)

            # 세로
                diff = abs(arr[j][i]-arr[j+1][i])
                if diff>=L and diff<=R:
                    graph[N*j+i].append(N*(j+1)+i)
                    graph[N*(j+1)+i].append(N*j+i)


    # 다 닽혀있으면 break
    flag = 0
    for i in range(N*N):
        if len(graph[i])!=0:
            flag = 1
            break
    if flag==0:
        print(result)
        break

    move(graph)
    result+=1


