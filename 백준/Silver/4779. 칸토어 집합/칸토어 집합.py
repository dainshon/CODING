
import sys
sys.setrecursionlimit(10**6)
result = []

def recur(s, e, n):  # 시작, 끝, 몇개
  if(n<1):
    return
  #가운데 삭제
  for i in range(s+n, e-n):
    result[i] = " "

  #왼
  recur(s, s+n, n//3)

  #오
  recur(e-n, e, n//3)


while True:
  try:
    N = int(sys.stdin.readline())
    result = ["-" for i in range(3**N)]
    recur(0, 3**N, 3**(N-1))
    for c in result:
      print(c, end="")
    print()
  except:
    break