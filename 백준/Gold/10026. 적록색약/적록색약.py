import sys
sys.setrecursionlimit(100000)

N = int(sys.stdin.readline())
arr = []
visited1 = []
visited2 = []
v_list = [False for j in range(N)]
for i in range(N):
    str_list = list(sys.stdin.readline().strip())
    arr.append(str_list)
    v_list1 = [False for j in range(N)]  # 얘를 밖에서 만들어주면 하나 바뀔때 다 바뀜;;
    v_list2 = [False for j in range(N)]
    visited1.append(v_list1)
    visited2.append(v_list2)

dx = [-1, 0, 1, 0] # 위, 오, 아, 왼
dy = [0, 1, 0, -1]
stack = []

def dfs(i,j, visited):
    stack.append(arr[i][j])
    visited[i][j] = True

    for k in range(4):
        nx = i+dx[k]
        ny = j+dy[k]
        if nx<0 or nx>=N or ny<0 or ny>=N:
            continue
        if visited[nx][ny] == True:
            continue
        if arr[nx][ny] != arr[i][j]:
            continue
        dfs(nx, ny, visited)

    if len(stack)==1:
        return 1

result1 = 0

for i in range(N):
    for j in range(N):
        if visited1[i][j] ==  False:
            dfs(i,j, visited1)
            result1+=1

# G->R 고치기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'
result2 = 0
for i in range(N):
    for j in range(N):
        if visited2[i][j] == False:
            dfs(i,j, visited2)
            result2+=1
print(result1, result2)


