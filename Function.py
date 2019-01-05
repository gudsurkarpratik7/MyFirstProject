
def greet():
    print('Hello')
    print('world')

greet()
#returning function
#in python a function can return multipe values

def add_sub(a,b):
    c=a+b
    d=a-b
    return c, d

res1,res2=add_sub(5,4)
print(res1,res2)
