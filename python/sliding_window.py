a=list(map(int,input().split()))
k=int(input())

s=sum(a[:k])
mx=s

for i in range(k,len(a)):
    s+=a[i]-a[i-k]
    mx=max(mx,s)

print(mx)