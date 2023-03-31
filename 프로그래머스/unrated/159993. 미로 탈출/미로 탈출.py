import sys
sys.setrecursionlimit(10**6)
H = 0
W = 0
map_1 = []
map_2 = []
queue = []

def solution(maps):
    answer = 0
    global H
    global W
    answer = 0
    H = len(maps)
    W = len(maps[0]) 
    s_r=s_c=l_r=l_c=e_r=e_c = 0
    
    for i in range(H):
        map_list1 = []
        map_list2 = []
        m_list = list(maps[i])
        for j in range(W):
            if(m_list[j]=='X'):
                map_list1.append(-2)
                map_list2.append(-2)
            else:
                map_list1.append(-1)
                map_list2.append(-1)
            if(m_list[j]=='S'):
                s_r = i;s_c = j
            elif(m_list[j]=='L'):
                l_r = i;l_c = j
            elif(m_list[j]=='E'):
                e_r = i;e_c = j
                
        map_1.append(map_list1)  
        map_2.append(map_list2)  
        
        # S~L    
    map_1[s_r][s_c] = 0
    
    recursive_1(s_r+1, s_c)
    recursive_1(s_r-1, s_c)
    recursive_1(s_r, s_c+1)
    recursive_1(s_r, s_c-1)
      
    while(queue):
        number = queue.pop(0)
        recursive_1(number//W, number%W)

        # L~E
    map_2[l_r][l_c] = 0
    
    recursive_2(l_r+1, l_c)
    recursive_2(l_r-1, l_c)
    recursive_2(l_r, l_c+1)
    recursive_2(l_r, l_c-1)
      
    while(queue):
        number = queue.pop(0)
        recursive_2(number//W, number%W)
    

    
    if(map_1[l_r][l_c]==-1 or map_2[e_r][e_c]==-1):
        return -1
    else:
        return map_1[l_r][l_c]+map_2[e_r][e_c]

        
    return answer

def recursive_1(i, j):
    number = []
    if(i>=0 and i<H and j>=0 and j< W and map_1[i][j]==-1):
        if(check(i+1,j) and map_1[i+1][j]>=0):
            number.append(map_1[i+1][j])
        if(check(i-1,j) and map_1[i-1][j]>=0):
            number.append(map_1[i-1][j])
        if(check(i,j+1) and map_1[i][j+1]>=0):
            number.append(map_1[i][j+1])
        if(check(i,j-1) and map_1[i][j-1]>=0):
            number.append(map_1[i][j-1])
        if(len(number)!=0):
            map_1[i][j] = min(number)+1    

def recursive_2(i, j):
    number = []
    if(i>=0 and i<H and j>=0 and j< W and map_2[i][j]==-1):
        if(check(i+1,j) and map_2[i+1][j]>=0):
            number.append(map_2[i+1][j])
        if(check(i-1,j) and map_2[i-1][j]>=0):
            number.append(map_2[i-1][j])
        if(check(i,j+1) and map_2[i][j+1]>=0):
            number.append(map_2[i][j+1])
        if(check(i,j-1) and map_2[i][j-1]>=0):
            number.append(map_2[i][j-1])
        if(len(number)!=0):
            map_2[i][j] = min(number)+1 
        
    
def check(i,j):
    if(i>=0 and i<H and j>=0 and j< W):
        queue.append(W*i+j)
        return True
    return False




# graph_1 = []
# graph_2 = []
# H = 0
# W = 0
# map = []
# distance = {}

# def solution(maps):
#     global H
#     global W
#     answer = 0
#     H = len(maps)
#     W = len(maps[0]) 
#     s_r=s_c=l_r=l_c=e_r=e_c = 0
    
#     for m in maps:
#         map.append(list(m))
    
#     # 그래프 생성
#     for i in range(H*W):
#         graph_1.append([])
#         graph_2.append([])
        
        
    
#     for i in range(H):
#         for j in range(W):
#             if(check(i-1, j)!=-1):
#                 graph_1[W*i+j].append(check(i-1,j))
#                 graph_2[W*i+j].append(check(i-1,j))
#             if(check(i+1, j)!=-1):
#                 graph_1[W*i+j].append(check(i+1,j))
#                 graph_2[W*i+j].append(check(i+1,j))
#             if(check(i, j-1)!=-1):
#                 graph_1[W*i+j].append(check(i,j-1))
#                 graph_2[W*i+j].append(check(i,j-1))
#             if(check(i, j+1)!=-1):
#                 graph_1[W*i+j].append(check(i,j+1))
#                 graph_2[W*i+j].append(check(i,j+1))
                
#             if(map[i][j]=='S'):
#                 s_r = i; s_c = j;
#             elif(map[i][j]=='L'):
#                 l_r = i; l_c = j
#             elif(map[i][j] == 'E'):
#                 e_r = i; e_c = j
# #     # S~L
#     distance[10] = 0
#     dfs(10)
    
#     return answer

# def check(i,j): # 연결되었는지 체크
#     if(i>=0 and i<H and j>=0 and j<W):
#         if(map[i][j]!='X'):
#             return i*W+j
#     return -1

# def dfs(begin):
#     visited = [False for i in range(W*H)]
#     stack = []
#     stack.append(begin)
    
#     while stack:
        
            
#     # for number in graph[begin]:
#     #     if(number in distance):
#     #         if(distance[number] > distance[begin]+1):
#     #             distance[number] = distance[begin]+1
#     #     else:
#     #         distance[number] = distance[begin]+1
#     # #print(distance)
#     dfs(number)
    
