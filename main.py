from artwork import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculation():
    print(logo)
    num1 = float((input("What's the first number?\n")))
    num2 = float(input("What is the second number?\n"))

    for operation in operations:
        print(operation)

    operation_symbol = input("Pick an operation from the line above: ")
    answer = operations[operation_symbol](num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    keep_going = input(f"Type 'y' to continue calculating with {answer}, type 'n' start a new calculation, or type 'e' to exit. ").lower()
    if keep_going == "n":
        calculation()
    num_prior = answer

    while keep_going == "y":
        operation_symbol_n = input("Pick another operation (+, -, *, /) ")
        num_n = float(input("What is the next number?\n"))
        answer_n = operations[operation_symbol_n](num_prior, num_n)
        print(f"{num_prior} {operation_symbol_n} {num_n} = {answer_n}")
        num_prior = answer_n
        
        keep_going = input(f"Type 'y' to continue calculating with {answer}, type 'n' start a new calculation, or type 'e' to exit. ").lower()
        if keep_going == "n":
            calculation()

calculation()