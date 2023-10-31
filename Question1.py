class Sample:
    def __init__(self,data):
        self.data=data
    def __mul__(self,obj):
        return self.data*obj.data
    def __add__(self,obj):
        return self.data+obj.data
    def __sub__(self,obj):
        return self.data-obj.data
    
s1=Sample(7)
s2=Sample(5)
s3=Sample(8)
s4=Sample(12)

s5=s4-s1+s3*s2

print(s5)