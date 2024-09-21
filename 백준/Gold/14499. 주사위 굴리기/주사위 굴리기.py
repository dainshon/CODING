import sys

N, M, x, y, K =map(int, sys.stdin.readline().split())
arr = []

for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    arr.append(lst)
direction = list(map(int, sys.stdin.readline().split()))

dice = [[-1, 0, -1], [0, 0, 0],[-1, 0, -1], [-1, 0, -1]]

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]



for d in direction:
    if x+dx[d]>=N or x+dx[d]<0 or y+dy[d]>=M or y+dy[d]<0:
        continue
    x += dx[d]
    y += dy[d]
    # 굴리는거에 맞게 dice 재배열
    row = dice[1]

    if d==1:
        bottom = dice[1][2]
        dice[1] = [dice[3][1], dice[1][0], dice[1][1]]
        dice[3][1] = bottom
    elif d==2:
        bottom = dice[1][0]
        dice[1] = [dice[1][1], dice[1][2], dice[3][1]]
        dice[3][1] = bottom
    elif d==3:
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[1][1], dice[2][1], dice[3][1], dice[0][1]
    elif d==4:
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[3][1], dice[0][1], dice[1][1], dice[2][1]

    # 숫자 복사
    if arr[x][y] == 0:
        arr[x][y] = dice[3][1]
    else:
        dice[3][1] = arr[x][y]
        arr[x][y] = 0

    # 출력
    print(dice[1][1])
