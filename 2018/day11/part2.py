from power import FuelGrid


serial_number = 8561

fuel_grid = FuelGrid(serial_number)
result = fuel_grid.find_highest_power_of_all_squares()

print(result)
