import sys
N = int(sys.stdin.readline())
board = []

for i in range(N):
    str = sys.stdin.readline()
    arr = list(str)
    del arr[-1]
    board.append(arr)

def check(arr):
    max_count = 0
    count = 1
    for i in range(1, len(arr)):
        if(arr[i-1] == arr[i]):
            count+=1
        else:
            max_count = max(max_count, count)
            count = 1
    max_count = max(max_count, count)        
    return max_count



def change_row(i, j):
    temp = board[i][j]
    board[i][j] = board[i][j+1]
    board[i][j+1] = temp
    
    arr_row = board[i]
    arr_col1 = []
    arr_col2 = []

    for row in board:
        arr_col1.append(row[j])
        arr_col2.append(row[j+1])

    count = max(check(arr_row), check(arr_col1), check(arr_col2))

    #원상복구
    temp = board[i][j]
    board[i][j] = board[i][j+1]
    board[i][j+1] = temp

    return count


def change_col(i, j):
    temp = board[i][j]
    board[i][j] = board[i+1][j]
    board[i+1][j] = temp

    arr_row1 = board[i]
    arr_row2 = board[i+1]
    arr_col = []

    for row in board:
        arr_col.append(row[j])
    
    count = max(check(arr_row1), check(arr_row2), check(arr_col))

    # 원상복구
    temp = board[i][j]
    board[i][j] = board[i+1][j]
    board[i+1][j] = temp

    return count


count = 0
final = 0
flag = 0
for i in range(N):
    for j in range(N):
        if(i<N-1 and j<N-1):
            count = max(change_row(i, j), change_col(i, j))
        elif(i==N-1 and j==N-1):
            break
        elif(i==N-1):
            count = change_row(i, j)
        elif(j==N-1):
            count = change_col(i, j)
        
        if(final < count):
            final = count
        if(final == N):
            flag = 1
            break
    if(flag==1):
        break

print(final)