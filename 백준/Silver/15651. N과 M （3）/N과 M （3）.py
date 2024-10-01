import sys
import copy

N, M = map(int,sys.stdin.readline().split())
visited = [False] * (N+1)

def dfs(stack):

    if len(stack)==M:

        for n in stack:
            print(n, end=" ")
        print()
        return

    for i in range(1,N+1):
        stack.append(i)
        dfs(copy.deepcopy(stack))
        n = stack.pop()

dfs([])