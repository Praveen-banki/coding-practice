a=list(map(int,input().split()))
nz=[i for i in a if i!=0]
z=[0]*a.count(0)

print(*(nz+z))