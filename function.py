# function without default arguments
def my_fun (n1, n2):
    print("number 1 is:", n1)
    print("number 2 is:", n2)
    print("sum is:", n1 + n2)

my_fun(10, 20)

# function with default arguments
def new_fun(a1, a2=20):

    print("number 1 is:", a1)
    print("number 2 is:", a2)
    print("sum is:", a1 + a2)

new_fun(10)  # a2 will take the default value of 20


new_fun(10, 30)  # a2 will take the value of 30