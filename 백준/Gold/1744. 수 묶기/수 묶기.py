import sys

N = int(sys.stdin.readline())
arr_p = []
arr_m = []
zero_cnt = 0

for i in range(N):
    n = int(sys.stdin.readline())
    if n>0:
        arr_p.append(n)
    elif n == 0:
        zero_cnt += 1
    else:
        arr_m.append(n)
arr_p.sort()
arr_m.sort(reverse=True)

i = len(arr_p)-1
j = len(arr_m)-1


result = 0
while(1):
    if i>0:
        if arr_p[i]>1 and arr_p[i-1]>1:
            result += (arr_p[i]*arr_p[i-1])
            arr_p.pop()
            arr_p.pop()

            i -= 2
        elif arr_p[i] > 0:
            result += arr_p[i]
            arr_p.pop()
            i -= 1

    if j>0:
        result += (arr_m[j]*arr_m[j-1])
        arr_m.pop()
        arr_m.pop()
        j -= 2

    if i<=0 and j<=0:
        break

for c in range(zero_cnt):
    if j>-1:
        arr_m.pop()
        j-=1

result += sum(arr_m)
result += sum(arr_p)

print(result)

