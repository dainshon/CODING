str = input()
str_dict = {}
length = len(str)

for j in range(length):
  for i in range(j+1,length+1):
    if (str[j:i] not in str_dict):
      str_dict[str[j:i]] = 0
      

print(len(str_dict))