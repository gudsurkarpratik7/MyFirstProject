"""- Conditional statements
- If statement
- Else statement
- Debugging code
- Nested if
- elif and else statement"""

#indentation matters
if False:
    print("Im Right")
    print("Bye")

print("Bye")

#Even or not
x=4
r=x%2

if r==0:
    print("Even Number ")
else:
    print("Odd Number ")


#NEsted if
if r==0:
    print("Even Number ")
    if x>5:
        print('Great')
else:
        print("Odd Number ")

#Elif(use debugger to check performance)
x=2
if x==1:
    print("One")
elif x==2:
    print("TWO")
elif x==3:
    print("Three")
elif x==4:
    print("Four")
else:
    print('Wrong input')
