def solution(sequence, k):
    answer = []

    s=0
    e=0
    sum_num = sequence[s]
    max_len = 0
    
    while(1):
        if(s>e):
            break
        if(s>=len(sequence) or e>=len(sequence)):
            break
        
        if(sum_num < k):
            e+=1
            if(e<len(sequence)):
                sum_num += sequence[e]
        elif(sum_num==k):
            if(max_len==0):
                answer.clear()
                max_len = e-s+1
                answer.append(s)
                answer.append(e)
            else:
                if((e-s+1)<max_len):
                    answer.clear()
                    max_len = e-s+1
                    answer.append(s)
                    answer.append(e)
            sum_num-=sequence[s]
            s+=1
            e+=1
            if(e<len(sequence)):
                sum_num+=sequence[e]
            else:
                break
        elif(sum_num > k):
            sum_num -= sequence[s]
            s += 1
            

    
    return answer



# def solution(sequence, k):
#     answer = []
    
#     count_max = 0
#     s = -1
#     e = -1
#     for i in range(len(sequence)):
        
#         num_sum = sequence[i]
#         count = 1
#         if(i == len(sequence)-1):
#             if(sequence[i]==k):
#                 s = i
#                 e = i
#             break

#         for j in range(i+1,len(sequence)):
            
#             num_sum += sequence[j]
#             count+=1
#             if(count_max!=0 and count>=count_max):
#                 break
#             if(num_sum == k):
#                 if(count_max==0):
#                     s = i
#                     e = j
#                     count_max = count
                    
#                 else:
#                     if(count < count_max):
#                         s = i
#                         e = j
#                         count_max = count
                        
#                 break
#             if(num_sum > k):
#                 break
                
#     answer.append(s)
#     answer.append(e)
            
#     return answer