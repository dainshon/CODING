N, M = map(int, input().split())
paper = [[0 for i in range(M+1)]]
visited = [[0 for i in range(M+1)]]

for i in range(N):
    num_list = list(map(int, input().split()))
    paper.append([0] + num_list)
    visited.append([0 for j in range(len(num_list)+1)])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

stack = []


dfs_result = 0

def dfs(i,j):
    #print(i,j)
    global dfs_result

    stack.append(paper[i][j])
    visited[i][j] = 1

    if len(stack) == 4:
        #print(stack)
        dfs_result = max(dfs_result, sum(stack))
        stack.pop()
        visited[i][j] = 0
        return

    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]

        if nx <= 0 or nx > N or ny <= 0 or ny > M:   # dfs 들어가기 전에 범위 체크!!!!!
            continue
        if visited[nx][ny] == 1:
            continue
        dfs(nx, ny)


    stack.pop()
    visited[i][j] = 0


result = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        dfs_result = 0
        add_stack_result = 0
        dfs(i, j)
        result = max(result, dfs_result)

# 상 하 좌 우
exec_dx = [-1, 1, 0, 0]
exec_dy = [0, 0, -1, 1]


# ㅗ 모양 체크
for i in range(1, N+1):
    for j in range (1, M+1):

        if (i==1 and j==1) or (i==1 and j==M) or (i==N and j==1) or (i==N and j==M):
            continue

        if i == 1:
            sum_ = paper[i][j] + paper[i][j-1] + paper[i][j+1] + paper[i+1][j]
            result = max(result, sum_)
        elif i == N:
            sum_ = paper[i][j] + paper[i][j-1] + paper[i][j+1] + paper[i-1][j]
            result = max(result, sum_)
        elif j == 1:
            sum_ = paper[i][j] + paper[i-1][j] + paper[i+1][j] + paper[i][j+1]
            result = max(result, sum_)
        elif j == M:
            sum_ = paper[i][j] + paper[i-1][j] + paper[i+1][j] + paper[i][j-1]
            result = max(result, sum_)
        else:
            lst = [paper[i+1][j], paper[i][j+1], paper[i-1][j], paper[i][j-1]]
            sum_ = sum(lst) - min(lst) + paper[i][j]
            result = max(result, sum_)


print(result)

