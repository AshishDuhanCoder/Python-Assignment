user = input("Enter a Character: ")
match user:
    case 1:
        user = 'a'
        print("It is vowel")

    case 2:
        user = 'e'
        print("It is vowel")
        
    case 3:
        user = 'i'
        print("It is vowel")        
    case 4:
        user = 'o'
        print("It is vowel")
        
    case 5:
        user = 'u'
        print("It is vowel")
        
    case _:
        print("It is not Vowel")