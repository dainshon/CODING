total = 0
lst = []
for i in range(10):
  N = int(input())
  lst.append(N)
  
for n in lst:

  if(abs(100-total) < abs(100-total-n)):
    break

  total += n
print(total)