def fun(ch):
    if(ch.__len__()>2 & ch.__len__()<6):
        print("accept")
    else:
        print("reject")
ch = input("Enter Character: ")
fun(ch)
print(ch.lower())