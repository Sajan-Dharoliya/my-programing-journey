import numpy as np


# list1 = [1,2,3,4]# this is list
# list2 = [5,6,7,8]# this is list

# arr_list_2=np.array([list1,list2])
# print(arr_list_2)
# print("   ^ this is 2d array becuase it has two [] square breckets")
# print(arr_list_2.ndim)
# print(" ")
# list1 = [1,2,3,4]
# list2 = [5,6,7,8]
# list3 = [9,10,11,12]
# arr_list_2=np.array([[list1,list2,list3]])
# print(arr_list_2)
# print("   ^ this is 3d array becuase it has three square [] breckets")
# print(arr_list_2.ndim)
# print(' ')

arr1=np.array([[1,2,3],[4,5,6]])
print(arr1)
print("\n")

print("Shape: ",arr1.shape)
print("Size: ",arr1.size)
print("Dtype: ",arr1.dtype)
print("N_dim: ",arr1.ndim)
print("\n")

zero_array=np.zeros((2,3))# it create 2 row 3 colum, 2d array and fiil value of 0 
print(zero_array)
print("\n")

one_array=np.ones((2,3))# it create 2 row 3 colum, 2d array and fiil value of 1
print(one_array)
print("\n")

full_array=np.full((3,2),11)# it create 3 row 2 colum, 2d array and fiil value you want in like 11 (full array)
print(full_array)
print("\n")

diagonal_array=np.eye(5)# diagonal array/matrix that start from top left and end in bottom right
# like this [1,0,0]
#           [0,1,0]
#           [0,0,1] *minimum possible size 3x3, 3 row 3 colum
print(diagonal_array)
print("\n")

print(np.empty(2))
print("\n")

# evenly spaced array
print(np.arange(1,10,2))#(1,10,2).... (1) is starting value and (2) is plus adding value for (10)
#                   first 1 print then it add 2 so 2+1 is 3, and 3+2 is 5 and 5+2 is 7 and 7+2 is 9 then 9+2 is 11 bigger then 10 will not excecute
print("\n")


# spacific number of eqaully (spaced) values between a range
print(np.linspace(1,10,4))# from 1 to 10 sapreat 4 values in 4 lines
print("\n")

#random values array/matrix
random_array=np.random.rand(3,2)
print(random_array)
print("\n")

random_array=np.random.randint(1,10,(3,3))#(1,10,(3,3)) print the random number in range from 1 to 10 in 3x3 (shape) array, 3 row 3 colum
print(random_array)
print("\n")

a=np.array([1,3,5,7,9])
print(a)
print("\n")

print(a[0])
print(a[4])
print(a[-1])
print("\n")
# slicing 
print(a[0:4])# first 3 elements start from 0 index to end index 3
print("\n")
print(a[-3:])# last three element and colon[:] to execute all remaing values
print("\n")
print(a[1:4])# select middle value 
print("\n")
print(a[0::2])# [0::2] start element from 0 index and [2] skip every 2nd element and print third
print("\n")


arr2=np.array([[1,2,3],[4,5,6]])
print(arr2)
print("\n")

print(arr2[1][2])# [1][2] 1 is row and 2 is colum so it print(6 in row 2 and index number 2 [6] )                   
print("\n")

print(arr2[1])# printing only row
print("\n")
print(arr2[1:])# slicing 
print("\n")

print(arr2[0:,1])# row number 0 colum number 1
print("\n")
print(arr2[0:,1])# 1st row [0] and 1st colum element print (use coma)
print("\n")

arr3=np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
print(arr3)
print("\n")
print(arr3[0])
print(arr3[1])
print(arr3[2])
print("\n")
print(arr3[0][2])# 0th row's 2 and colum
print(arr3[2][2])# 2and row [last row] and 2 and colum [last colum element]
print("\n")

print(arr3[:,2])
#       [1,2,3]
#       [4,5,6]
#       [7,8,9]
#            ^ this colum*
print("\n")
print(arr3[::2,0])# [::2,0] skip every 2nd element in 0th row in 0th colum
print("\n")

print(arr3[0::,1:2])# pick every rows but only 1 index colum (2 in not included) last index not include 
print("\n")

arr1=np.array([1,2,3,4,5,6])# 1 row 5 colum   
print(arr1)
print("\n")
# array reshaping
reshaped=arr1.reshape((6,1))
print(reshaped)# it becomes 1d to 2d array, 5 row and 1 colum
print("\n")
reshaped2=arr1.reshape((2,3))
print(reshaped2)# adding more colum
print("\n")
print(reshaped2.flatten())# convert higher dimansion array in 1D
print("\n")
a=np.array([1,2,3])
b=np.array([4,5,6])

print(np.vstack((a,b)))
print(np.hstack((a,b)))
print("\n")

c=np.array([[1,2,3],[4,5,6]])
print(c)
print("\n")

print(np.hsplit(c,3))
print("\n")

split=np.hsplit(c,3)
for s in split:
    print(s)# split array in 3 part (stacking)
print("\n")

vsplit=np.vsplit(c,2)
for s in vsplit:
    print(s)
print("\n")
a=np.array([10,20,40,-30])
print(a)
print("\n")

print(a+10)
print(a-30)
print(a*2)
print(a/10)
print("\n")

b=np.array([1,4,9])
print(b)
print("\n")

print(np.square(b))
print(np.sqrt(b))
print("\n")

a=np.array([1,2,3])
b=np.array([4,5,6])

print(a)
print(b)
print("\n")

print(np.add(a,b))# it add's arrays like 1+4 is 5, 2+5 is 7 and 3+6 is 9
print(np.subtract(a,b))# it minus 1-4 is -3, 2-5 is -3 and 3-6 is -3
print(np.multiply(a,b))#it multiply 1*4 4, 2*5 is 10, 3*6 is 18 
print(np.divide(a,b))#it divide 1\4 is 0.25, 2/5 is  0.4, 3/6 is 0.5
print("\n")

print(np.dot(a,b))# it's give sum of all addition element like 1*4 is 4, 2*5 is 10, 3*6 is 18, so 4+10+18 is 32

t=np.array([[1,2,3],
            [4,5,6]])

print(t)
print("\n")
print(t.T)# it convert row in colum and colum in row like 1,2,3 is row and  
           # [1,4]
           # [2,5]
           # [3,6]
           # ^ ths is now colum(Tranpose)

a=np.array([[1,2,3],[4,5,6]])
print(a)
print("\n")

print(np.sum(a))# sum all element in array
print("\n")
# statistical or statistical function
print(np.mean(a))#  avarege value between 1 to 6 [3.5]
print(np.median(a))# middle avarege value between 1 to 6
print(np.std(a)) # close to middle value or far
print(np.min(a))# minimum  value in array [1]
print(np.max(a))# maximum value in array [6]

# array comparison
a=np.array([1,5,3])
b=np.array([4,5,6]) 
print(a)
print(b)
print("\n")

print(a==b)
print(np.array_equal(a,b))# compare element 1 is = 4 is false 5=5 is true 3=6 is false 
print("\n")

#broodcasting
a=np.array([1,2,3,4])# it add 5 0d array in 1d array
b=np.array([5])  
print(a+b)
print("\n")

c=np.array([[1,2,3],[4,5,6]])# 2d
d=np.array([10,20,30])# it multiply 10 in 1st 1 so 1*10 is 10,2*20 is 40, 3*30 is 90(change smaller Dimansion array in higher dimansion without changing elements)
print(c*d)# it mentend 2d array

data1=np.array([1,2,np.nan,4,np.inf])# chacking nan value
print(data1)# 1,2 and nan value and 4 and infinit
print("\n")# 1 is not nal value so false and false and nan is nan rue, infinate nan false
print(np.isnan(data1)) 
print("\n")
arr=np.array([1,0,0,8])
print(arr)
np.save("my array learning.npy",arr)

loaded_arr=np.load("my array learning.npy")
print(loaded_arr)