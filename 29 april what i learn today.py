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
arr1=np.array([1,2,3,4,5,6])
print(arr1)
print("\n")
reshaped=arr1.reshape((6,1))
print(reshaped)# it convert row in column and column in row thid is 5 row 1 colum array/matrix
print("\n")

reshaped2=arr1.reshape((2,3))
print(reshaped2)
print("\n")
# flatten
print(reshaped2.flatten())# now it become 1d
print("\n")
#array stacking and splitting
a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.vstack((a,b)))# now it become 2d array/matrix
print("\n")
print(np.hstack((a,b)))
print("\n")
# horizontal split
c=np.array([[1,2,3],[4,5,6]])
print(c)
print("\n")

hsplit=np.hsplit(c,3)
for s in  hsplit:# horizontal split
    print(s)
print("\n")

vsplit=np.vsplit(c,2)# vertical split
for s in vsplit:
    print(s)
print("\n")
# mathematical operation on array/matrix (1d)
a=np.array([10,20,40,-30])
print(a)
print("\n")
print(a+10)
print(a-30)
print(a*2)
print(a/10)
print("\n")

b =np.array([1,4,9])
print(b)
print("\n")
print(np.square(b))# for square
print(np.sqrt(b))# for square root
print("\n")
# mathematical operation on multiple array/matrix (2d)

a=np.array([1,2,3])
b=np.array([4,5,6])
print(a)
print(b)
print("\n")
print(np.add(a,b))# addition [5,7,9]
print(np.subtract(a,b))# subtract [-3,-3,-3]
print(np.multiply(a,b))# multiply [4,10,18]
print(np.divide(a,b))# divide [0.25,0.4,0.5]
print("\n")
# dot product
print(np.dot(a,b))# it simply add all elements value in single unit,
# like 1*4 is (4), 2*5 is (10), 3*6 is (18) so now add all this, the result will be 32
print("\n")
# transpose
t=np.array([[1,2,3],
            [4,5,6]])
print(t)
print("\n")
print(t.T)# it flip row in column and column in row diagonally 
print("\n")
# statistical function
a=np.array([[1,2,3],[4,5,6]])
print(a)
print("\n")
print(np.sum(a))
print("\n")

print(np.mean(a))# average value between 1 to 6 (3.5)
print(np.median(a))# middle average value between 1 to 6 (3.5)
print(np.std(a))# close to middle value or far
print(np.min(a))# minimum value in array/matrix 1
print(np.max(a))# maximum value in array/matrix 6
print("\n")
# array comparison 
a=np.array([1,5,3])
b=np.array([4,5,6])
print(a)
print(b)
print("\n")

print(a==b)# comparing each elements 
print(np.array_equal(a,b))# compare elements like 1=4 is false, 5=5 is true, 3=6 is false
print("\n")

# broodcasting
a=np.array([1,2,3,4])
b=np.array([5])
print(a+b)
print("\n")

c=np.array([[1,2,3],[4,5,6]])
d=np.array([10,20,30])# it maintained higher dimansion array in with lower dimansion array
print(c+d)# like it first add 10 in 1 so it's 11 and 20 in 2 is 22 and 30 in 3 is 33 and next column 10 in 4 is 14 and 20 in 5 is 25 and 30 in 6 is 36
print("\n")
# handling with nan value

data1=np.array([1,2,np.nan,4,np.inf])
print(data1)
print("\n")
print(np.isnan(data1))# checking nan value
print("\n")
print(np.nan_to_num(data1))# it replece nan value to 0 
print("\n")
# save and load array
arr=np.array([1,2,3])
print(arr)
print("\n")
np.save('my array.npy',arr)
# load
loaded_arr=np.load('my array.npy')
print(loaded_arr)









