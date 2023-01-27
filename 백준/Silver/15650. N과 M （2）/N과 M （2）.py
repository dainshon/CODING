import sys

N, M = map(int,sys.stdin.readline().split())
result = []
visited = [False] * N

def recursion(count,N,M):
    if(count == M):
        print(' '.join(map(str, result)))
        return
    for i in range(N):
        if(len(result)==0):
            result.append(i+1)
            visited[i] = True
            recursion(count+1, N, M)
            visited[i] = False
            result.pop()
        else:
            if not visited[i]:
                if(i+1 > result[-1]):
                    result.append(i+1)
                    visited[i] = True
                    recursion(count+1, N, M)
                    visited[i] = False
                    result.pop()
            


recursion(0, N, M)