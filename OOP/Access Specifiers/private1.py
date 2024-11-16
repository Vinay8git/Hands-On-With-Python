class Test:
    def __init__(self):
        self.__a =0
        self.__b=0
        self.__c=0
    
    def set_value(self, a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c
    
    def get_value(self):
        return self.__a,self.__b,self.__c
        
    

t1=Test()
t1.set_value(10,20,30)
print(t1.get_value())
tup1=t1.get_value()
for val in tup1:
    print(val)