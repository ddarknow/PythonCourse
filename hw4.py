n = input("Input 4 digit number: ")
count = 1
for x in n:
    count *= int(x)

print("Multiplied nubers summary is:", count)

y = str(n)
z = y[::-1]

print("Reversed: ", z)

print("List of sorted elements: ", sorted(y))