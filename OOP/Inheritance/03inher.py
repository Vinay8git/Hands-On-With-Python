class Vehicle:
    def __init__(self, brand, name):
        self.brand=brand
        self.name=name
    
    def display(self):
        print(self.brand, self.name)

class Car(Vehicle):
    def __init__(self, brand, name, model, type, safety_Ratings):
        super().__init__(brand, name)
        self.model=model
        self.type=type
        self.safety_Ratings=safety_Ratings

    def display(self):
        # super().display()      # Display Super Class's Attributes
        print(self.brand, self.name, self.model, self.type, self.safety_Ratings)


def main():
    c1=Car("BMW", "X5", "2020", "SUV", "5-Star")
    c1.display()

    c2=Car("Mahindra", "Thar", "2024", "Off-Roady", "4-Star")
    c2.display()

if __name__=="__main__":
    main()