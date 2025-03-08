class int(object):
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
class employee(int):
    def __init__(self, name, idnumber,salary,post):
        self.salary=salary
        self.post=post
        int.__init__(self,name,idnumber)
a=employee('aitihya',20161019,'100000$','CEO')
a.display()


        