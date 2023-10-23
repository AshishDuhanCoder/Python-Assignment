def fun1():
    print("Outer function")
    def fun2():
        print("Inner function")
    return fun2()
fun1()