"""
def disp(*vars):
	if(vars.__len__()==0):
		print("no argument passed")
	else:
		for k in vars:
			print(k)
def fun():
    disp("abc",200)
fun()


(lambda *n:[print(i) for i in n])(100,25,"ghgh",250)

"""
'''
def fun(*var):
    disp(var)

disp=lambda x:[print(i) for i in x]

fun(100,14,"fhgfh",48)
'''

(lambda *n: [print(i) for i in n])(190,"Duhan",32.5)