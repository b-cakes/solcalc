import solcalc as sc
from solar_module import SolarModule

# solcalc tests:
test1 = sc.cost_watt_gm(1.00, 0.20)
print(test1)

test2 = sc.sell_watt_gm(1.25, 0.20)
print(test2)

test3 = sc.cost_unit_gm(400.00, 0.20)
print(test3)

test4 = sc.sell_unit_gm(500.00, 0.20)
print(test4)



# solar_module tests:
mod_1 = SolarModule('REC', 'NP3')

mod_1.rating(400)
mod_1.cost(0.71)
mod_1.show()

mod_1.rating(500)
mod_1.sell(1.00)
mod_1.show()
