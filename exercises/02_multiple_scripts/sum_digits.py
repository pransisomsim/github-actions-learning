
def sum_digit(number):
    total = 0

    while number > 0:
        total = total + (number % 10)
        number = number // 10

    return total

print(sum_digit(123))
print(sum_digit(456))
print(sum_digit(789))
