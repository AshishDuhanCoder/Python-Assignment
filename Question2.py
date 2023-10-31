class Sample:
    def __init__(self,data):
        self.data=data
    def __lt__(self,obj):
        return self.data<obj.data
    def __eq__(self,obj):
        return self.data==obj.data
    def __gt__(self,obj):
        return self.data>obj.data
s1=Sample(7)
s2=Sample(5)
print(s1==s2)