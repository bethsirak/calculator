def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

#First calculation
def calculator():
    operations = {"+": add, "-": subtract, "/": divide, "*": multiply}
    num1 = int(input("What is the first number? "))
    for symbol in operations:
        print(symbol)

    #Follow up calculations
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation ")
        num2 = int(input("What is the next number? "))
        calculator_function = operations[operation_symbol]
        first_answer = calculator_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {first_answer}")
        input_should_continue = input(f"Type 'y' to continue calculating with {first_answer} or type 'n' to start a new calculation ").lower()
        if input_should_continue == "y":
            num1 = first_answer
        else:
            should_continue = False
            calculator()


calculator()
