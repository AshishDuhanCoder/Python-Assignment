# 3) accept 10 values and store them in the Series. Now perform following operations:
#     a) display the entire Series
#     b) extract 3rd element
#     c) extract elements from 4 to 7
#     d) extract elements from fourth last till the last element
#     e) extract first 3 elements
#     f) extract elements from the 5th position

import pandas as pd
a=[]
for i in range(10):
    b=int(input("Enter values: "))
    a.append(b)
c=pd.Series(a)
print(c)
print("\n")
print(c[3])
print("\n")
print(c[4:7].to_string(index=False))
print("\n")
print(c[-4:].to_string(index=False))
print("\n")
print(c[0:3].to_string(index=False))
print("\n")
print(c[5:].to_string(index=False))