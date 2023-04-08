# SolarModule is parent class

class SolarModule:

    def __init__(self, manufacturer: str, product_line: str):
        self.mfg = manufacturer
        self.line = product_line
        self.watt_rating = 0
        self.watt_cost = 0.00
        self.watt_sell = 0.00

    def rating(self, watt_rating: int):
        self.watt_rating = watt_rating

    def cost(self, watt_cost: float):
        self.watt_cost = watt_cost

    def sell(self, watt_sell: float):
        self.watt_sell = watt_sell

    def show(self):
        print(self)
        print(self.mfg)
        print(self.line)
        print(self.watt_rating)
        print(self.watt_cost)
        print(self.watt_sell)


mod_1 = SolarModule('REC', 'NP3')

mod_1.rating(400)

mod_1.cost(0.71)

mod_1.show()

mod_1.rating(500)

mod_1.sell(1.00)

mod_1.show()
