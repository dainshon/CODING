#2630
N = int(input())
box = []
for i in range(N):
    row = list(map(int, input().split()))
    box.append(row)
blue = 0
white = 0
flag = -1

def partition(r, c, n):
    # blue, white 는 전역변수를 갖다 쓸것 선언
    global blue
    global white

    if(n<=1):
        if(box[r][c]==1):
            blue+=1
        elif(box[r][c]==0):
            white+=1
        return -1

    # 네모가 모두 같을때
    flag = box[r][c]
    for i in range(r,r+n):
        for j in range(c,c+n):
            if(box[i][j]!=flag):
                flag = -1
                break
    if(flag==1):
        
        blue+=1
        return -1
    elif(flag==0):
       
        white+=1
        return -1

    # 네모가 모두 다를때 (return 되지 않아서 여기까지옴)
    partition(r, c, n//2)
    partition(r+n//2, c, n//2)
    partition(r, c+n//2, n//2)
    partition(r+n//2, c+n//2, n//2)

partition(0, 0, N)


print(white)
print(blue)
