import numpy as np

list1=[1,2,3]

print(list1)
print("\n")

arr_list1=np.array(list1)
print(arr_list1)
print("\n")
print(type(arr_list1))
print(arr_list1.ndim)
print("\n")
list1=([1,2,3])
list2=([4,5,6])
arr_list_2=np.array([list1,list2])
print(arr_list_2)
print(arr_list_2.ndim)
print("\n")
list1=np.array([1,2,3])
list2=np.array([4,5,6])
list3=np.array([7,8,9])
arr_list_3=np.array([[list1,list2,list3]])
print(arr_list_3)
print("\n")
print(arr_list_3.ndim)
print("\n")
# numpy array attributes
arr1=np.array([[1,2,3],[3,4,5]])
print(arr1)
print("\n")
print("Shape",arr1.shape)# for shape of array (2,3)
print("Size",arr1.size)# size of array (6) elements
print("Dtype",arr1.dtype)# data type
print("Ndim",arr1.ndim)# N-dimansion
print("\n")
# array initialization methods
zeros_arr=np.zeros((2,3))
print(zeros_arr)
print("\n")
ones_arr=np.ones((2,3))
print(ones_arr)
print("\n")
# full array
full_arr=np.full((3,2),11)# custom elements array
print(full_arr)
print("\n")
# identity matrix 
id_arr=np.eye(3)# it create array and print 1 in daigonally
print(id_arr)
print("\n")
# empty array
print(np.empty(2))
print("\n")
print("\n")
# evenly spaced array
print(np.arange(1,10,2))# it print from 1 to 10 but skip every 2nd element
print("\n")
#spacific number of equally spaced values between a range
print(np.linspace(1,10,4))# it separate value between 1 to 10 evenly in 4 part
print("\n")
# random values array/matrix
r_arr=np.random.rand(3,2)
print(r_arr)
print("\n")
rint_arr=np.random.randint(1,100,(3,3))
print(rint_arr)
print("\n")
# array indexing and slicing (1d)
a=np.array([1,3,5,7,9])
print(a)
print("\n")
print(a[0])
print("\n")
print(a[4])
print("\n")
print(a[-1])
print("\n")
# array slicing [start:stop:step]
# stop index is not included (exclusive)
a=np.array([1,3,5,7,9])
print(a)
print("\n")
print(a[0:3])# first three elements 
print("\n")
print(a[-3:])# last three elements
print("\n")
print(a[1:4])# middle three elements
print("\n")
print(a[0:4:2])# [0:4:2] print value from index number 0 to 4 but skip every 2nd elements, result (1 5)
print(a[1:4])# middle three elements
print("\n")
print(a[0::2])# means start from index 0 and [:] colon and stop index, and [:] colon means step index or value
print("\n")
#indexing and slicing in array/matrix (2d)
arr2=np.array([[1,2,3],
               [4,5,6]])
print(arr2)
print("\n")
print(arr2[1][0])# 1 means index number 1 row and 0 means 0 index column, result (4)
print("\n")
# sliicng
print(arr2[1])# means print whole index number 1 row
print("\n")
print(arr2[1:])# means print index number 1 row and [:] means print whole remaining values
print("\n")
print(arr2)
print("\n")
print(arr2[:,2])# [:,2] print whole row but only in index number 2 column result (3 6)
print("\n")
# 2d [rows, columns]
# 3d [height, rows, columns]

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
print(arr3[:,2])# it pick every row and only index number 2 column so it print index number 2 column (last column)
print("\n")
print(arr3[::2,0])# it print whole row but skip every 2nd element in index number 0 column (first column) result (1 7)
print("\n")
print(arr3[::, 1:2])# [::] means print all rows and [,] means stop and 1 [:] colon 2 means print column 1 to 2 but because last
# index in not included (exclusive) it print index number 1 column only
print("\n")
#array reshaping and flattening
arr1=np.array([1,2,3,4,5,6])
print(arr1)
print("\n")

reshaped=arr1.reshape((6,1))# it reshaped array column in rows and rows in column (2d)
print(reshaped)
print("\n")
reshaped2=arr1.reshape((2,3))
print(reshaped2)
print("\n")
# falttening
print(reshaped2.flatten())# convert 2d array in 1d
print("\n")
# array stacking and splitting
a=np.array([1,2,3])
b=np.array([4,5,6])
print("\n")
print(np.vstack((a,b)))# vertical stacking (2d)
print("\n")
print(np.hstack((a,b)))# horizontal stacking (1d)
print("\n")
# splitting 
c=np.array([[1,2,3],[4,5,6]])
print(c)
print("\n")

hsplit=np.hsplit(c,3)# horizontal split (2d)
for s in hsplit:
    print(s)
print("\n")

vsplit=np.vsplit(c,2) # vertical split (2d)
for s in vsplit:
    print(s)
print("\n")

# mathematical operations on array (1d)
a=np.array([10,20,40,-30])
print(a)
print("\n")

print(a+10)# add 10, [20,30,50,-20]
print(a-30)# subtract -30 [-20,-10,-10-60]
print(a*2)# multiply by 2 [20,40,80,-60]
print(a/10)# divide by 10 [1,2,4,-3]
print("\n")

b=np.array([1,4,9])
print(b)
print("\n")
print(np.square(b))# square 
print(np.sqrt(b))# square root   
print("\n")
# methematical operations on array/matrix (2d)
a=np.array([1,2,3])
b=np.array([4,5,6])
print(a)
print(b)
print("\n")

print(np.add(a,b))# addition 1+4 is 5, 2+5 is 7, 3+6 is 9
print(np.subtract(a,b))# subtract 1-4 is -3, 2-5 is -3, 3-6 is -3
print(np.multiply(a,b))# multiply 1*4 is 4, 2*5 is 10, 3*6 is 18
print(np.divide(a,b))# divide 0.25, 0.4, 0.5,
print("\n")
# dot product
print(np.dot(a,b))# it multiply and add all elements in one unit like 1*4 is 4, 2*5 is 10 and 3*6 is 18 and now it all this. result (32)
print("\n")
# transpose
t=np.array([[1,2,3],[4,5,6]])
print(t)
print("\n")
print(t.T)# it convert rows in column and column in rows daigonally
print("\n")
# statistical functions 
a=np.array([[1,2,3],[4,5,6]])
print(a)
print("\n")
print(np.mean(a))# average value between 1 to 6 [3.5]
print(np.median(a))# middle average value between 1 to 6 [3.5]
print(np.std(a))# close to middle average value or far
print(np.min(a))# minimun value in array/matrix [1]
print(np.max(a))# maximum value in array/matrix 6
print("\n")

# array comparison
a=np.array([1,5,3])
b=np.array([4,5,6])
print(a)
print(b)
print("\n")

print(a==b)# comparing each element 
print("\n")
print(np.array_equal(a,b))# comparing complete array
print("\n")
# broadcasting 
a=np.array([1,2,3,4])
b=np.array([5])
print(a+b)
print("\n")
c=np.array([[1,2,3],[4,5,6]])
d=np.array([10,20,30])
print(c+d)# it add 10 in 1 so it 11, and 20 in 2 so it 22, and 30 in 3, it's 33 and same for next row
#result [11,22,33] in 0 index row and [14,25,36] for 1 index row, no element will repeat maintening higher dimansion array/matrix
print("\n")
# handling with nan values and inf
data1=np.array([1,2,np.nan,4,np.inf])
print(data1)
print("\n")
print(np.isnan(data1))# to check nan value in array
print("\n")
print(np.nan_to_num(data1))# it replace nan value with 0
print("\n")
# save and load arrays
arr=np.array([2,0,3,6])
print(arr)
print("\n")
np.save('1st_may_my_arr.npy',arr)

# load arrays
loaded_arr=np.load('1st_may_my_arr.npy')
print(loaded_arr)