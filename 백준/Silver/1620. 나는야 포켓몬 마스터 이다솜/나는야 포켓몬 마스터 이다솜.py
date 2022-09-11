N, M = map(int, input().split())
pokemon = []
test = []
monster = {} #dict

for i in range(N):
  monster[input()] = i+1
for i in range(M):
  test.append(input())

reverse_monster = dict(map(reversed, monster.items()))

for i in range(M):
  if(test[i].isdigit()):  #숫자면
    num = int(test[i])
    print(reverse_monster.get(num, "null"))
  else:
    print(monster.get(test[i], "null"))
      
