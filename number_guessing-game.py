print("Welcome to number guessing game")
n=1
s=0
t=0
while n==1 :
    print("Enter range ")
    x=int(input("enter starting number:"))
    y=int(input("enter ending number:"))
    z=int(input("enter the guessing number:"))
    import random
    m=random.randint(x,y)
    if m==z:
        print("your guessing is correct")
        s=s+1
    else:
        print("your guessing is incorrect")
        print("correct number=",m)
    t=t+1
    n=int(input("Do you want to continue? enter 1 else enter 0 ="))
print("your score is=",s)
print("your total participated in the game=",t)
print("Thankyou for playing")
