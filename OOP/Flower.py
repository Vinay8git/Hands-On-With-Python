class Flower:
    def __init__(self):
        self.__flower_name = None
        self.__price_per_kg = None
        self.__stock_available = None

    def set_flower_name(self, name):
        self.__flower_name = name

    def set_price_per_kg(self, rate):
        self.__price_per_kg = rate

    def set_stock_available(self, stock):
        self.__stock_available = stock

    def validate_flower(self):
        ls = ["orchid", "rose", "jasmine"]
        if self.__flower_name.lower() in ls:
            return True
        else:
            return False

    def validate_stock(self, required_quantity):
        if self.__stock_available <= required_quantity:
            return True
        else:
            return False

    def sell_flower(self, required_quantity):
        if self.validate_flower == True and self.validate_stock == True:
            self.set_stock_available(self.__stock_available - required_quantity)
