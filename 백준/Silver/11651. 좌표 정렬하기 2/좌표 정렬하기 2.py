import sys

N = int(sys.stdin.readline())

board = []
y = []

for i in range(N):
   pos = list(map(int,sys.stdin.readline().split()))
   y.append(pos[1])
   board.append(pos)

# 1번째 인덱스 먼저 정렬하고 0번째 인덱스 정렬
sorted_board = sorted(board, key=lambda x:(x[1], x[0]))

for i in range(N):
    print(sorted_board[i][0],sorted_board[i][1])