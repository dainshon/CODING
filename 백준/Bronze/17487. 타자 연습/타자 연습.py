str = input()
str_list = list(str)

buf = 0
left = 0
right = 0

def LorR(num):
    global buf, left, right
    if((num>=104 and num<=112) or num==117):
        right+=1
    else:
        left+=1

for char in str_list:
    if(ord(char)==32):
        buf+=1
    elif(ord(char)>=65 and ord(char)<=90):    # 대문자
        buf+=1
        LorR(ord(char)+32)
    else:
        LorR(ord(char))

for i in range(buf):
    if(left>right):
        right+=1
    else:
        left+=1

print(left, right)
