def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def divide(a, b):
    return a / b

number1 = float(input("enter a number: "))
operator = input("enter an operator (+,-,*,/): ")
number2 = float(input("enter a number: "))
if operator == "+":
     print(add(number1, number2))

elif operator == "-":
    print(sub(number1, number2))

elif operator == "*":
    print(mul(number1, number2))

elif operator == "/":
    if number2 != 0:
            print(divide(number1, number2))
    else:
            print("cannot divide by zero")

else:
        print("Invalid operator")


