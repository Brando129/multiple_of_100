# Create a function that takes an integer and returns true if it's divisible by 100, otherwise return false.

def multiple_or_not(number):
    if number % 100 == 0:
        return True
    else:
        return False

print(multiple_or_not(1100))