def solution(order):
    answer=0
    order_dict = {}
    visit_dict = {}
    sub = []
    
    for i in range(len(order)):
        order_dict[i+1] = order[order[i]-1]
        visit_dict[i+1] = 0  #  방문X
    
    idx = 1
    start = 0   
    def find(num):   # sub에 이미 존재
        nonlocal start
        if(visit_dict[num]==0): # 아직 안나옴
            for i in range(start, len(order)):
                if(order[i]==num):
                    visit_dict[order[i]]=1
                    start = i+1
                    #del order[:i+1]   # 앞부분 지워줌
                    return 1
                sub.append(order[i])
                visit_dict[order[i]]=1
        elif(sub[-1]==num):
            sub.pop()
            return 1
        elif(visit_dict[num]==1):  #  이미 등장했는데 sub의 top에 있지도않음
            return 0
                
    
    for i in range(1, len(order)+1):        
        result = find(order_dict[i])
        answer+=result
        if(result == 0):
            break
            
    
    return answer