import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("graph.csv")
# Print Data
print(df)

# Create Bar Graph - Salary vs Name
plt.figure()
plt.bar(df["Name"], df["Salary"])   # NO specific colors
plt.xlabel("Employee Name")
plt.ylabel("Salary")
plt.title("Salary Comparison")
plt.show()
