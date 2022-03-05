# Part 1 Calculate the factorial of a given number
# 5*4*3*2*1    = 120
# Part 2 Find the number of trailing zeros in that factorial

def factorial(number):
    if number == 0 or number == 1:
        return 1
    # Method 1
    # for i in range(1, number+1):
    #     fact = fact * i
    # return fact
    # Method 2
    return number * factorial(number-1)


def factorial_trailing_spaces(number):
    # 5! 5*4*3*2*1
    # 6! 6*5*4*3*2*1
    # Check how many times 5 comes
    # 100! = 100//5 + 100//5*5
    count = 0
    i = 5
    while number//i != 0:
        count += int(number//i)
        i = i*5
    return count


if __name__ == '__main__':
    n = int(int(input("\nPlease enter number: ")))
    # factorial = factorial(n)
    # print(f"Factorial of {n} is {factorial}")
    print(f'Trailing Zero count is: {factorial_trailing_spaces(n)}')





