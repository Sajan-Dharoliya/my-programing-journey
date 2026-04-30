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
# array indexing and slicing
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
print(a[0:4:2])# [0:4:2] print value from index number 0 to 4 but skip every 2 and elements, result (1 5)
print(a[1:4])# middle three elements
print("\n")
print(a[0::2])# means start from index 0 and [:] colon and stop index, and [:] colon means step index or value