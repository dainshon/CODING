import sys
import copy
arr = []
fish_dict = [[] for i in range(17)]  # x,y,direction,
fish_live = [1 for i in range(17)] # 살았는지
max_result = 0

for i in range(4):
    lst = list(map(int, sys.stdin.readline().split()))
    arr_lst = []
    for j in range(4):
        arr_lst.append(lst[2*j])
        fish_dict[lst[2*j]] = [i,j,lst[2*j+1]]
    arr.append(arr_lst)


dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

def fish_move(arr, fish_dict, shark):
    for i in range(1, 17):

        if fish_live[i] == 0:
            continue

    # 현재 가려는 방향으로 갈 수 있는지
        fish = fish_dict[i]
        x = fish[0]
        y = fish[1]

        for j in range(8):
            direction = fish[2]
            direction += j

            if direction > 8:
                direction -= 8

            nx = x + dx[direction]
            ny = y + dy[direction]

            # 공간 넘었을떄
            if nx<0 or nx>=4 or ny<0 or ny>=4:
                continue
            # 상어 자리일때
            if nx == shark[0] and ny == shark[1]:
                continue

            # 갈수있음! -> 물고기 위치 바꿈
            arr[nx][ny], arr[x][y] = arr[x][y], arr[nx][ny]

            fish1 = arr[x][y]
            fish2 = arr[nx][ny]

            # 위치만 바꿔야됨! 방향까지 바꾸면 안됨
            fish_dict[fish1][0], fish_dict[fish2][0] = fish_dict[fish2][0], fish_dict[fish1][0]
            fish_dict[fish1][1], fish_dict[fish2][1] = fish_dict[fish2][1], fish_dict[fish1][1]

            fish[2] = direction

            break
    return arr, fish_dict, shark


def shark_move(arr, fish_dict, shark, score):  # n은 0,1,2
    global max_result
    arr, fish_dict, shark = fish_move(copy.deepcopy(arr), copy.deepcopy(fish_dict), copy.deepcopy(shark))

    for i in range(1,4):
        original_shark_x = shark[0]
        original_shark_y = shark[1]
        original_shark_d = shark[2]

        nx = shark[0] + i*dx[shark[2]]
        ny = shark[1] + i*dy[shark[2]]

        if nx<0 or nx>=4 or ny<0 or ny>=4 or fish_live[arr[nx][ny]]==0:
            max_result = max(max_result, score)
            continue


        # 움직여서 먹고 방향 가짐
        eated_fish = arr[nx][ny]
        score += eated_fish
        shark = [nx, ny, fish_dict[eated_fish][2]]
        fish_live[eated_fish] = 0

        shark_move(copy.deepcopy(arr), copy.deepcopy(fish_dict), copy.deepcopy(shark), copy.deepcopy(score))
        # 먹은거 원상복구 & 상어 위치도 원상복구
        fish_live[eated_fish] = 1
        shark = [original_shark_x, original_shark_y, original_shark_d]
        score -= eated_fish



# 상어 들어가기
eated_fish = arr[0][0]
shark = [fish_dict[eated_fish][0], fish_dict[eated_fish][1], fish_dict[eated_fish][2]]
fish_live[eated_fish] = 0


shark_move(arr, fish_dict, shark, eated_fish)


print(max_result)
