import sys  #sys로 안하면 시간초과남.

N = int(sys.stdin.readline())

num = []
dict = {}

for i in range(N):
    num.append(int(sys.stdin.readline()))

num.sort()

# 1. 산술평군
print(round(sum(num)/N))

# 2. 중앙값
half = N//2
print(num[half])

# 3. 최빈값
for i in range(N):
    if(num[i] in dict):
        value = dict[num[i]]
        dict[num[i]] = (value+1)
    else:
        dict[num[i]] = 1
#value대로 sort

sort_dict = sorted(dict.items(), key = lambda dict: dict[1], reverse=True)

if(len(dict)==1):
    print(sort_dict[0][0])
elif(sort_dict[0][1] == sort_dict[1][1]):
    print(sort_dict[1][0])
else:
    print(sort_dict[0][0])

# 4. 범위
print(num[-1]-num[0])

