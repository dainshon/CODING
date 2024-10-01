def solution(phone_book):
    answer = True
#    phone_dict = {}
    phone_book.sort()
#    print(phone_book)
    
    for i in range(1,len(phone_book)):
        a_len = len(phone_book[i-1])
        b_len = len(phone_book[i])
        if a_len >= b_len:
            continue
        if phone_book[i-1] == phone_book[i][:a_len]:
            answer = False
            break
                
            
    
    # dict끼리 췤
#     for i in range(1,10):
#         if i not in phone_dict:
#             continue
#         phone_dict[i].sort()

#         flag = 0
#         for p in range(len(phone_dict[i])-1):
#             for q in range(p+1, len(phone_dict[i])):
#                 if len(phone_dict[i][p])<=len(phone_dict[i][q]):
#                     a = phone_dict[i][p]
#                     b = phone_dict[i][q]
#                 else:
#                     a = phone_dict[i][q]
#                     b = phone_dict[i][p]
                
#                 if a == b[:len(a)]:
#                     answer = False
#                     flag = 1
#                     break

#             if flag == 1:
#                 break
        
        
    
    return answer