import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
homes = []
chicken = []

arr = []
for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if lst[j] == 1:
            homes.append((i, j))
        elif lst[j] == 2:
            chicken.append((i,j))
    arr.append(lst)

def get_min_distance(home, chicken_lst):
    min_distance = 25000
    for (chicken_x, chicken_y) in chicken_lst:
        distance = abs(home[0]-chicken_x) + abs(home[1]-chicken_y)
        min_distance = min(distance, min_distance)
    return min_distance


result = 100000000000000
for safe_chicken in combinations(chicken, M):
    total = 0
    for home in homes:
        total += get_min_distance(home, safe_chicken)
    result = min(result, total)
print(result)

