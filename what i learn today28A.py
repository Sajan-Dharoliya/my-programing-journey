import numpy as np

list1=[1,2,3]
print(list1)
print("\n")

arr_list1 =np.array(list1)
print(arr_list1)
print("\n")

print(type(arr_list1))
print("\n")

list1=[1,2,3]
list2=[4,5,6]

arr_list1_2=np.array([list1,list2])
print(arr_list1_2)
print("\n")

list1=[1,2,3]
list2=[4,5,6]
list3=[7,8,9]

arr_list_3=np.array([list1,list2,list3])
print(arr_list_3)
print("\n")
print(arr_list_3.ndim)
print("\n")
print()

arr1=np.array([[1,2,3,],[4,5,6]])
print(arr1)

print("Shaped: ",arr1.shape)
print("Size: ",arr1.size)
print("Dtype: ",arr1.dtype)
print("dimansion: ",arr1.ndim)
print("\n")

zeros_arr=np.zeros((2,3))
print(zeros_arr)
print("\n")

ones_arr=np.ones((1,3))
print(ones_arr)
print("\n")

full_arr=np.full((3,4),11)
print(full_arr)
print("\n")

id_arr=np.eye(4)
print(id_arr)
print("\n")  

print(np.empty(2))
print("\n")
# evenly spaced array
print(np.arange(1,10,2))# it print number from 1 to 10 and skip very 2 number
print("\n")

#spacific number of equally values between a range
print(np.linspace(1,10,4))# it print number from 1 to 10 in linear but skip every 3rd value evenly*
print("\n")

# random values array
r_arr=np.random.rand(3,2)# this is flaoting array/matrix
print(r_arr)
print("\n")

rint_arr=np.random.randint(1,100,(3,3))# generete random number from 1 to 100 and size of array\matrix is 3 row and 3 column
print(rint_arr)
print("\n")

# array indexing and slicing
a=np.array([1,3,5,7,9])
print(a[0])
print("\n")
print(a[4])
print("\n")
print(a[-1])
print("\n")
a=np.array([1,3,5,7,9])
print(a)
print("\n")
#slicing
#array [start:stop:step] basic syntax (1d)
print(a[0:3])# first three elements
print("\n")
print(a[-3:])#last three elements
print("\n")
print(a[1:4])# middel three elements 
print("\n")
print(a[0:4:2])# it 0 4 and 2, 0 and 4 is indexing and 2 is step value maens it skip every 2nd elements
print("\n")
# indexing in 2d array/matrix
arr2=np.array([[1,2,3],[4,5,6]])
print(arr2)
print("\n")
print(arr2[1][0])
print("\n")
# slicing in 2d array/matrix group of elements
print(arr2[1:])# sliicng
print("\n")
print(arr2)
print("\n")
print(arr2[:,2])# it print index number 2 column
#         [1,2,3]
#         [4,5,6]
#              ^ like this    
print("\n")
#2d [row,column]
#3d [height/layers,rows.column]
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
print(arr3[0][2])
print(arr3[2][2])
print("\n")
print(arr3[:,0])# 0th row 1st column
print(arr3[:,2])# 0th row 3rd column
print("\n")
# value jump
print(arr3[0::2,0])# ::2,0 (2) means skip every 2nd element in 0th column
print("\n")
# column sliicng 
print(arr3[0:,1:2])# pick every rows one element but only in column 1
# 0 means pick every row from index 0 to 2 (all three row) and , coma maens stop and 1 [:] colon 2, means pick column from 1 to 2 but because last
# index value is not included (exclusive) so it now have to pick 1st index column and it print it
print("\n")
# array reshaping and flattening
arr1=np.array([1,2,3,4,5])
print(arr1)
print("\n")
reshaped=arr1.reshape((5,1))
print(reshaped)# it convert row in column and column in row thid is 5 row 1 colum array/matrix











