# Presentation 7.1:

def ser_ar(*arg):
    return sum(arg)/len(arg)

# Presentation 7.2:

def max_number(*arg):
    '''Some function description'''
    return max(arg)

# Presentation 7.3:

def rectangle():
    a = float(input("Input width: "))
    b = float(input("Input height: "))
    return "Square={}".format(a*b)

def triangle():
    a = float(input("Input basis: "))
    h = float(input("Input height: "))
    return "Area={}".format(0.5 * a * h)

def circle():
    PI = 3.14
    r = float(input("Input radius: "))
    return "Square={}".format(PI * r**2)

figure = input("1 - rectangle, 2 - triangle, 3 - circle")
if figure == '1':
    print(rectangle())
elif figure == '2':
    print(triangle())
elif figure == '3':
    print(circle())
else:
    print("Input error")

# Presentation 7.4:

def symb_count(word):
    result = {}
    for x in word:
        if x in result:
            continue
        else:
            result.update({str(x): word.count(x)})
    return result

print(symb_count("test"))