#all the values of same type
#Dont have specific values
from array import *

vals=array('i',[0,1,2,3])

print(vals)
#APPEND
vals.append(58)
print(vals)

#Copying Array
newArr= array(vals.typecode,(a*a for a in vals))
print(newArr)
#printing easy way
for j in vals:
    print(j)

#for dynamic printing(if we dont know the length of array while printing)
for j in range(len(vals)):
    print(vals[j])