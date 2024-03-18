import sys

arr = []
N, M = map(int, sys.stdin.readline().split())

for i in range(N):
  n = int(sys.stdin.readline())
  arr.append(n)

# 퀵정렬 구현
def quick_sort(start, end, array):
  if start >= end: # 원소 1개면 종료
    return
  
  pivot = start
  left = start+1
  right = end

  while left<=right:
    # 왼쪽에서 pivot 보다 큰거 찾기
    while left <= end and array[left] <= array[pivot]:
      left+=1
    #오른쪽에서 pivot 보다 작은거 찾기
    while right > start and array[pivot] <= array[right]:
      right-=1

    if left < right: # 엇갈리지 X
      array[left], array[right] = array[right], array[left]
    else:
      array[pivot], array[right] = array[right], array[pivot]

  quick_sort(start, right-1, array)
  quick_sort(right+1, end, array)

quick_sort(0, len(arr)-1, arr)

min_gap = 2000000000
flag = False

p1 = 0
p2 = 0


for i in range(N-1):
  p1 = i

  # 배열 하나면 끝
  if N==1:
    min_gap = 0
    break
    
  if p1>=p2:
    p2 = p1+1
    if p2>N-1:
      p2 = N-1

  for j in range(p2,N):
    gap = arr[j] - arr[p1]
    if gap == M:
      min_gap = M
      flag = True
      break
    
    if gap >= M and gap <= min_gap:
      min_gap = gap
      p2 = j
      break
    if gap > min_gap:
      p2 = j
      break


  if flag:
    break
    
      
print(min_gap)    