def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

x = float(input("Enter the value of X (in radians): "))
n = int(input("Enter the highest even power (n): "))

cos_x = 0
sign = 1

for i in range(0, n + 1, 2):
    term = sign * (x ** i) / factorial(i)
    cos_x += term
    sign *= -1

print(f"cos({x}) using series up to X^{n}/{n}! is: {cos_x}")