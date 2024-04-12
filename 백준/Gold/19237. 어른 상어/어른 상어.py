import sys

N, M, K = map(int, sys.stdin.readline().split())
arr = []
shark_loc = {}
board = {}

for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    for j in range(len(lst)):
        if lst[j] != 0:
            shark_loc[lst[j]] = (i,j)
            board[(i,j)] = [lst[j], K]
        else:
            board[(i,j)] = [0, 0, 0]

# 상어 방향
shark_d = list(map(int, sys.stdin.readline().split()))

for i in range(1, M+1):
    loc = shark_loc[i]
    board[loc].append(shark_d[i-1])
#print(board)


# 상어 우선순위
shark_pri = [] # 몇번 상어, 어느 방향일때, 우선순위
for i in range(M):
    lst2 = []
    for j in range(4):
        direction = list(map(int, sys.stdin.readline().split()))
        lst2.append(direction)
    shark_pri.append(lst2)

# 상어 움직임 정보 -> 다음에 어디로 움직여야될지
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

def move_shark():
    move_shark_info = {}
    for i in range(1,M+1):
        if shark_loc[i] == 0:
            continue
    #각 상어별 (i 상어)
        x = shark_loc[i][0]
        y = shark_loc[i][1]
        #print("현재: ", x, y)

        flag = False
        # 아무것도 없는곳으로 이동
        for j in range(4):
            #print(shark_pri[i-1][shark_d[i-1]-1])
            # print(i)
            # print(shark_d)
            # print(shark_pri[i-1][shark_d[i-1]-1])
            move = shark_pri[i-1][shark_d[i-1]-1][j]
            #print("얼마나: ",move)
            nx = x + dx[move]
            ny = y + dy[move]

            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue

            if board[(nx, ny)][0] == 0:
                #print((nx,ny))
                flag = True
                if (nx, ny) not in move_shark_info:
                    move_shark_info[(nx, ny)] = [[i, move]] #j는 방향
                else:
                    move_shark_info[(nx, ny)].append([i,move])
                break

        # 자신 냄새 있는곳으로 이동
        for j in range(4):
            if flag == True:
                break
            move = shark_pri[i-1][shark_d[i-1]-1][j]
            nx = x + dx[move]
            ny = y + dy[move]

            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            if board[(nx, ny)][0] == i:
                if (nx, ny) not in move_shark_info:
                    move_shark_info[(nx, ny)] = [[i, move]]
                else:
                    move_shark_info[(nx, ny)].append([i,move])
                break

    # 움직임
    for loc in move_shark_info:
        if len(move_shark_info[loc])==1:
            shark_num = move_shark_info[loc][0][0]
            shark_direction = move_shark_info[loc][0][1]
            board[loc] = [shark_num, K, shark_direction]
            shark_loc[shark_num] = loc
            #print("바얗ㅇ: ", shark_direction)
            shark_d[shark_num-1] = shark_direction
        else:
            min_info = []
            for info in move_shark_info[loc]:
                if len(min_info)==0:
                    min_info = [info[0], K, info[1]]
                    continue
                # 겹치면 작은거 하나 남기고 죽임
                if info[0] < min_info[0]:
                    #print("죽!: ", min_info[0])
                    shark_loc[min_info[0]] = 0
                    shark_d[min_info[0]-1] = 0
                    min_info = [info[0], K, info[1]]
                else:
                    shark_loc[info[0]] = 0
                    shark_d[info[0]-1] = 0

            board[loc] = min_info
            shark_loc[min_info[0]] = loc
            shark_d[min_info[0]-1] = min_info[2]




result = -1
for i in range(1001):
    # 1만 남았으면 탈출
    cnt = 0
    for p in range(M):
        if shark_d[p]!=0:
            cnt+=1
    if cnt == 1:
        result = i
        break

    move_shark()
    # 냄새 하나씩 줄임
    for p in range(N):
        for q in range(N):
            if board[(p,q)][0] == 0 or (p,q) in shark_loc.values():
                continue
            if board[(p,q)][1] == 1:
                board[(p,q)] = [0,0,0]
                continue
            board[(p,q)][1]-=1

print(result)

