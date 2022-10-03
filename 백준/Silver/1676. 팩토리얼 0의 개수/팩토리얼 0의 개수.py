N = int(input())
two=0
five = 0

for i in range(N,1,-1):
  num = i

  if(num%5==0 or num%2==0):
    while(1):
      if(num%5==0):
        five+=1
        num = num//5
      if(num%2==0):
        two+=1
        num = num//2

      if(num%5 != 0 and num%2 != 0):
        break

print(min(five, two))
    