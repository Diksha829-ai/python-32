a=int(input("Enter the total number of natural numbers: "))
lowest= 0
for i in range(a):
    num = int(input("Enter a natural number: "))
    if num < lowest or lowest == 0:
        lowest= num
print("The lowest number is:",lowest)
