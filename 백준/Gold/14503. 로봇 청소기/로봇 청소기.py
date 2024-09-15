import sys

N, M =map(int, sys.stdin.readline().split())
x, y, d = map(int, sys.stdin.readline().split())
arr = []

result = 0

for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    arr.append(lst)
new_d = d

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while(1):
    #현재칸 청소
    if arr[x][y] != 2:
        arr[x][y] = 2
        result += 1

    is_clean = 0
    #사면 보면서 청소해야되는지 판단
    for i in range(4):
        new_d -= 1
        if new_d<0:
            new_d += 4

        # 청소해야됨?
        if arr[x+dx[new_d]][y+dy[new_d]] == 0:
            x += dx[new_d]
            y += dy[new_d]
            is_clean = 1
            break

    if is_clean==1:
        continue

    # 여기로 넘어오면 청소할거없음.후진
    back_d = new_d + 2
    back_d %= 4

    if arr[x+dx[back_d]][y+dy[back_d]] != 1:
        x += dx[back_d]
        y += dy[back_d]
    else:
        print(result)
        break

