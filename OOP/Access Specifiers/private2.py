class Test:
    def __init__(self):
        self.__a =0
        self.__b=0
        self.__c=0
    
    def set_value(self, a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c
    
    def get_a(self):
        return self.__a
    def get_b(self):
        return self.__b
    def get_c(self):
        return self.__c
        
    

t1=Test()
t1.set_value(10,20,30)
print(t1.get_a())
print(t1.get_b())