# is it possible to get to the pump or not:

def zero_fuel(distance_to_pump, mpg, fuel_left):

    distance_to_pump = int(distance_to_pump)
    mpg = float(mpg)
    fuel_left = float(fuel_left)
    
    while distance_to_pump > mpg*fuel_left:
        return print(False)
    else:
        return print(True)

