import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

array.sort()
result = 0

start = 0
end = n-1

while(1):
  if start >= end : 
    break
  
  if array[start] + array[end] == x:
    result += 1
    start += 1
    end -= 1
  elif array[start] + array[end] > x:
    end -= 1
  else:
    start += 1


print(result)
  


