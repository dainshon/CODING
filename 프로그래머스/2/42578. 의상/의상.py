from itertools import combinations

def solution(clothes):
    answer = 1
    cloth_dict = {}
    
    for cloth in clothes:
        category = cloth[1]
        
        if category in cloth_dict:
            cloth_dict[category]+=1
        else:
            cloth_dict[category] = 1
            
    for c in cloth_dict:
        answer *= (cloth_dict[c]+1)
    
    answer -= 1
    
    return answer