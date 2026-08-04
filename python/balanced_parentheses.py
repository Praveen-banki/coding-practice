stack=[]

s=input()

flag=True

for i in s:
    if i=="(":
        stack.append(i)
    elif i==")":
        if not stack:
            flag=False
            break
        stack.pop()

if flag and not stack:
    print("Balanced")
else:
    print("Not Balanced")