import sys

N = int(sys.stdin.readline())

schedules= []
table = []
left = []

for i in range(N):
  s, e = map(int, input().split())
  schedules.append([s,e])

# x[1]에 대해서 오름차순, x[0]에 대해서 오름차순
schedules.sort(key=lambda x: (x[1],x[0]))

result = 0
end = 0
for schedule in schedules:
  if end<=schedule[0]:
    result +=1
    end = schedule[1]

print(result)
  
  



  