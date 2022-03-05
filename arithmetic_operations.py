total = 0
first_number = int(input("\nEnter first number: "))
second_number = int(input("\nEnter second number: "))

print(f'Addition: {first_number + second_number}')
print(f'Subtraction: {first_number - second_number}')
print(f'Multiplication: {first_number * second_number}')
try:
    print(f'Division: {first_number / second_number}')
    print(f'Modulus: {first_number % second_number}')
    print(f'Floor division: {first_number // second_number}')
except ZeroDivisionError:
    print("division by zero")

print(f'Exponentiation Operator: {first_number ** second_number}')

