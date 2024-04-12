import sys
from collections import deque

N, M, T = map(int, sys.stdin.readline().split())
circle = {}
x = []
d = []
k = []

for i in range(1, N+1):
    lst = list(map(int, sys.stdin.readline().split()))
    queue = deque(lst)
    circle[i] = queue

def spin(x,d,k):
    for i in range(1,(N//x)+1,1):
        circle_num = i*x
        c_board = circle[circle_num]   # 얕은 복사자 되는거임

        # 시계방향
        if d==0:
            for j in range(k):
                temp = c_board.pop()
                c_board.appendleft(temp)
        # 반시계방향
        elif d==1:
            for j in range(k):
                temp = c_board.popleft()
                c_board.append(temp)



#인접한거 같은지 첵
def check_side():
    change_loc = [] # 0될 애들 모음

    for i in range(1, N+1):
        c_board = circle[i]

        under = i-1
        top = i+1
        for j in range(M):

            if c_board[j] == 0:
                continue

            # 오/왼 인덱스 설정
            right = j-1
            left = j+1
            if right < 0:
                right = M-1
            if left >= M:
                left = 0

            # 오른
            if c_board[j] == c_board[right]:
                change_loc.append((i,j))
                change_loc.append((i,right))
            # 왼
            if c_board[j] == c_board[left]:
                change_loc.append((i,j))
                change_loc.append((i,left))

            # 아래
            if under > 0 and circle[under][j] == circle[i][j]:
                change_loc.append((i,j))
                change_loc.append((under, j))
            # 위
            if top <= N and circle[top][j] == circle[i][j]:
                change_loc.append((i,j))
                change_loc.append((top, j))

    # 인접한애들 0으로 만들어줌
    for loc in change_loc:
        circle[loc[0]][loc[1]] = 0

    if len(change_loc) == 0:
        change2avg()


def change2avg():
    cnt = 0
    total = 0
    for i in range(1, N+1):
        for j in range(M):
            if circle[i][j] == 0:
                continue

            cnt += 1
            total += circle[i][j]
    if cnt == 0:
        return
    avg = total/cnt
    for i in range(1, N+1):
        for j in range(M):
            if circle[i][j] == 0:
                continue
            if circle[i][j] < avg:
                circle[i][j] += 1
            elif circle[i][j] > avg:
                circle[i][j] -= 1

for i in range(T):
    x, d, k = map(int, sys.stdin.readline().split())
    spin(x, d, k)
    check_side()

# 총합 구하기
result = 0
for i in range(1, N+1):
    for j in range(M):
        result += circle[i][j]
print(result)



