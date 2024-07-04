import numpy as np
#? types of Array Creation in numpy
l1 = [1,2,3,4,5,6,7,8,9]
print(type(l1))
arr = np.array(l1) #? creates an array of object passed as perameter

z = np.zeros(3) #? creates an array which is completely filled with zeros also takes size as parameter
print(z)

one = np.ones(3) #? creates an array which is completely filled with ones also takes size as parameter
print(one)

f = np.full(5,4,str) #? creates an ARRAY and takes first argument as size and another as value and third as datatype
print(f)

e = np.empty(5) #? creates an empty array whoes each index is filled with unique or random values
print(e)

a = np.arange(10) #? creates an empty array whoes each value is same as its index value
print(a)

l = np.linspace(2,20,10,int) #? creates an array of linearly splaced element ie difference of 2 adjecent element is equal it take first argumnet as Starting second as ending and 3rd as no of elements requried
print(len(l))
print(l)

identity = np.eye(3) #? creates an identity matrix and takes row and col as parameter if single parameter is given it creates an square matrix
print(identity)