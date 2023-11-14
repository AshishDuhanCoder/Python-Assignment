#7) create "Vita.xlsx" using pandas. In this Excel file you have to create 2 sheets "DBDA", and "DAC". 
#   in each sheet you have to write name,address and age of all the team leaders.
#   make sure Excel file gets created successfully.
from pandas import *
proid = [1,2,3,4]
proname = ["Soap","Perfume","Deo","Body_Wash"]
price = [120,400,250,180]
dict1={'proid':proid,'proname':proname,'price':price}
frame1=DataFrame(dict1)
name=['Abc','Xyz','Pqr']
designation=['officer','manager','salesexecutive']
salary=[40000,60000,70000]
dict2={'name':name,'designation':designation,'salary':salary}
frame2=DataFrame(dict2)
print(frame1)
print("\n\n")
print(frame2)
with ExcelWriter('Vita.xlsx') as mywriter:
    frame1.to_excel(mywriter,sheet_name="Dbda",index=False)
    frame2.to_excel(mywriter,sheet_name="Dac",index=False)