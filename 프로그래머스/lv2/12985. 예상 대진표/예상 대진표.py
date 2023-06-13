def solution(n,a,b):
    answer = 0
    number = n
    while(1):
        if(number<=1):
            break
        number = number//2
        answer+=1

    min_ = min(a,b)
    max_ = max(a,b)
    
    mid = n//2
    while(1):
        if(answer==1):
            break
        if(min_<=mid and max_>mid):
            break
        elif(min_<=mid):    # 중간값 기준 왼쪽
            answer-=1
            mid-=2**(answer-1)
        elif(min_>mid):     # 중간값 기준 오른쪽
            answer-=1
            mid+=2**(answer-1)

            
        
    
    return answer