import sys
T = int(sys.stdin.readline())

def count_small(a, B):  #B 배열에서 a보다 작은거 수 구하기
        l = 0 # index
        r = len(B)-1
        result = 0

        while(l<=r):
            mid = (l+r)//2

# 여기 부분에 따라 의도가 달라진다
            if B[mid] < a:
                l = mid+1
                result = mid
            else:
                r = mid - 1

        return result+1

for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    A.sort()
    B.sort()
    cnt = 0
    for a in A:
        if a > B[0]:
            cnt += count_small(a, B)
    print(cnt)

