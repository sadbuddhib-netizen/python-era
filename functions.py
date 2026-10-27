# finding the even numbers
def even(n):
 count = 0
 for i  in range (1,n+1):
  if i % 2 == 0:
   print(i)
   count  += 1
 return count  
result = even(10)
print(result)

# check the students paas or fail
marks = int (input("enter a marks :"))   
def students(marks):
    if marks >= 70 :
        return("Distinction")
    elif marks >= 35:
        return("pass")
    elif marks >= 0:
        return "Fail"
    else :
        return("please enter valid input")
 
result = students(marks)
print(result)    

#sum the numbers
def numbers(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total
print(numbers(10,20,30,40,50,60,70,80,90))    

#Write a function that accepts multiple numbers using *args and returns how many numbers are odd.
def count_even(*numbers):
    count = 0
    for i in numbers:
        if i % 2 == 0:
            count += 1
    return count

print(count_even(80, 90,3))






 
