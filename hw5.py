a = str(input("Enter first number: "))
b = str(input("Enter secondd number: "))

print(f"\n Original view:\n a = {a}, b = {b} \n")

a, b = b, a

print(f"Replaced view:\n a = {a}, b = {b}")