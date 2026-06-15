num = int(input("enter a number:"))
print(num)

try:
   num = int(input("enter a number:"))
   print(num)
except:   
  print("invalid input")

try:
    num = int(input("enter a number:"))
    print(num)
except ValueError:
     print("enter numbers only") 
try:
    a = int(input("enter a number1:"))
    b = int(input("enter a number2:"))
    print(a/b)
except ZeroDivisionError:
    print("not division by zero")    



try:
   number1 = int(input("enter a number1"))
   number2 = int(input("enter a number2:"))
   print(number1/number2)
except ValueError:
   print("enter number only")
except ZeroDivisionError:
   print("not division  by zero")   


try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Result:", a/b)

except ValueError:
    print("Please enter valid numbers")

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Thank You")


try:
    a = int(input("enter a number:"))
    print(a)
except ValueError:
    print("enter a number a only")   


try:
    number1 =int(input("enter a first number"))
    number2 = int(input("enter a second number:"))
    print(number1/number2)
except ZeroDivisionError:
    print("not divisin by zero")    

try:
    a = int(input("enter anumber1 : "))
    b = int(input("enter a number 2 : "))
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
except ValueError:
    print("invalid input")
except ZeroDivisionError:
     print("cannot divide by zero")  
     

