def solution(k, tangerine):
    answer = 0
    tang_dict = {}
    
    for t in tangerine:
        if(t in tang_dict):
            tang_dict[t]+=1
        else:
            tang_dict[t] = 1
        
    v_list = list(tang_dict.values())
    v_list.sort()
    v_list.reverse()
    
    
    for v in v_list:
        k-=v
        answer+=1
        if(k<=0):
            break
    
    return answer