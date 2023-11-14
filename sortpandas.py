#1 Series object is a one-dimensional labelled or indexed  array
""" 
import pandas as pd

first=pd.Series([100,20,3,40,5])
print(first)
print("sorting Pandas values without indexes changed")
print(first.sort_values())
print("sorting Pandas values with indexes changed")
print(first.sort_values(ignore_index=True))
print("sorting in descending order ,Pandas values with indexes changed")
print(first.sort_values(ascending=False,ignore_index=True)) """

#2 DataFrame is a two dimensional labelled data structure
# DataFrame comprises of rows and columns
""" 
from pandas import *

mydict={"Name":['Sachin','Rahul','Anil'],"Age":[39,35,38]}
print(mydict)
mydataframe=DataFrame(mydict)
print(mydataframe)
print("Age-wise ascending sort")
print(mydataframe.sort_values(by="Age",ignore_index=True))
print("Age-wise descending sort")
print(mydataframe.sort_values(by="Age",ascending=False,ignore_index=True))
print("Name-wise ascending sort")
print(mydataframe.sort_values(by="Name",ignore_index=True))
print("Name-wise descending sort")
print(mydataframe.sort_values(by="Name",ascending=False,ignore_index=True))
 """
list=[10,45,34,23,67,35,23,23,23]
list1=[15,20,34,23,67,35,23,23,23]
list.append(90)
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.reverse()
print(list)
a=list.index(90)
print(a)
b=list.count(23)
print(b)
c=list.copy()
print(c)
d=list.insert(1,4)
print(d)
e=list.extend(list1)
print(e)