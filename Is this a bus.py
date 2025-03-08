class Vechile:
    def __init__(self,name,mile,max):
        self.name=name
        self.mile=mile
        self.max=max
class bus(Vechile):
    pass
vb=bus('school',30,120)    
print('Bus name',vb.name,'range',vb.mile,'max speed',vb.max)    
        