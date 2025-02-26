print("~Mini Calculator~")

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

option = int(input("Choose an operation: "))
result = 0

if(option in [1,2,3,4]):
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))

    if option == 1:
        result = n1 + n2
    elif option == 2:
        result = n1 - n2
    elif option == 3:
        result = n1 * n2
    elif option == 4:
        result = n1 / n2
else:
    print("You have entered an invalid output.")

print(f"Result = {result}")