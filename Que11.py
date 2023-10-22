user = int(input("Enter a number: "))
for i in range(2,user):
    if user%i==0:
        print(user,"Number is not prime")
        break
    
else:
    print(user,"Number is not prime")