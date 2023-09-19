import itertools

N = int(input())
S = list(map(int, input().split()))
result = 0

def calc(lst):
  total = 0
  for i in range(1, len(lst)):
    total += abs(lst[i]-lst[i-1])
  return total

nPr = itertools.permutations(S,N)
for comb in nPr:
  lst = list(comb)
  total = calc(lst)
  if total>result:
    result = total

print(result)