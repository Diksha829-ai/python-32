import matplotlib.pyplot as plt

# Data for multi-line graph
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

# Sales data of two products
product_A = [120, 140, 160, 180, 200, 220]
product_B = [100, 130, 150, 170, 190, 210]

# Create Multi Line Graph
plt.figure()
plt.plot(months, product_A, label="Product A")  # Line 1
plt.plot(months, product_B, label="Product B")  # Line 2

plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Sales Comparison: Product A vs Product B")
plt.legend()  # Shows labels for both lines
plt.grid(True)
plt.show()
