import random
x=random.randint(1,10)
a=[1,2,3,4,6]
y=random.choice(a)
print(x,y,end=" ")
print("x+y=",x+y)
random.shuffle(a)
print(a)
print(random.random())