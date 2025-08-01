class mybrain:
    def __init__(self):
        self.public="public"
        self._protected="protected"
        self.__private="Private"
    def subclass(self):
        print("This is",self.public)
        print("This is ",self._protected)
        
        try:
            print("This is ",self.__private)
        except AttributeError:
            print('error')    

class child(mybrain):
    def subclass(self):
        return super().subclass()
    
a=child()
a.subclass()