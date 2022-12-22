import sys

N = int(sys.stdin.readline())
number=[]
for i in range(N):
    number.append(int(sys.stdin.readline()))

common=[]
number.sort()
first = number[0]
second = number[1]
num = second-first
div_num = []

#second-first 의 공약수중에 common이 있으므로 공약수리스트(div_num)구해서 그것들만  비교
# ㅇ뭐야 시간초과;;;
for i in range(2,num//2+1):
    if(num%i==0):
        if(num//i < i):
            break
        elif(num//i == i):
            div_num.append(i)
        else:
            div_num.append(i)
            div_num.append(num//i)
div_num.append(num)

div_num.sort()

for n in div_num:
    flag = 1
    div = first%n
    for j in range(1, len(number)):
        if(number[j]%n != div):
            flag = 0
            break
    if(flag == 1):
        common.append(n)

for num in common:
    print(num, end=' ')