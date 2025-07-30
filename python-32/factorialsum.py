def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

n = int(input("Enter the value of n: "))
sum_seq = 1.0  # Start with the first term

for i in range(1, n + 1):
    sum_seq += 1 / factorial(i)

print(f"Sum of the sequence up to 1/{n}! is: {sum_seq}")