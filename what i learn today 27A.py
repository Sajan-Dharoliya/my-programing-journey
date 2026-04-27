import numpy as np

arr=np.array([1,2,3,4,5])
print(arr)
print("\n")

arrzero=np.array(80)
print(arrzero)
print(arrzero.ndim)
print("\n")

arr2=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr2)
print(arr2.ndim)
print(arr2.size)
print(arr2.nbytes)
print("\n")
print(arrzero.nbytes)
print("\n")

print(arr2.itemsize)
print("\n")
print(arr2.dtype)
print("\n")

print(arr2[0,0])
print("\n")
print(arr2[0:1])
print(arr2[0,:1])
print("\n")

arr3=np.array([1,2,3,4,5,6,7,8,9,10])

print(arr3)
print("\n")
print(arr3[1:5])# 1 to last index print
print("\n")

print(arr3[5:])
print(arr3[:5])
print("\n")

print(arr2[1,1:4])
print("\n")

arr4=arr2.copy()
print(arr4)
print("\n")

print(np.zeros((4,5)))
print("\n")
print(np.ones((6,3,3)))
print("\n")

print(np.full((4,4),11))
print("\n")
from numpy import random
#print(np.randint(100))

print(np.random.rand(4,4))
print("\n")

print(np.identity(10))
print("\n")

arrr=np.array([10,20,30,40])
print(arrr)
print("\n")
arrr=arrr+15
print(arrr)
print("\n")


arrr=arrr-40
print(arrr)
print("\n")

arrz=arrr+100
print(arrz)

print("\n")

arrz*10
print(arrz)
print("\n")

arrz/7
print(arrz)
print("\n")

a1=np.array([1,2,3,4,5])
a2=np.array([10,15,20,25,30])
print(a1+a2)
print("\n")

print(np.cos(a1))
print("\n")

print(arr2)
print("\n")

print(np,min(arr3))
print("\n")

print(np.max(arr3))
print("\n")

print(np.sum(arr2))
print("\n")

for x in a1:
    print(x)
print("\n")
for z in arr2:
    print(z)
print("\n")
for a in arr2:
    for b in a:
        print(b)






