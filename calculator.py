class Cal:
    def add(self, first_value, second_value):
        return f"{first_value} + {second_value} = {first_value+second_value}"

    def subtract(self, first_value, second_value):
        return f"{first_value} - {second_value} = {first_value-second_value}"

    def divide(self, first_value, second_value):
        return f"{first_value} / {second_value} = {first_value//second_value}"

    def exponent(self, first_value, second_value):
        return f"{first_value} ** {second_value} = {first_value**second_value}"

    def multiply(self, first_value, second_value):
        return f"{first_value} * {second_value} = {first_value * second_value}"


def values():
    while True:
        try:
            value_one = int(input("Please enter the first value:\n"))
            value_two = int(input("Please enter the second value:\n"))
            return value_one, value_two
        except ValueError as Error:
            print(Error)
            print("The value must be in integer. Please enter the first value again:\n")


while True:
    ask = ("Please enter the command to begin. If you don't know the commands,"
           " please use /help to check, and /exit to exit:\n")
    check = input(ask).lower()
    calculator = Cal()
    # if check in ["/add", "/divide", "/multiply", "/subtract", "/exponent"]:
    #     value_one, value_two = values()
    if check == "/help":
        print('''
                 /add
                 /subtract
                 /multiply
                 /divide
                 /exponent
                 /exit
        ''')

    elif check == "/add":
        value_one, value_two = values()
        print(calculator.add(value_one, value_two))

    elif check == "/subtract":
        value_one, value_two = values()
        print(calculator.subtract(value_one, value_two))

    elif check == "/multiply":
        value_one, value_two = values()
        print(calculator.multiply(value_one, value_two))

    elif check == "/divide":
        value_one, value_two = values()
        print(calculator.divide(value_one, value_two))

    elif check == "/exponent":
        value_one, value_two = values()
        print(calculator.exponent(value_one, value_two))

    elif check == "/exit":
        break
    else:
        print("Invalid Command")
