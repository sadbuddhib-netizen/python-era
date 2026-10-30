"""Count how many times a target appears in a list."""


def count_occurrences(numbers, target):
    count = 0

    for number in numbers:
        if number == target:
            count += 1

    return count


if __name__ == "__main__":
    numbers = [10, 20, 10, 30, 10, 40]
    print(count_occurrences(numbers, 10))  # 3
    print(count_occurrences(numbers, 20))  # 1
    print(count_occurrences(numbers, 50))  # 0
