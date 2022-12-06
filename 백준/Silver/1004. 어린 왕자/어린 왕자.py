def distance(X, Y, Cx, Cy, R):
    ptp = (Cx-X)**2 + (Cy-Y)**2
    radius = R**2

    if(ptp<radius):   #중심~점 거리 > 반지름 -> 1반환
        return 1
    else:
        return 0


T = int(input())
x=[]
y=[]
r=[]

for i in range(T):
    x.clear()
    y.clear()
    r.clear()
    result = 0

    x1, y1, x2, y2 = map(int, input().split())

    N = int(input())
    for j in range(N):
        X, Y, R = map(int, input().split())
        x.append(X)
        y.append(Y)
        r.append(R)
    
    for j in range(N):
        p1 = distance(x1, y1, x[j], y[j], r[j])
        p2 = distance(x2, y2, x[j], y[j], r[j])

        if((p1==1 and p2==0) or (p1==0 and p2==1)):
            result+=1
    print(result)
