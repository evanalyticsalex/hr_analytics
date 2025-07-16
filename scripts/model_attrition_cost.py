import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os

# Create outputs directory if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# Load the dataset
df = pd.read_csv("data/WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Add a flag: 1 if employee left, 0 if stayed
df['AttritionFlag'] = df['Attrition'].apply(lambda x: 1 if x == 'Yes' else 0)

# Define a flat cost estimate per lost employee
COST_PER_EMPLOYEE = 50000  # Adjust based on company size

# Total employees who left
total_leavers = df['AttritionFlag'].sum()

# Total estimated cost
total_cost = total_leavers * COST_PER_EMPLOYEE

# Print results
print(f"Total employees lost: {total_leavers}")
print(f"Estimated total attrition cost: ${total_cost:,.0f}")

import matplotlib.pyplot as plt

# Attrition cost by department
dept_costs = df[df['AttritionFlag'] == 1].groupby('Department').size() * COST_PER_EMPLOYEE

# Plot it
dept_costs.sort_values().plot(kind='barh', figsize=(10, 6), color='skyblue')
plt.title('Estimated Attrition Cost by Department')
plt.xlabel('Cost in USD')
plt.ylabel('Department')
plt.tight_layout()
plt.show()


# Save detailed cost data
df[df['AttritionFlag'] == 1].to_csv("outputs/attrition_leavers.csv", index=False)

# Save summary table
dept_costs.to_csv("outputs/attrition_cost_by_department.csv")
