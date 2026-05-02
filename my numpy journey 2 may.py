import numpy as np
list1=[1,2,3]
list2=[4,5,6]
list3=[7,8,9]
myarr=np.array([list1,list2,list3])
print(myarr)
print("\n")
arr1=np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
print(arr1)
print("\n")
# [start:stop:step]
print(arr1[0:3,0:2])
 #   means i need rows from 0 to 3 and column 0 to 2
print("\n")

print(arr1[0:3, 0:3 :2])# 0:3 and 0:3 pick every row and column, :2 jump every 2nd column

print("\n")

print(arr1[0:3:2])# skip every 2nd row
print("\n")

print(arr1[1][1])
print("\n")

print(arr1.T)
print("\n")

print(np.add(arr1,myarr))
print("\n")
print(np.subtract(arr1,myarr))
print("\n")


print(np.sum(arr1))
print("\n")

print(np.sum(myarr))
print("\n")

print(myarr.T)
print("\n")

nan=np.array([1,2,np.nan,4,5,np.nan,7,np.nan,np.nan,10])
print(nan)
print("\n")

print(np.isnan(nan))# find nan values
print("\n")
print(np.nan_to_num(nan))# replace nan with 0
print("\n")

print(np.full((5,5),11))
print("\n")
print(np.eye(3,3))
print("\n")
print(np.zeros((3,4)))
print("\n")
print(np.ones((2,2)))
print("\n")

print(arr1!=myarr)
print("\n")
print(np.equal(arr1,myarr))
print("\n")

print(np.add(arr1,myarr))
print("\n")
print(np.subtract(arr1,myarr))
print("\n")
print(np.divide(arr1,myarr))
print("\n")
print(np.multiply(arr1,myarr))
print("\n")
print(np.square(arr1))
print("\n")
print(np.sqrt(arr1))
print("\n")

arr1=np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
print(arr1[0:3,0:3:2])# skip column
print("\n")
print(arr1[0:3:2])# skip row
print("\n")
print(arr1[2][1])# 8
print("\n")
print(arr1[1:3,1:2])# [5 8]
print("\n")
print(arr1[1:2,2:])# 6
print("\n")
print(arr1[2:3,2:])# 9 
print("\n")
print(arr1[2:3,0:1])# 7
print("\n")
print(arr1[0:1,2:3])# 3
print("\n")
print(arr1[0:1,0:1])# 1
print("\n")
print(arr1[2:3,1:2])#8
print("\n")
print(arr1[1:2,0:1])#4
print("\n")
print(arr1[0:1,2:3])#3
print("\n")
bigarr=np.array([[1,2,3,4,5],
                 [6,7,8,9,10],
                 [11,12,13,14,15],
                 [16,17,18,19,20]])

print(bigarr[2:3,2:3])#13
print("\n")
print(bigarr[1:2,0:1])#6
print("\n")
# i need 8
print(bigarr[1:2,2:3])# it print 8
# next a need 16
print("\n")
print(bigarr[3:4,0:1])# now it print (16)
# next array indexing 15
print(bigarr[2:3,4:5])# coma means stop
# now it  print 15
print("\n")
print(bigarr[0:4,0:5:4])# jump/step
# i need 0 index column to last index column
# correct
print("\n")
print(np.dot(myarr,arr1))
print("\n")
print(np.sum(bigarr))
print("\n")
print(bigarr.T)
print("\n")
print(bigarr)
print("\n")