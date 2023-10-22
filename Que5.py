a=int(input("Enter a Number: "))
if(a>33):
    print("pass")
    if(50<a<60):
        print("second class")
    elif(60<a<100):
        print("first class")
elif(0<a<33):
    print("fail")
else:
    print("distinction")