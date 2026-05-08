a=int(input("enter first subject mark: "))
b=int(input("enter second subject mark: "))
c=int(input("enter third subject mark: "))
d=int(input("enter fourth subject mark: "))
e=(a+b+c+d)/4
if e>75:
    print("distinction")
elif e==60 and e<76:
    print("1st division")
elif e==50 and e<60:
    print("2nd division")
elif e==40 and e<50:
    print("3rd division")
else:
    print("fail")
