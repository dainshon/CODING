number = []


def solution(n, t, m, p):
    answer = ''    

    i=0
    while(len(number)<=t*m+p):
        change(i,n)
        i+=1

    for i in range(t):
        num = number[(p-1)+(m*i)]
        answer+=str(num)
            
    

    return answer

def change(num,n):
    global number
    n_list = []
    
    while(num>n-1):
        n_list.insert(0, num%n)
        num = num//n
        
    n_list.insert(0,num)
        
    for n in n_list:
        if(n>=10):
            number.append(chr(n+55))
        else:
            number.append(n)