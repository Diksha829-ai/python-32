a=int(input("Enter the total number of natural numbers: "))
largest = 0
for i in range(a):
    num = int(input("Enter a natural number: "))
    if num > largest:
        largest = num
print("The largest number is:", largest)
