N = int(input())
x = []
y = []

for i in range(N):
    X, Y = map(int, input().split())
    x.append(X)
    y.append(Y)

# *를 써서 배열을 만들면 참조를 복사하기때문에 [][2] 값을 수정하면 2열의 값이 모두 바뀐다.
# 따라서 리스트 함축을 사용하자 

# 둘은 같은결과
# a=[[0]*10]*10
# b=[[0 for j in range(10)] for i in range(10)]
box = [[0 for j in range(100)] for i in range(100)]

for i in range(N):
    for p in range(10):
        for q in range(10):
            box[y[i]+p][x[i]+q] += 1

remove = 0

for i in range(100):
    for j in range(100):
        if(box[i][j]>1):
            remove += (box[i][j]-1)
result = (N*100) - remove
print(result)
