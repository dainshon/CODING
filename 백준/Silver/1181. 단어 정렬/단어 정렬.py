N = int(input())
str = []

for i in range(N):
    str.append(input())

str.sort()
dict = {}

for string in str:
    if(string not in dict):
        dict[string] = len(string)
sort_dict = sorted(dict.items(), key = lambda item: item[1])

for string in sort_dict:
    print(string[0])
