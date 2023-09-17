import itertools

N = int(input())
lst = []
for i in range(1, N+1):
  lst.append(i)

nPr = itertools.permutations(lst, N)

for perm in nPr:
  for i in perm:
    print(i, end=" ")
  print()
