class VotingNotAllowedException(Exception):
    pass

class voter:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        if(age<18):
            return VotingNotAllowedException("not allowed to vote")
        else:
            print("You are allowed")