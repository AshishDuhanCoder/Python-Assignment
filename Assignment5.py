# accept 5 names,designations and salaries and display them with DataFrame.

import pandas as pd
a={} 
for i in range(5):
    name=input("Enter names: ")
    designation=input("Enter Designation: ")
    salaries=int(input("Enter Salaries: "))
    a[name] = designation,salaries
b=pd.DataFrame(a,index=False)
print(b)