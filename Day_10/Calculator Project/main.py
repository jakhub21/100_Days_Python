from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def devide(n1, n2):
    return n1 / n2


flag = True
result = 0
while flag:
    flag2 = True
    n1 = int(input("Type the first number\n"))
    while flag2:
        operation = input("Type mathematical operation\n+\n-\n*\n/\n")
        n2 = int(input("Type the second number\n"))
        if operation == "+":
            result = add(n1, n2)
        elif operation == "-":
            result = substract(n1, n2)
        elif operation == "*":
            result = multiply(n1, n2)
        elif operation == "/":
            result = devide(n1, n2)
        else:
            print("Bad ooperation symbol try again")
        print(f"{n1} {operation} {n2} = {result}")
        answer = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation, or type 'exit if you want to leave\n")
        if answer == "y":
            n1 = result
        elif answer == "n":
            flag2 = False
        else:
            flag2 = False
            flag = False