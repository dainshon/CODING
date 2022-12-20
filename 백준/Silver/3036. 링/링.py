import sys
N = int(sys.stdin.readline())
ring = list(map(int,sys.stdin.readline().split()))

def find_common(a, b):
    common = 1
    div = 2 
    while(1):
        if(a%div==0 and b%div==0):
            a = a//div
            b = b//div
            common *= div
        else:
            div+=1
        
        if(div> min(a, b)):
            break
    return common
        

for i in range(N):
    ring[i]*=2

circle = ring[0]
up = 1
down = 1

for i in range(1,N):
    if(circle%ring[i]==0):
        print(str(circle//ring[i])+'/1')
    else:
        num = find_common(circle, ring[i])
        print(str(circle//num)+'/'+str(ring[i]//num))