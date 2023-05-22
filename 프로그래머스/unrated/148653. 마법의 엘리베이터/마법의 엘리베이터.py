def solution(storey):
    answer = 0
    num_list = []
    i = 1
    while(1):
        num_list.append(storey%10)
        storey = storey//10
        
        if(storey<10):
            num_list.append(storey)
            break
        i+=1

        
    buf = 0
    for i in range(len(num_list)):
        num = num_list[i]+buf
        
        if(num>5):
            answer+=(10-num)
            buf = 1
        elif(num<5):
            answer+=num
            buf = 0
        elif(num==5):
            if(i!=len(num_list)-1):
                if(num_list[i+1]<5):
                    answer+=num
                    buf=0
                else:
                    answer+=(10-num)
                    buf=1
            else:
                answer+=num
   
    if(buf==1):
        answer+=1
    
    return answer