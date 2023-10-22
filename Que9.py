num = 10
num1 = 0
num2 = 1
fibonacci = num2
count = 1
while count<=num:
    print(fibonacci, end =" ")
    count +=1
    num1,num2 = num2,fibonacci
    fibonacci = num1+num2
print()