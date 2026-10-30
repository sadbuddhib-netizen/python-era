"""Linear search: return True if the target exists in the list."""


def find_name(names, target):
    for name in names:
        if name == target:
            return True
    return False


if __name__ == "__main__":
    names = ["anita", "vanita", "om", "yamadasan"]
    print(find_name(names, "om"))      # True
    print(find_name(names, "rahul"))   # False
