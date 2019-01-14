
#Evrything in python is neither call by value nor by reference

def update(arg):
    print("before update",id(arg)) #till this point evrything is call by reference
    arg=8
    print("after update",id(arg))
    print("inside function",arg)

a=10
print("Outside function",id(a))
print("before passsing :",a)
update(a)
print("after passing",a,"thats why everything is neither pass by value nor pass by reference")
