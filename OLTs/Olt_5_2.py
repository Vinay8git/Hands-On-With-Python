class A:
    def __init__(self):
        self.calc(40)
        print("I from A is", self.I)

    def calc(self, I):
        self.I=2*I

class B(A):
    def __init__(self):
        super().__init__()

    def calc(self, I):
        self.I=3*I

b=B()