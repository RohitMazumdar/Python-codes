def create_plus_string(numbers):
    plus_string = '+'.join(numbers)
    return plus_string

user_numbers = []
for i in range(5):
    number = input("Enter a number:")
    user_numbers.append(number)

plus_string = create_plus_string(user_numbers)
print("Plus_separated_string:", plus_string)
