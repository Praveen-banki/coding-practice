n=int(input()) #5

a=list(map(int,input().split())) # 2 3 6 7 1

count=0

for i in a:
    if i>n:
        count+=1

print(count) # 2