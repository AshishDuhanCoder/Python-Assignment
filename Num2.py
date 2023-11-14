#1 Create a list, accept 5 numbers , store them in the list and finally convert that list to numpy array.

""" import numpy as np
a=[int(input("Enter number: ")) for i in range(1,6)]
print(a)
num = np.array(a)
print(num) """


#2 Create numpy array of 5 numbers and print their sum
'''
import numpy as np
a=np.array([1,2,3,4,5])
print(sum(a))
'''

#3 create numpy double dimension array of 3*3 to store your initial and display them in a tabular form.

""" import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a) """

#4 create one-d numpy array of 12 elements , accept 12 numbers and display them.
#  Now convert this one-d array into (4*3) two-d array and display it in a tabular form.
""" 
import numpy as np
a=[int(input("Enter 12 numbers: ")) for i in range(1,13)]
print(np.array(a))
b=np.reshape(a,(4,3))
print(b)
"""

#5 create two double dimension array and arrange (stack) them using "axis=0" "axis=1" and  "axis=2".
""" 
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
a1=np.array([[7,8,9],[10,11,12]])
b=np.stack((a,a1),axis=0)
print(b)
print("############################################")
c=np.stack((a,a1),axis=1)
print(c)
print("############################################")
d=np.stack((a,a1),axis=2)
print(d)
 """
 
#6 create two one-d arrays and then find out:
	#a) common elements of both the array
	#b) unique elements of first array
	#c) unique elements of second array
'''
import numpy as np
a=np.array([1,2,3,4,5])
b=np.array([5,4,2,8,9])
common=np.intersect1d(a,b)
print(common)
unq=np.unique(np.concatenate((a,b)))
print(unq)
'''

#7 accept no.of rows and no. of cols from the user , create two-d array accordingly. 
#  Now calculate the sum as per "axis=0" and "axis=1"
""" 
import numpy as np
list=[]
print("No. of Rows")
a=int(input())
print("No. of Columns")
b=int(input())
print("Enter",a*b," values")
for i in range(1,(a*b)+1):
    num=int(input())
    list.append(num)
c=np.array([list])
print(c)
print("#######################")
e=c.reshape(a,b)
print(e)
print("#######################")
d=np.stack(e,axis=0)
print(d)
print("#######################")
f=np.sum(d)
print(f)
print("#######################")
g=np.stack(e,axis=1)
print(g)
"""

#8 declare two 2d arrays and calculate the sum as per "axis=0" "axis=1" and "axis=2"
""" 
import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8]])
b=np.array([[10,20,30,40],[50,60,70,80]])
c=np.sum((a,b),axis=0)
print(c)
print("###############################")
d=np.sum((a,b),axis=1)
print(d)
print("\n")
e=np.sum((a,b),axis=2)
print(e)
print("\n")
f=np.stack((a,b),axis=2)
print(f)
"""
 
#9 create two-d array ,display it.Now accept a number from user and perform all arithmetic 
#  operations on each and every element of the array using that number.
""" import numpy as np
a=np.array([[1,2,3],[4,5,6]])
a.flags.writeable = False
print(a)
print("\n")
b=a+2
print(b)
print("\n")
c=a*b
print(c)
 """
 
#10 accept start, end and how many numbers to be generated and then using "linspace" create numpy array.
""" import numpy as np
a=np.array(np.linspace(1,8,num=12))
print(a) """


#11 create one-d array of 8 numbers and then using "slicing" concept,
	# a) print numbers from 1 to 4
	# b) print all the numbers from 3rd position
	# c) print last 3 numbers
"""  
import numpy as np
a=np.array([1,2,3,4,5,6,7,8])
print(a[0:4])
print(a[2:])
print(a[-3:])
 """
 
 
#12 create 2 d array (4*3) with following values:
# [[10,20,30,40],[50,60,70,80],[90,100,110,120]]

# now using array slicing concept display following values
# 	a) display   50  60  70  80
# 	b) display 100 and 110
# 	c) display 30 70 and 110
# 	d) display 50  60  90 and 100

import numpy as np
a=np.array([[10,20,30,40],[50,60,70,80],[90,100,110,120]])
b=np.reshape(a,(4,3))
print(b)
print('\n')
print(a[1:2])
for i in range(1,2):
    for j in range(0,a[i].__len__()):
        print(a[i][j],"\t",end="")
    print("\n")
for i in range(2,a.__len__()):
    for j in range(0,a[i].__len__()):
        print(a[i][j],"\t",end="")
    print("\n")
