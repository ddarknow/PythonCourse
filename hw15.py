import math

def distance(x1, y1, x2, y2):
    z1 = (x2 - x1)
    z1 = z1**2
    
    z2 = (y2 - y1)
    z2 = z2**2
    
    return round(math.sqrt(z1 + z2), 2)