from array import *

arr = array('i',[])

n =int(input('Enter the length of array '))

for i in range(n):
    val=int(input('Enter a value '))
    arr.append(val)


print(arr)

e =int(input('Enter the value you want to search: '))

count=0;
for val in arr:
    if e==val:
        print(count)
        break;
    count += 1;

#ADDED COMMENT