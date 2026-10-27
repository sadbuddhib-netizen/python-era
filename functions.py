# Python Functions Practice
# Topics: defining functions, return values, conditionals, loops, and *args


def greet():
    """Print a greeting."""
    print("Hello")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def square(number):
    return number * number


def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"


def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    return c


def print_even_numbers(limit):
    """Print even numbers from 1 through limit and return their count."""
    count = 0
    for number in range(1, limit + 1):
        if number % 2 == 0:
            print(number)
            count += 1
    return count


def student_result(marks):
    """Return a result for marks from 0 to 100."""
    if marks < 0 or marks > 100:
        return "Invalid marks"
    elif marks >= 70:
        return "Distinction"
    elif marks >= 35:
        return "Pass"
    return "Fail"


def sum_numbers(*numbers):
    """Return the sum of any number of numeric arguments."""
    total = 0
    for number in numbers:
        total += number
    return total


def count_even(*numbers):
    """Return how many supplied numbers are even."""
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count


def count_odd(*numbers):
    """Return how many supplied numbers are odd."""
    count = 0
    for number in numbers:
        if number % 2 != 0:
            count += 1
    return count


if __name__ == "__main__":
    # Example calls
    greet()
    print("Addition:", add(10, 20))
    print("Subtraction:", subtract(30, 10))
    print("Multiplication:", multiply(10, 30))
    print("Division:", divide(5, 10))
    print("Square:", square(10))
    print("Even/odd:", even_or_odd(9))
    print("Largest:", largest_of_three(8, 9, 10))
    print("Even numbers from 1 to 10:")
    print("Count:", print_even_numbers(10))
    print("Student result:", student_result(75))
    print("Sum:", sum_numbers(10, 20, 30, 40, 50))
    print("Even count:", count_even(80, 90, 3))
    print("Odd count:", count_odd(0, 20, 30, 5, 67))
