n=int(input("Enter the number"))
if n> 1:
    for i in range(2, n):
        if n % i == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")
else:
    print("Enter a number greater than 1")
print("Thank you for using the program!")