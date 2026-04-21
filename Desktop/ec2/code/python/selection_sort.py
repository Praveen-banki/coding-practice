#selection sort

a = [3,4,1,6,2,9,2,0]
n = len(a)
for i in range(n):
    min_a = i
    for j in range(i+1,n):
        if a[min_a] > a[j]:
            min_a = j
    a[i],a[min_a] = a[min_a],a[i]
print(a)