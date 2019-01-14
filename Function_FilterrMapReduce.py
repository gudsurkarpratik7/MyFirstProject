#1.Filter : Used to filter the data , it filter the data based on given condition that is the function

def is_even(num):
    return num%2==0

nums= [3,2,6,9,8,7,6]

evens=list(filter(is_even,nums))

evens1=list(filter(lambda num:num%2==0,nums))#filter using lambda

print(evens)
print(evens1)
#2.Map : It take a iterable and performs some operation on it

#eg:Finding doubles of given iterable
def update(n):
    return n*2
doubles= list(map(update,evens))

doubles1=list(map(lambda n:n*2,evens))

print(doubles)
print(doubles1)
#3.Reduce

from functools import reduce

def add_all(a,b):
    return a+b

sum = reduce(add_all,doubles)# remember reduce always return a single value not an iterable
sum1 = reduce(lambda a,b :a+b,doubles)
print(sum)
print(sum1)