#armstrong number 153

n=153
temp=n
arm=0
while n>0:
    rem=n%10
    arm=rem**3 + arm
    n//=10
print(arm)
if arm==temp:
    print("armstrong number")
else:
    print("non")