from collections import deque

def solution(board):
    answer = 0
    map = []
    R = []
    G = []
    
    for b in board:
        lst = list(b)
        map.append(lst)
    
    for i in range(len(map)):
        flag=0
        for j in range(len(map[0])):
            if(map[i][j]=='R'):
                R.append(i)
                R.append(j)
            elif(map[i][j]=='G'):
                G.append(i)
                G.append(j)
            
            if(len(R)!=0 and len(G)!=0):
                flag=1
                break
        if(flag==1):
            break
    
    dx = [-1, 1, 0, 0]    # 상하
    dy = [0, 0, -1, 1]    # 좌우
    x = R[0]
    y = R[1]
    
    def dfs():
        dq = deque()
        visited = [[0]*len(map[0]) for i in range(len(map))]
        visited[x][y] = 1
        dq.append(x)
        dq.append(y)
        
        while(dq):
            cx = dq.popleft()
            cy = dq.popleft()
            if(map[cx][cy]=='G'):
                return visited[cx][cy]
            
            for i in range(4):
                fx = cx
                fy = cy

                while(1):
                    fx, fy = fx+dx[i], fy+dy[i]
                    if(0<=fx<len(map) and 0<=fy<len(map[0]) and map[fx][fy]=='D'):    #  D 만남  
                        fx -= dx[i]
                        fy -= dy[i]
                        break
                    
                    if(fx<0 or fx>=len(map) or fy<0 or fy>=len(map[0])):        #  벗어남
                        fx -= dx[i]
                        fy -= dy[i]
                        break
                if(visited[fx][fy]==0):
                    visited[fx][fy] = visited[cx][cy]+1
                    dq.append(fx)
                    dq.append(fy)
            
        return -1
    
    answer = dfs()
    if(answer>0):
        answer-=1
    
    
    return answer