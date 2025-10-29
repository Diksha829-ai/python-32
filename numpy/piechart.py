import matplotlib.pyplot as plt

# Data for pie chart
names = ["Diksha", "Rutu", "Deva", "Abhi"]
salaries = [50000, 60000, 70000, 55000]

# Create Pie Chart
plt.figure()
plt.pie(salaries, labels=names, autopct="%1.1f%%")  # Shows % values
plt.title("Employee Salary Distribution")
plt.show()
