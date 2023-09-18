import itertools

N = int(input())
S = []
comb = []


def calc_ability(team):
  ability = 0
  nPr = itertools.permutations(team, 2)

  for perm in nPr:
    i = list(perm)[0]
    j = list(perm)[1]
    ability+=S[i][j]
   
  return ability
  
  
  
  

# 능력맵 입력받기
for i in range(N):
  lst = list(map(int, input().split()))
  S.append(lst)

nCr = itertools.combinations(list(range(N)), N//2)

for ncr in nCr:
  comb.append(list(ncr))

result = 100
for i in range(len(comb)//2):
  team_1 = calc_ability(comb[0])
  team_2 = calc_ability(comb[-1])

  del comb[0]
  del comb[-1]

  dif = abs(team_1 - team_2)
  if(result > dif):
    result = dif
  if(result == 0):
    break
  

print(result)  
