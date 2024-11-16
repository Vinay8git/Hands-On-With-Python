class c1:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        print (self.a*self.b)

class c2(c1):
    def __init__(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c

    def vol(self):
        print(self.a*self.b*self.c)
        super(c2, self).__init__(self.a, self.b)  # 8 2
        # super(c2, self).area()   #  8 2 2

ob=c2(1,2,4)
ob.vol()
ob.area()