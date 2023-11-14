#1
""" import pandas as pd
first = pd.Series([10,2.8,True,40,"Ashish"])
print(first)
print("\n")
print(first.index)
print("\n")
print(first.values) """

#2 accept input
"""  
from pandas import *

mylist=[]
print("enter values, 0 to exit")
while True:
    val=int(input())
    if(val==0):
        break
    mylist.append(val)
myseries=Series(mylist)
print(myseries)
 """

#3 create panda series using tuple
""" 
from pandas import *

mytuple=(100,200,300,400,500)
myseries=Series(mytuple)
print(myseries)
 """
 
#4 if you don't want to print index
""" 
import pandas as pd

first=pd.Series([10,20,30,40,50])
print(first)
print("*************")
print(first.to_string(index=False))
 """
 
#5 We can change the labels or indexes
""" 
from pandas import *

first=Series([10,20,30,40,50],index=['p','q','r','s','t'])
print(first)
 """
 
#6 extract DataFrame columns randomly
""" 
from pandas import *

mydataframe=DataFrame({"proid":range(5,9),"proname":['soap','perfume','deo','powder'],"price":[120,400,280,160]})
print(mydataframe)
print("\n")
mylist=mydataframe.values.tolist()                # extract all rows
print(mylist)
print("\n\n")
mylist=mydataframe.iloc[:,[0,2]].values.tolist()    #  extract all rows of 0 and 2nd columns ( by skipping 1st column)
print(mylist)
 """
 
#7 extract DataFrame columns randomly
""" 
from pandas import *

mydataframe=DataFrame({"proid":range(5,9),"proname":['soap','perfume','deo','powder'],"price":[120,400,280,160]})
print(mydataframe)
print("\n\n")
mylist=mydataframe.values.tolist()                # extract all rows
print(mylist)
print("\n\n")
mylist=mydataframe.iloc[[1,3],[0,2]].values.tolist()    #  extract row no. 1 and 3 of 0 and 2nd columns
print(mylist)
 """
 
#8 difference between tradional reading and pandas way of reading
""" 
from pandas import *

myfile=read_json("details.json")
mydataframe=DataFrame(myfile)
print(mydataframe)
print("\n\n")
print("let's us read the file in a tradional way")
f=open("details.json","r")
for content in f:
	print(content)
f.close()
print("Done")
 """
 
#9  For this to work , you need to install "xlrd"

# pip install xlrd
""" 
import pandas as pd
mydataframe1 = pd.read_excel('ForPandas.xls')
 
print(mydataframe1)

print("\n\nLet's print Sheet2")
mydataframe1 = pd.read_excel('ForPandas.xls',sheet_name='Sheet2')
print(mydataframe1)
 """

#10 
""" 
import pandas as pd 
proid = [1,2,3,4]
proname = ["Soap","Perfume","Deo","Body_Wash"]
price = [120,400,250,180]
 
# dictionary of lists
mydictionary = {'proid':proid,'proname':proname,'price':price}
     
mydataframe = pd.DataFrame(mydictionary)
 
print(mydataframe)
mydataframe.to_csv("prod.csv")
mydataframe.to_json("prod.json")
 """

#11 # pip install openpyxl
# pip install xlwt    # try not installing this
""" 
import pandas as pd
 
proid = [1,2,3,4]
proname = ["Soap","Perfume","Deo","Body_Wash"]
price = [120,400,250,180]
 
# dictionary of lists
mydictionary = {'proid':proid,'proname':proname,'price':price}
     
mydataframe = pd.DataFrame(mydictionary)
 
print(mydataframe)
# index=False   is not to include dataframe index inside the excel file
mydataframe.to_excel("prod.xlsx",sheet_name="prod_sheet",index=False)
 """
 
#12 pip install openpyxl

# The ExcelWriter object allows you to use multiple pandas. DataFrame objects can be exported to separate sheets.
""" 
import pandas as pd
 
proid = [1,2,3,4]
proname = ["Soap","Perfume","Deo","Body_Wash"]
price = [120,400,250,180]
 
# dictionary of lists
mydictionary1 = {'proid':proid,'proname':proname,'price':price}
     
mydataframe1 = pd.DataFrame(mydictionary1)
 
name=['Abc','Xyz','Pqr']
designation=['officer','manager','salesexecutive']
salary=[40000,60000,70000]

mydictionary2={'name':name,'designation':designation,'salary':salary}

mydataframe2=pd.DataFrame(mydictionary2)

print(mydataframe1)
print("\n\n")
print(mydataframe2)

mydataframe1.to_excel("prod2.xlsx",sheet_name="prod_sheet",index=False)

mydataframe2.to_excel("prod2.xlsx",sheet_name="employee_sheet",index=False) # this will overwrite previous sheet
 """
 
#13 # pip install openpyxl
# pip install xlwt    # try not installing this
# The ExcelWriter object allows you to use multiple pandas. DataFrame objects can be exported to separate sheets.
""" 
import pandas as pd
 
proid = [1,2,3,4]
proname = ["Soap","Perfume","Deo","Body_Wash"]
price = [120,400,250,180]
 
# dictionary of lists
mydictionary1 = {'proid':proid,'proname':proname,'price':price}
     
mydataframe1 = pd.DataFrame(mydictionary1)
 
name=['Abc','Xyz','Pqr']
designation=['officer','manager','salesexecutive']
salary=[40000,60000,70000]

mydictionary2={'name':name,'designation':designation,'salary':salary}

mydataframe2=pd.DataFrame(mydictionary2)

print(mydataframe1)
print("\n\n")
print(mydataframe2)

mydataframe1.to_excel("prod2.xlsx",sheet_name="prod_sheet",index=False)
input()  #  just to check what happens with the previous "to_excel()" function
mydataframe2.to_excel("prod2.xlsx",sheet_name="employee_sheet",index=False) # this will overwrite previous sheet
 """
 
#14
# pip install openpyxl
# pip install xlwt    # try not installing this
# The ExcelWriter object allows you to use multiple pandas. DataFrame objects can be exported to separate sheets.
""" 
import pandas as pd
 
proid = [1,2,3,4]
proname = ["Soap","Perfume","Deo","Body_Wash"]
price = [120,400,250,180]
 
# dictionary of lists
mydictionary1 = {'proid':proid,'proname':proname,'price':price}
     
mydataframe1 = pd.DataFrame(mydictionary1)
 


name=['Abc','Xyz','Pqr']
designation=['officer','manager','salesexecutive']
salary=[40000,60000,70000]

mydictionary2={'name':name,'designation':designation,'salary':salary}

mydataframe2=pd.DataFrame(mydictionary2)

print(mydataframe1)
print("\n\n")
print(mydataframe2)

with pd.ExcelWriter('Prod1.xlsx') as mywriter:
    mydataframe1.to_excel(mywriter, sheet_name='prod_sheet',index=False)
    mydataframe2.to_excel(mywriter, sheet_name='employee_sheet',index=False)
 """
 