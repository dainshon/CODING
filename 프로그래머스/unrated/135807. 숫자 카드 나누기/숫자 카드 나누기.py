
def solution(arrayA, arrayB):
    answer = 0 
    common_1 = []
    common_2 = []  
    
    
    # A 최대공약수 구하기
    common_max = GCD(max(arrayA), min(arrayA))
    common_max_list = []
    if(common_max!=1):
        # 공약수 구하기
        for i in range(1, int(common_max**(1/2))+1):
            if(common_max%i==0):
                common_max_list.append(i)
                if(i**2 != common_max):
                    common_max_list.append(common_max//i)
        common_max_list.sort(reverse=True)
        
        for num in common_max_list:
            flag = 0
            for n in arrayA:
                if(n%num!=0):
                    flag = 1
                    break
            if(flag==0):
                common_1.append(num)
            
        if(len(common_1)!=0):    
            for num in common_1:
                flag = 0
                for n in arrayB:
                    if(n%num==0):
                        flag = 1
                        break
                if(flag == 0):
                    answer = num
                    break

        
    # B 최대공약수 구하기
    common_max = GCD(max(arrayB), min(arrayB))
    common_max_list=[]
    if(common_max!=1):
        # 공약수 구하기
        for i in range(1, int(common_max**(1/2))+1):
            if(common_max%i==0):
                common_max_list.append(i)
                if(i**2 != common_max):
                    common_max_list.append(common_max//i)
        common_max_list.sort(reverse=True)
        
        for num in common_max_list:
            flag = 0
            for n in arrayB:
                if(n%num!=0):
                    flag = 1
                    break
            if(flag==0):
                common_2.append(num)

        if(len(common_2)!=0):
            for num in common_2:
                if(num<=answer):
                    break
                flag = 0
                for n in arrayA:
                    if(n%num==0):
                        flag = 1
                        break
                if(flag == 0):
                    answer = num
                    break

    
    return answer

# 최대공약수 리턴
def GCD(a,b):
    while(1):
        if(b==0):
            return a
        temp = a%b
        a = b
        b = temp
    