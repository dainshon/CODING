import sys
from collections import deque

R, C, T = map(int,sys.stdin.readline().split())
house = []
c_x1 = -1
c_x2 = -1
change_cell = {}

for i in range(R):
    num_list = list(map(int,sys.stdin.readline().split()))
    house.append(num_list)
# 공청기 위치찾기
for i in range(R):
    if house[i][0] == -1:
        c_x1 = i
        c_x2 = i+1
        break
# # 추가할수 초기화
# for i in range(R):
#     for j in range(C):
#         change_num[(i,j)] = []

#print(change_num)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 확산
def spread():
    global house
    for i in range(R):
        for j in range(C):
            if house[i][j] < 0:
                continue
            cnt = 0
            # 사방을 통해 나를 바꿈
            add_num = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if nx<0 or nx>=R or ny<0 or ny>=C or house[nx][ny] == -1:
                    continue
                add_num += house[nx][ny]//5
                cnt += 1
            add_num -= (house[i][j]//5)*cnt
            change_cell[(i,j)] = add_num

    # 확산 추가
    for add_info in change_cell:
        house[add_info[0]][add_info[1]] += change_cell[add_info]


# 공청기 작동
def clean_air():

    buffer = [house[0][0],house[c_x1][-1], house[R-1][0], house[c_x2][-1]]
# 가로
    # 맨끝 (<-)
    del house[0][0]
    house[0].append(0)

    del house[R-1][0]
    house[R-1].append(0)

    # 중간 (->)
    house[c_x1][2:] = house[c_x1][1:C-1]
    house[c_x2][2:] = house[c_x2][1:C-1]
    house[c_x1][1] = 0
    house[c_x2][1] = 0

# 세로
    # 첫줄
    for i in range(c_x1-2, 0, -1):
        house[i+1][0] = house[i][0]
    house[1][0] = buffer[0]
    for i in range(c_x2+2, R-1):
        house[i-1][0] = house[i][0]
    house[R-2][0] = buffer[2]

    # 막줄
    for i in range(1, c_x1):
        house[i-1][C-1] = house[i][C-1]
    house[c_x1-1][C-1] = buffer[1]
    for i in range(R-2, c_x2, -1):
        house[i+1][C-1] = house[i][C-1]
    house[c_x2+1][C-1] = buffer[3]

for i in range(T):
    spread()
    clean_air()

result = 0
for i in range(R):
    result += sum(house[i])

print(result+2)




