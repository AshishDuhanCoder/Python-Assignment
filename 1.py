'''
def square():
    a = int(input("Enter a Number: "))
    print(a*a)
square()
'''
a=int(input("Enter a Number: "))
square = lambda a: a*a
print(square(a))