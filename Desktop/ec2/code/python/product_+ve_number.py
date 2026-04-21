n=int(input())

a=list(map(int,input().split()))

prod=1

for i in a:
    if i>0:
        prod*=i

print(prod)