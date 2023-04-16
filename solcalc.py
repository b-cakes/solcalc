# Functions for solcalc.

# Parameters:
# cost per unit or watt, sell per unit or watt, GM%, and profit(GM$). 

# Required to know two parameters, but only need two parameters to find all values.

# Enter cost per watt and GM%, return sell per watt.
def cost_watt_gm(cost_watt: float, gm: float) -> float:
    sell_watt = cost_watt / (1 - gm)
    return sell_watt

# Enter sell_watt and GM%, return cost/watt. 
def sell_watt_gm(sell_watt: float, gm: float) -> float:
    cost_watt = sell_watt - (gm * sell_watt)
    return cost_watt

# Enter cost per unit and GM%, return sell per unit.
def cost_unit_gm(cost_unit: float, gm: float) -> float:
    sell_unit = cost_unit / (1 - gm)
    return sell_unit

# Enter sell per unit and GM$, return cost per unit.
def sell_unit_gm(sell_unit: float, gm: float) -> float:
    cost_unit = sell_unit - (gm * sell_unit)
    return cost_unit

test1 = cost_watt_gm(1.00, 0.20)
print(test1)

test2 = sell_watt_gm(1.25, 0.20)
print(test2)

test3 = cost_unit_gm(400.00, 0.20)
print(test3)

test4 = sell_unit_gm(500.00, 0.20)
print(test4)
