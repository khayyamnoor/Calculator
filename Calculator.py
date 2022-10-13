
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

opreations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
    should_continue = True
    num_1 = float(input("What is The First Number: \n"))

    for symbols in opreations:
        print(symbols)

    while should_continue == True:

        opreation_function = input("Please select a operator to continue: \n")

        num_2 = float(input("What Is The Next Number: \n"))

        calculator_function = opreations[opreation_function]
        answer = round(calculator_function(num_1, num_2))
        print(f"{num_1} {opreation_function} {num_2} = {answer}")
        loop = True
        while loop == True:

            result = input(f"Type Y to continue with {answer} N to start new or Q to quit: \n").lower()

            if result == "y":
                num_1 = answer
                loop = False
            elif result == "n":
                loop = False
                should_continue = False
                calculator()
            elif result == "q":
                loop = False
                should_continue = False
                print("Good Bye :)")
calculator()