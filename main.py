# -------- Built-in Module Handling --------
import math
import random
import datetime

print("=== Built-in Module Handling ===")
print("Square root of 25:", math.sqrt(25))
print("Random number between 1 and 10:", random.randint(1, 10))
print("Current date and time:", datetime.datetime.now())

# -------- User-defined Module Handling --------
import mymodule   # importing our own module

print("\n=== User-defined Module Handling ===")
print(mymodule.greet("Diksha"))
print("Addition using mymodule:", mymodule.add(10, 5))