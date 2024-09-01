
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial


n = int(input("Enter a non-negative integer: "))
print(f"The factorial of {n} is: {calculate_factorial(n)}")
