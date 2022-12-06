# 문자열을 배열에 하나씩 넣기
str = input()
list = list(str)
list.sort(reverse=True)

result = ''
for string in list:
    result+=string

print(result)
