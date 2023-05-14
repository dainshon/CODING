# 시간초과 -> heap사용
import heapq

def solution(n, k, enemy):
    answer = 0
    total = 0
    
    heap = []
    
    for num in enemy:
        heapq.heappush(heap, -1 * num)
        answer+=1   
        total+=num
        
        if(total>n):
            if(k<=0):
                answer-=1
                break
            k-=1
            max_num = -heapq.heappop(heap)
            total-=max_num
            
        
    
        
#     total = 0
#     defence = {}
#     #sorted_enemy = sorted(enemy)

#     for num in enemy:
#         value = defence.get(num)    # O(1)
#         if(value == None):   # 없음
#             defence[num] =1
#         else:
#             defence[num] += 1
        
        
#         total+=num       
#         answer+=1
        
#         if(total>n):
#             if(k<=0):
#                 answer-=1
#                 break
#             k-=1
            
#             key_list = defence.keys()
#             max_num = max(key_list)
            
#             if(defence[max_num]>1):
#                 defence[max_num]-=1
#             else:
#                 del defence[max_num]
            
#             total -= max_num
           
        
    
    return answer