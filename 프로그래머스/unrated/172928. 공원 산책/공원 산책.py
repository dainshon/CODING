def solution(park, routes):
    answer = []
    
    map = []
    p_r = 0
    p_c = 0
    

    for row in park:       
        row =  list(row)
        map.append(row)
    H = len(map)
    W = len(map[0])
    
    # 현재 위치 찾기
    i = 0
    for row in map:
        if('S' in row):
            p_r = i
            j=0
            for loc in row:
                if(loc == 'S'):
                    p_c = j
                    break
                j+=1
            break
        i+=1
        
        
    for route in routes:
        route_list = route.split()
        distance = int(route_list[1])
        flag = 0
        
        if(route_list[0] == 'E'):
            for i in range(1, distance+1):
                if(p_c+i >= W or map[p_r][p_c+i] == 'X'):
                    flag = 1     # 패스
                    break
            if(flag == 0):
                p_c += distance
        
        elif(route_list[0] == 'S'):
            for i in range(1, distance+1):
                if(p_r+i >= H or map[p_r+i][p_c] == 'X'):
                    flag = 1     # 패스
                    break
            if(flag == 0):
                p_r+=distance
        
        elif(route_list[0] == 'W'):
            for i in range(1, distance+1):
                if(p_c-i < 0 or map[p_r][p_c-i] == 'X'):
                    flag = 1     # 패스
                    break
            if(flag == 0):
                p_c -= distance

        elif(route_list[0] == 'N'):          
            for i in range(1, distance+1):
                if(p_r-i < 0 or map[p_r-i][p_c] == 'X'):
                    flag = 1     # 패스
                    break
            if(flag == 0):
                p_r -= distance
                
    answer.append(p_r)
    answer.append(p_c)
                    
            
    
    
    
    
    return answer