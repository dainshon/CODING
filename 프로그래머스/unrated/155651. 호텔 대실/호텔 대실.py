import datetime

def solution(book_time):
    
    Room = []
    time = {}

    for time in book_time:
        s_h = int(time[0].split(':')[0])
        s_m = int(time[0].split(':')[1])
        e_h = int(time[1].split(':')[0])
        e_m = int(time[1].split(':')[1])
        
        c_start = s_h*60 + s_m
        c_end = e_h*60 + e_m + 10
        
        Room.append([c_start,1])
        Room.append([c_end,-1])

    Room.sort()
    number=0
    max_num = 0
    print(Room)
    
    for i in range(len(Room)-1):
        number += Room[i][1]
        
        if(number>max_num):
            if(Room[i][0] != Room[i+1][0]):
                max_num = number
            
    if(number+Room[-1][1] > max_num):
        max_num = number+Room[-1][1]
    print(max_num)
        
    answer = max_num
        
    
        
    
        
    
    
    
#     Room = []
#     for time in book_time:

#         s_h = int(time[0].split(':')[0])
#         s_m = int(time[0].split(':')[1])
#         e_h = int(time[1].split(':')[0])
#         e_m = int(time[1].split(':')[1])
        
#         c_start = datetime.time(s_h, s_m)
        
#         if(e_h==23 and e_m>=50):
#             c_end = datetime.time(23, 59)
#         elif(e_m>=50):
#             c_end = datetime.time(e_h+1, e_m-50)
#         else:
#             c_end = datetime.time(e_h, e_m+10)
            
#         flag = 1
        
#         for room in Room:
#             flag = 1
#             length = len(room)

#             #start 찾기
#             start_index = -1
#             end_index = -1

#             if(c_start>=room[-1]):  #  맨 뒤에 추가
#                 room.append(c_start)
#                 room.append(c_end)
#                 flag = 0
#                 break
#             elif(c_end <= room[0]): # 맨 앞에 추가
#                 room.insert(0, c_start)
#                 room.insert(1, c_end)
#                 flag = 0
#                 break
#             else:
#                 # start 찾기
#                 for i in range(1, length):
#                     if(c_start>=room[i-1] and c_start<room[i]):
#                         start_index = i
#                         break
#                 # end 찾기
#                 for i in range(length):
#                     if(c_end>room[i-1] and c_end<=room[i]):
#                         end_index = i
#                         break
#                 # start end index  비교
#                 if(start_index == end_index and start_index%2==0):
#                     room.insert(start_index, c_start)
#                     room.insert(start_index+1, c_end)
#                     flag = 0
#             if(flag == 0):
#                 break
#         # flag = 0 이면 이미 추가된거고 1이면 아직 추가 안된것
                
#         if(flag == 1):  # 새로운 룸에 추가 (아무것도 없을때도 추가)
#             Room.append([c_start, c_end])  
#     print(Room)

#     answer = len(Room)
    return answer