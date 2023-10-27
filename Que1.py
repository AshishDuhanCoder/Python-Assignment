myset = set({})
for i in range(1,11):
    a=input("Acceptn 10 values: ")
    myset.add(a)
print(myset)
a=input("Accept one more values: ")
myset.update(a)
print(myset)