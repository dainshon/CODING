import sys
map = []
total = 0
H = 0
W = 0

def recursive(r, c):    #4방향
    global total
    #위
    if(r-1 >= 0):
        if(map[r-1][c] != 'X'):
            total += int(map[r-1][c])
            map[r-1][c] = 'X'    
            recursive(r-1, c)
    #아래
    if(r+1 < H):
        if(map[r+1][c] != 'X'):
            total += int(map[r+1][c])
            map[r+1][c] = 'X'
            recursive(r+1, c)
    #오른
    if(c+1 < W):
        if(map[r][c+1] != 'X'):
            total += int(map[r][c+1])
            map[r][c+1] = 'X'
            recursive(r, c+1)
    #왼
    if(c-1 >= 0):
        if(map[r][c-1] != 'X'):
            total += int(map[r][c-1])
            map[r][c-1] = 'X'
            recursive(r, c-1)
    


def solution(maps):
    # 배열에 다시 배치   
    global total
    global H
    global W
    
    for m in maps:
        map.append(list(m))
    H = len(map)
    W = len(map[0])
    answer = []
    
    for i in range(H):
        for j in range(W):
            total = 0
            if(map[i][j] != 'X'):   #  숫자면 재귀 돌림
                total += int(map[i][j])
                map[i][j] = 'X'
                recursive(i, j)
                answer.append(total)
    answer.sort()
    if(len(answer)==0):
        answer.append(-1)
    
    return answer

sys.setrecursionlimit(10**6)

