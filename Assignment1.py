# 1) store marks of 5 subjects
# 	here use marks as actual data and subject names as indexes.
#     accept both marks and subjects from the user.

import pandas as pd
data={}
for i in range(5):
    subject=input("Enter subject name: ")
    marks=int(input("Enter marks: "))
    data[subject]=marks
dict=pd.Series(data)
print(dict)