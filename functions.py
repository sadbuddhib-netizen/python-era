def greet():
    print("Hello")
greet()


def add (a,b):
    return a+b
print(add(10,20))


def sub (c,d):
    return c-d
print(sub(30,10))

def mul(s,q):
    return s*q
print (mul(10,30))

def div(t,m):
    return t/m
print(div(5,10))

def square(u):
    return u*u
print(square(10))

def sabu(num):
    if num%2 == 0:
        return "even"
    else:
        return "odd"
    
print(sabu(8))
print(sabu(9))
  

def large(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>a and b>=c:
        return b
    else:
        return c
    
print(large(8,9,10))

def even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
    
print(even_odd(9)) 
print(even_odd(0))   
    
    
