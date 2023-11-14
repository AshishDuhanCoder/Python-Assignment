#1
'''
import numpy as np
first=np.array([100,200,300,400])
print(first)
for i in range(0,first.__len__()):
    print(first[i])
print(type(first))
print("dimension of array is\t",first.ndim)
print("\n")
print("shape of array is\t",first.shape)
'''

#2
'''
import numpy as k
#indexing in numpy array

arr1=k.array([10,20,30,40])
print(arr1)
print(arr1[0])
print(arr1[-1])
print("from the begining")
for i in range(0,arr1.__len__()):
    print(arr1[i])
print("from the end")
for i in range(-1,-(arr1.__len__()+1),-1):
    print(arr1[i])
'''

#3
'''
# initialize one-d and 2d array  with one  

import numpy as np
first=np.ones((1,4))                             # one row , 4 columns

print(first)
print("\n")

# initialize two-d array with zeros

second=np.ones((3,4))                            # 3 rows and 4 columns

print(second)
'''

#4
'''
#  2 d arrays stack with 0 ,1 and 2 axis
# here stack will create 3d array

import numpy as np
first=np.array([[1,2,3],[4,5,6]])
second=np.array([[7,8,9],[10,11,12]])
third=np.stack((first,second),axis=0)
print(third)
print("###############################################")
""" [[[ 1  2  3]  
     [ 4  5  6]] 

    [[ 7  8  9]  
     [10 11 12]]] """

fourth=np.stack((first,second),axis=1)
print(fourth)
print("##############################################################")
""" [[[ 1  2  3]  
     [ 7  8  9]] 

    [[ 4  5  6]  
     [10 11 12]]] """

fifth=np.stack((first,second),axis=2)
print(fifth)
print("################################################")
""" [[[ 1  7]     
  [ 2  8]     
  [ 3  9]]

 [[ 4 10]
  [ 5 11]
  [ 6 12]]] """

""" #numpy.AxisError: axis 3 is out of bounds for array of dimension 3
sixth=np.stack((first,second),axis=3)
print(sixth) """
'''

#5
'''
#  1 d arrays stack with 0 and 1 axis
# here stack will create 2d array

import numpy as np
first=np.array([4,5,8,12,15])
second=np.array([11,15,4,8,9])
third=np.stack((first,second),axis=0)
print(third)
""" [[ 4  5  8 12 15] 
     [11 15  4  8  9]] """
fourth=np.stack((first,second),axis=2)
print(fourth)
fourth.shape=(2,5)
print(fourth)

""" [[ 4 11] 
     [ 5 15] 
     [ 8  4] 
     [12  8] 
     [15  9]] """

""" fifth=np.stack((first,second),axis=2) # numpy.AxisError: axis 2 is out of bounds for array of dimension 2
print(fifth) """
'''

#6
'''
# axis=0  column-wise sum
# axis=1  row-wise sum

import numpy as k
arr=k.array([[1,2,3,4],
             [2,3,4,5],
             [7,8,9,10]])     
arr1=k.sum(arr,axis=1)   # row-wise total
# 1+2+3+4   2+3+4+5   7+8+9+10
print(arr1)
arr2=k.sum(arr,axis=0)  # column-wise total
# 1+2+7     2+3+8     3+4+9     4+5+10
print(arr2)


"""

output:

[10 14 34]
[10 13 16 19]

"""
'''

#7
'''
import numpy as np

fourth=np.array([[10,20,30],[40,50,60]])
fifth=np.array([[70,80,90],[100,110,120]])
#fourth.shape=(2,3)
print(fourth)
print("#################")
print("#################")
print(fifth)
print("#################")
print("#################")
sixth=np.sum((fourth,fifth),axis=0)  
print(sixth)
""" [[ 80 100 120] 
     [140 160 180]] """
print("\n")
eighth=np.sum((fourth,fifth),axis=1)
print(eighth)
""" [[ 50  70  90] 
 [170 190 210]] """
print()
ninth=np.sum((fourth,fifth),axis=2)
print(ninth)
""" [[ 60 150]     
 [240 330]] """ 
'''
 
 #8
''' 
import numpy as np
 
a = np.array([12, 15, 10, 1])
print("Array before sorting",a)
a.sort()
print("Array after sorting",a)
'''

#9
'''
import numpy as np
# sort without any axis

a = np.array([[12, 25], [30, 18]])
arr1 = np.sort(a, axis = None)       
print ("\nAlong None axis : \n", arr1)

# sort along the first axis
a = np.array([[12, 25], [30, 18]])
arr1 = np.sort(a, axis = 0)       
print ("Along 0 axis : \n", arr1)       
 
a = np.array([[12, 25], [30, 18]])
arr1 = np.sort(a, axis = 1)       
print ("\nAlong 1 axis : \n", arr1)

print("Reverse order column-wise\n")
arr1=-np.sort(-a,axis=0)
print(arr1)
print("Reverse order row-wise\n")
arr1=-np.sort(-a,axis=1)
print(arr1)
print("****************")
myar=np.array([[[10,20,30],[4,50,6]],[[70,8,90],[65,110,12]]])
print(myar)
print("Ascending order 3d array column-wise")
"""
10 will be compared with 70, 20 will be with 8, 30 will be with 90
4 will be with 65, 50 will be with 110, 6 will be with 12
"""
arr1=np.sort(myar,axis=0)
print(arr1)
print("Ascending order 3d array row-wise")
""" 10 will be compared with 4, 20 will be with 50, 30 will be compared with 6
70 will be compared with 65, 8 will be compared with 110, 90 will be compared with 12"""
arr1=np.sort(myar,axis=1)
print(arr1)
print("Reverse order 3d array column-wise\n")
arr1=-np.sort(-myar,axis=0)
print(arr1)
print("Reverse order 3d array row-wise\n")
"""
10 will be compared with 4, 20 with 50, 30 with 6
70 with 65, 8 with 110,  90 with 12
"""
arr1=-np.sort(-myar,axis=1)
print(arr1)
'''

#9
'''
import numpy as np

arr = np.array([5,8,9,11,12,16])
print(arr)
print(arr[[True,False,True,False,True,False]])
'''

#10
'''
import numpy as np

arr = np.array([5,8,9,11,12,16])
print(arr)

print(arr%4==0)  #  it prints  [False  True False False  True  True]

print(arr[(arr%4==0)]) # it's like arr[[False  True False False  True  True]]

print(arr[(arr>=9) & (arr<=15)])

print(arr[(arr%3==0) | (arr%11==0)])

#filter for values that are equal to 2, 3, 5, or 12
print(np.in1d(arr,[2, 3, 5, 12]))
print("*****************")

print(arr[np.in1d(arr,[2, 3, 5, 12])])
'''

#11
'''
# Using mask

import numpy as np
 
# making a numpy array
array1 = np.array([num for num in range(10, 50,5)])
 
print("Original array")
print(array1)
 
# defining mask based on two conditions:
# array element must be greater than 22
# and must be a divisible by 2
mask = (array1 > 22) & (array1 % 2 == 0)
 
# making new array on conditions
array2 = array1[mask]
print("New array")
print(array2)
'''

#12
'''
# Using iterative method

import numpy as np
 
# making a numpy array
array1 = np.array([x for x in range(11, 40)])
 
print("Original array")
print(array1)
 
# making a blank list
mylist = []
 
for x in array1:
    # applying two conditions: number is divisible by 2 and is greater than 15
    if x % 2 == 0 and x > 15:
       mylist.append(x)
 
# Converting new list into numpy array
array2 = np.array(mylist)
print("New array")
print(array2)
'''

#13
'''
import numpy as np

array1= np.arange(12).reshape(3,4)
print("original array is\n")
print(array1)
result = array1[array1 > 5]
print("Filter values from array:",result)
result1=array1[(array1<10) & (array1%3==0)]
print(result1)
'''

#14
'''
import numpy as np

# axis=0 works on all columns of 2d array , so first argument : indicates  all the rows

# axis=1 works on all rows of 2d array, so second argument : indicates all the columns

a = np.arange(12).reshape((3, 4))
print(a)
print("***************")
"""
np.all() method return True if all the values fulfills the condition. 
This return value maps with the original array to give the filtered values
"""
print(a[:, np.all(a < 10, axis = 0)])
print("*********************")
""" np.any() method return true if any of the values fulfill the condition. 
 This return value maps with the original array to give the filtered values. """
print(a[:,np.any(a < 10, axis = 0)])
print("*******************")
print(a[:,np.any(a > 8, axis = 0)])
print("**************************")
print(a[np.any(a < 10, axis = 1),:])
print("**************************")
print(a[np.all(a < 10, axis = 1),:])
'''

#13

# numpy array elements are mutable but numpy as an object is immutable
# first+1  creates a new numpy object in which changes can be seen

import numpy as np


first=np.array([10,20,30])
print(first,"\t",id(first))
second=first+1      #  this is like immutable
first[0]=34         # mutable array
print(first,"\t",id(first))
print(second,"\t",id(second))

# how to make numpy array read only
import numpy as np


first=np.array([10,20,30])
first.flags.writeable = False
print(first,"\t",id(first))
second=first+1      #  no problem here
# first[0]=34         # ValueError: assignment destination is read-only
print(first,"\t",id(first))
print(second,"\t",id(second))