import numpy as np
# arr=np.array([1,2,3,4,5,])# 1D 

arrzero=np.array(80)# 0D
print(arrzero)

print(arr.ndim)
print(arrzero.ndim)

arr2 =np.array([[1,2,3,4,5,],[6,7,8,9,10]])
print(arr2)
print(arr2.ndim)# seen for dimansion (this is 2D array)

print(arr2.size)
print(arr2.nbytes)# memory allocation for each item (bytes)

print(arr2.itemsize)# memory for single item 

print(arr2.dtype)


print(arr2[1,:])

arr3=np.array([1,2,3,4,5,6,7,8,9,10])

print(arr3[1:5])
print(arr3[:5])# last to first
print(arr3[5:])# first to last

print(arr2[1,1:4])

arr4=arr2.copy()# copy array
print(arr4)

print(np.zeros((4,6)))
print(np.ones((3,3,3)))# matrix

print(np.full((4,4),45)) #45 number matrix\array
from numpy import random
x=random.randint(100)
print(x)
print(np,random.rand(50,50))

print(np.identity(5))

arran=np.array([10,20,30,40])
print(arran)
arran=arran+15
print(arran)
print(arran)

arran=arran-40
print(arran)

arran=arran*10
print(arran)

arran=arran/7
print(arran)

a=np.array=([0,2,3,4,5])
a=np.array=([10,15,20,25,30])
print(a1+a2)

print(np.cos(a))
print(np.max(arr2))
print(np.min(arr2))
print(np.sum(arr2))

for z in arr2:
    print(z)

for a in arr2:# arr2 value store in a 
    for b in a: # a value now store in b and b will print in loop
        print(b)