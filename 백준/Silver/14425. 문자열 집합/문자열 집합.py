N, M = map(int, input().split())
S = []
list = []
for i in range(N):
  S.append(input())
for i in range(M):
  list.append(input())

result = 0

dict = {letter : 0 for letter in S}

for i in range(M):
  if(list[i] in dict.keys()):
    result+=1

print(result)