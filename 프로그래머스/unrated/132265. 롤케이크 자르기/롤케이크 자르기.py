def solution(topping):
    answer = 0
    dic1 = {}
    dic2 = {}
    for n in topping:
        if(n in dic1):
            dic1[n]+=1
        else:
            dic1[n] = 1
    
    for i in range(len(topping)):
        number = topping[i]
        # dic1에서 삭제
        dic1[number]-=1
        if(dic1[number]==0):
            del dic1[number]
        #dic2에 추가
        if(number not in dic2):
            dic2[number] = 1
            # dic2에 있으면 굳이 +1 안해줘도됨
        
        # 길이같으면 result+1 
        if(len(dic1)==len(dic2)):
            answer+=1
        elif(len(dic1)<len(dic2)):
            break
    
    return answer