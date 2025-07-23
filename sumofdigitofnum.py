n=int(input("Enter the number"))
s=0
while n > 0:
    digit = n % 10
    s += digit
    n //= 10
print("Sum of digits:", s)