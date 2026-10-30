# Count matching numbers

def count_numbers(numbers, target):
    count = 0

    for num in numbers:
        if num == target:
            count += 1

    return count


numbers = [10, 20, 40, 60, 80]
target = 10
result = count_numbers(numbers, target)
print(result)
