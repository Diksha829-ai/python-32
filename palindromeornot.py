n=int(input("Enter the number"))
original = n
reverse=0

while n > 0:
   digit=n%10   
   reverse=reverse*10+digit 

if original==reverse:
    print(original, "is a palindrome")  
else:
    print(original, "is not a palindrome")