n=int(input())

arr=list(map(int,input().split()))

sum_odd=0
count=0

for i in arr:
    if i%2!=0:
        sum_odd+=i
        count+=1

if count>0:
    avg=sum_odd/count
else:
    avg=0

print(sum_odd)
print(count)
print(round(avg,2))