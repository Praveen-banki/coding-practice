y=int(input())
print("Leap Year" if (y%400==0 or (y%4==0 and y%100!=0)) else "Not Leap")