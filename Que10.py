for i in range(3,30):
    if i>1:
        for j in range(2,i):
            if(i%j)==0:
                break
        else:
            print(i)