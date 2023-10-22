def add():
    print("add",)

def modify():
    print("modify")
    
def delete():
    print("delete")

opr = int(input("Enter options:"))
match opr:
    case 1:
        add()
    case 2:
        modify()
    case 3:
        delete()
    case _:
        print("You are finished")