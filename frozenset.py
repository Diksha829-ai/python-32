f_set=frozenset([1, 2, 3, 4, 5])

print(type(f_set))

print(f_set)  
# frozenset is immutable, so we cannot add or remove elements

# function of frozenset
print(len(f_set))  # Length of the frozenset
print(3 in f_set)  # Check if an element is in the frozenset
print(f_set.union([6, 7]))  # Union with another iterable
print(f_set.intersection([3, 4, 5, 6]))  #

