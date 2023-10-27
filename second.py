list = []
a=1
while(a!=0):
    a = int(input("Enter number till user enter zero: "))
    if(a!=0):
        list.append(a)
        print(list)

print(list)
print(len(list))