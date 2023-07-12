def add (n1, n2):
  return n1 + n2

def subtract (n1, n2):
  return n1 - n2

def divide (n1, n2):
  return n1 / n2

def multiply (n1, n2):
  return n1 * n2

operations = {
  "+": add,
  "-": subtract,
  "/": divide,
  "*": multiply
}

num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))

for symbol in operations:
  print(symbol)

operation_symbol = input("Pick an operation from the line above ")

calculator_function = operations[operation_symbol]

print(f"{num1} {operation_symbol} {num2} = {calculator_function(num1, num2)}")
