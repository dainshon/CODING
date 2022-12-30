import sys

# 에라토스테네스의 체
prime = {}
for i in range(2, 1000001):
    prime[i] = 1

for i in range(2, 500001):
    
    if(i in prime):
        j=2
        while(1):
            if(i*j>1000000):
                break
            if(i*j in prime):
                del prime[i*j]
            j+=1

while(1):
    N = int(sys.stdin.readline())
    if(N==0):
        break

    for i in range(3, N//2+1, 2):
        a = i
        b = N-i

        if(a>b):
            break

        if(a in prime and b in prime):
            print(N,'=',a,'+',b)
            break
