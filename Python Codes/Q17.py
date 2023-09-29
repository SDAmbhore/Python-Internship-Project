#Q17- Those who have high CGPA & More experience in language those who had high expectations for salary? (Avg)

import pandas as pd
import matplotlib.pyplot as plt
file_path = r'C:\Users\Sudhanshu\Desktop\IAC\Data analyst Data.xlsx'
df = pd.read_excel(file_path)

cgpa = df['CGPA']
experience_python = df['Experience with python (Months)']
expected_salary = df['Expected salary (Lac)']

# Create a figure with three subplots arranged side by side
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Plot 1: CGPA
axs[0].hist(cgpa, bins=20, color='skyblue', alpha=0.7, edgecolor='black')
axs[0].set_title('CGPA Distribution')
axs[0].set_xlabel('CGPA')
axs[0].set_ylabel('Frequency')

# Plot 2: Experience with Python
axs[1].hist(experience_python, bins=20, color='lightgreen', alpha=0.7, edgecolor='black')
axs[1].set_title('Experience with Python Distribution')
axs[1].set_xlabel('Experience with Python (Months)')
axs[1].set_ylabel('Frequency')

# Plot 3: Expected Salary
axs[2].hist(expected_salary, bins=20, color='lightcoral', alpha=0.7, edgecolor='black')
axs[2].set_title('Expected Salary Distribution')
axs[2].set_xlabel('Expected Salary (Lac)')
axs[2].set_ylabel('Frequency')

# Adjust spacing between subplots
plt.tight_layout()

# Show the plots
plt.show()

#Conclusion: Most students have a CGPA between 7 and 7.5, possess 5 months of Python programming experience, and hold salary expectations close to 10 lakhs.