n=int(input("Enter the nymber"))
factorial=1
for i in range(1, n + 1):
    factorial *= i
print("Factorial of", n, "is:", factorial)