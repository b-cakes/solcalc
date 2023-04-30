# SolarModule is parent class

class SolarModule:

    def __init__(self):
        self.mfg: str | None = None
        self.line: str | None = None
        self.watt_rating: int = 0
        self.cost_watt: float = 0.00
        self.sell_watt: float = 0.00
        self.cost_unit: float = 0.00
        self.sell_unit: float = 0.00
        self.gm: float = 0.00
        self.profit: float = 0.00

    def rating(self, watt_rating: int):
        self.watt_rating = watt_rating

    def cost(self, cost_watt: float):
        self.cost_watt = cost_watt

    def sell(self, sell_watt: float):
        self.sell_watt = sell_watt

    def show(self):
        print(self)
        print(self.mfg)
        print(self.line)
        print(self.watt_rating)
        print(self.cost_watt)
        print(self.sell_watt)
        print(self.cost_unit)
        print(self.sell_unit)
        print(self.gm)
        print(self.profit)

