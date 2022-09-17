N, M = map(int, input().split())
no_listen = {}
both=[]

for i in range(N):
  no_listen[input()] = 1
for i in range(M):
  word = input()
  if word in no_listen.keys():
    both.append(word)

print(len(both))
both.sort()
for i in range(len(both)):
  print(both[i])