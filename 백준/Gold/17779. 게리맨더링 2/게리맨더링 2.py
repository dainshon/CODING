import sys

N = int(sys.stdin.readline())
A = [[]]
total = 0
for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    total += sum(lst)
    lst = [0] + lst
    A.append(lst)


def max_diff(x,y,d1,d2):
    num_people = [0,0,0,0,0]
    boundary = []


    for i in range(d1+1):
        boundary.append((x+i, y-i))
        boundary.append((x+d2+i, y+d2-i))
    for i in range(d2+1):
        boundary.append((x+i, y+i))
        boundary.append((x+d1+i, y-d1+i))

    is_5 = -1
    for i in range(1,N+1):
        for j in range(1, N+1):
            if (i,j) in boundary:
                num_people[4] += A[i][j]
                if (i,j) != (x, y) and (i,j) != (x+d1+d2, y-d1+d2):
                    is_5 = -is_5
            elif is_5 == 1:
                num_people[4] += A[i][j]
            elif 1 <= i < x+d1 and 1 <= j <= y:
                num_people[0] += A[i][j]
            elif 1 <= i <= x+d2 and y < j <= N:
                num_people[1] += A[i][j]
            elif x+d1 <= i <= N and 1 <= j < y-d1+d2:
                num_people[2] += A[i][j]
            elif x+d2 < i <= N and y-d1+d2 <= j <= N:
                num_people[3] += A[i][j]

    return max(num_people) - min(num_people)



result = 1000000000000

for i in range(1, N-1):
    for j in range(2, N):
        for p in range(1, N+1):
            if i+p > N or j-p < 1:
                break
            for q in range(1, N+1):
                if j+q > N or i+p+q > N:
                    break
                value = max_diff(i,j,p,q)
                result = min(result, value)

print(result)


