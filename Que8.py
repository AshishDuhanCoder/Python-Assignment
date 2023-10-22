'''
user = ord(input("Enter an Alphabet"))
if ord('A')<=user<=ord('Z'):
    print("up")
elif ord('a')<=user<=ord('z'):
    print("lower")
else:
    print("invalid")
'''

#or
 
user = input("Enter an Alphabet: ")
if 'A'<=user<='Z':
    print("up")
elif 'a'<=user<='z':
    print("lower")
else:
    print("invalid")