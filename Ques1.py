list = [10,20,30,(40,50),60]
a=0
for i in list:  
    if isinstance(i,tuple):
        break
    a+=1 
print(a)