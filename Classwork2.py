# Presentation 6.1:

term = input ('Type some number: ')
lst = [int(x) for x in str(term)]
print(lst)

print('Biggest number: ', max(lst))
print('Smallest number: ', min(lst))

# Presentation 6.2:

for x in range(1,11):
    if x % 2 == 0:
        print(x, 'is even and multiple of 2')
    elif x % 3 == 0:
        print(x, 'is odd and multiple of 3')
    else:
        print(x, 'is not divideable by 2 and 3')

# Presentation 6.3:

num = int(input("Enter number: "))
fact = 1
if num < 0:
    print("Negative number, factorial doesn't exist")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        fact = fact*i
    print("Factorial of {0} is {1}".format(num, fact))

# Presentation  6.4:

user = input("Your log in: ")

while user != 'First':
    print("Error, wrong username, try again")
    user = input("Username: ")

print("Greetings First!")