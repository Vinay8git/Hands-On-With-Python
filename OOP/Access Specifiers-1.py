class Acc:
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name


obj=Acc()
obj.set_name("test")
print(obj.get_name())