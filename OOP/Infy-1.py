class Vehicle:
    def __init__(self):
        self.__vehicle_id = None
        self.__vehicle_type = None
        self.__vehicle_cost = None
        self.__premium_amount = None
        self.__premium_percentage = None

    def set_vehicle_id(self, vehicle_id):
        self.__vehicle_id = vehicle_id

    def set_vehicle_type(self, vehicle_type):
        self.__vehicle_type = vehicle_type
        if self.__vehicle_type == "Two Wheeler":
            self.__premium_percentage = 2
        elif self.__vehicle_type == "Four Wheeler":
            self.__premium_percentage = 6
        else:
            self.__premium_percentage = -1

    def set_vehicle_cost(self, vehicle_cost):
        self.__vehicle_cost = vehicle_cost

    def calculate_premium(self):
        if self.__premium_percentage == -1:
            self.__premium_amount = None
            return None
        self.__premium_amount = self.__premium_percentage * self.__vehicle_cost / 100

    def set_premium_amount(self, premium_amount):
        self.__premium_amount = premium_amount

    def get_vehicle_id(self):
        return self.__vehicle_id

    def get_vehicle_type(self):
        return self.__vehicle_type

    def get_vehicle_cost(self):
        return self.__vehicle_cost

    def get_premium_amount(self):
        return self.__premium_amount

    def display_vehicle_details(self):
        print(self.__vehicle_id)
        print(self.__vehicle_type)
        print(self.__vehicle_cost)
        self.calculate_premium()
        # v.calculate_premium()
        print(self.__premium_amount)

    def __str__(self):
        return "Vehicle Cost" + str(self.get_vehicle_cost)


v = Vehicle()
v.set_vehicle_id("UP35BC9478")
v.set_vehicle_type("Two Wheeler")
v.set_vehicle_cost(92000)
# v.calculate_premium()
v.display_vehicle_details()