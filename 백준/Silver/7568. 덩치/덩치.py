N = int(input())
weight = []
height = []
result = []

for i in range(N):
    a, b = map(int, input().split())
    weight.append(a)
    height.append(b)


for i in range(N):
    count = 0
    for j in range(N):
        if((weight[i]<weight[j]) and (height[i]<height[j])):
            count+=1
        
    result.append(count+1)

for i in range(N):
    print(result[i], end=' ')