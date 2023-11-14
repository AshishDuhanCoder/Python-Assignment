# 4) accept 5 values in a Series and perform the following operations:
# 	a) display their sum
# 	b) add the value accepted from the user
# 	c) subtract the value accepted from the user
# 	d) multiply the value accepted from the user
# 	e) add the value accepted from the user

import pandas as pd
a=[]
for i in range(5):
    b=int(input("Enter 5 values: "))
    a.append(b)
c=pd.Series(a)
print(c)
print("\n")
d=c.sum()
print(d)
print("\n")
e=int(input("Enter a value: "))
f=c.add(e)
print(f)
print("\n")
g=int(input("Enter a value: "))
h=c.subtract(g)
print(h)
print("\n")
i=int(input("Enter a value: "))
print(c.multiply(i))
print("\n")
j=int(input("Enter a value: "))
print(c.divide(j))