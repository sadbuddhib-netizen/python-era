# Second highest salary

def second_higest(numbers):
    highest = None
    Second = None

    for num in numbers:
        if highest is None or num > highest:
            Second = highest
            highest = num
        elif num != highest and (Second is None or num > Second):
            Second = num

    return Second


numbers = [10, 90, 70, 20]
result = second_higest(numbers)
print("second highest salary", result)


# Third highest salary

def Third_highest_salary(numbers):
    highest = None
    second = None
    Third = None

    for num in numbers:
        if highest is None or num > highest:
            Third = second
            second = highest
            highest = num
        elif num != highest and (second is None or num > second):
            Third = second
            second = num
        elif num != highest and second != Third and (Third is None or num > Third):
            Third = num

    return Third


numbers = [10, 30, 40, 50, 60]
result = Third_highest_salary(numbers)
print("Third_highest_salary", result)


# Second lowest salary

def second_lowest_salary(numbers):
    lowest = None
    second = None

    for num in numbers:
        if lowest is None or num < lowest:
            lowest = num
            second = lowest
        elif num != lowest and (second is None or num < second):
            second = num

    return lowest


numbers = [70, 80, 90, 10]
result = second_lowest_salary(numbers)
print("second_lowest_salary", result)


# List indexing

List = [12, 3, 45, 7]
first_number = List[3]
print(first_number)


# Search for a paper/name

def paper_find(Name, Papers):
    for Paper in Papers:
        if Paper == Name:
            return True
    return False


Papers = ["anita", "vanita", "om", "yamadasan"]
search_name = "om"
result = paper_find(search_name, Papers)
print("got a match", result)


# Find a name in a list

def find_name(names, Papers):
    for Paper in Papers:
        if Paper == names:
            return True
    return False


Papers = ["anita", "vanita", "om", "yamadasan"]
names = "Rahul"
result = find_name(names, "rahul")
print("got a match", result)


# Count matching numbers

def count_numbers(numbers, target):
    count = 0

    for num in numbers:
        if num == target:
            count += 1

    return count


numbers = [10, 20, 40, 60, 80, 10]
target = 10
result = count_numbers(numbers, target)
print(result)
