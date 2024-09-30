        
def solution(diffs, times, limit):
    #answer = 0
    l = 1
    r = max(diffs)
    answer = max(diffs)
    
    cnt = 0
    while(l<r):
        level = (l+r)//2
        # cnt+=1
        # if l>r:
        #     break
        # print("l,r: ", l, r)
        # print(level)
        time = 0
        for i in range(len(times)):
            if diffs[i] > level: # 퍼즐이 더 어려움. 
                time += ((diffs[i]-level)*(times[i]+times[i-1]))+times[i]
            else:
                time += times[i]
        
        if time<=limit:
          #  print("111")
            r = level
            answer = level
        else:
          #  print("22")
            l = level+1
    return answer
    print(answer)
    