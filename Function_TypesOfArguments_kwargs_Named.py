
def sum(a,b): #formal arguments
     c=a+b
     print(c)


sum(5,6)     #Actual argument


# actual arguments types:
#1.Keyword
def person(name, age):
    print(name)
    print(age)


person(name="pratik", age=60)#keyword

#2.default
def person1(name, age=18):
    print(name)
    print(age)

person1(name="pratik")
person1(name="pratik",age=25)

#3.variable length
def sum(a, *b):
    print(a)
    print("observe this is a tuple",b)


sum(5, 6,56,78)


#Keyworded Variable Length Arguments

def person3(name, **data):
    print(name)
    for i,j in data.items():   # Notice .item is method of dictionary which returns tuples of key value pair
        print(i,':',j)


person3(name="pratik", age=60,address="Pune",number=9845100)#keyword