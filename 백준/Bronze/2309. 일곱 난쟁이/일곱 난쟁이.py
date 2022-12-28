import sys

dwarf = []
total = 0
for i in range(9):
    height = int(sys.stdin.readline())
    dwarf.append(height)
    total += height

no_dwarf = total - 100
flag = 1
a = 0
b = 0
for i in range(8):
    for j in range(i+1,9):
        if(dwarf[i]+dwarf[j] == no_dwarf):
            flag = 0
            a = i
            b = j
            break
    if(flag == 0):
        break

final_dwarf = []
for i in range(9):
    if(i!=a and i!=b):
        final_dwarf.append(dwarf[i])

final_dwarf.sort()

for num in final_dwarf:
    print(num)

