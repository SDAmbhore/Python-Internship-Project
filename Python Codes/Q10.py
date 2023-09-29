#Q10- How does the expected salary vary based on factors like “GPA”, “Family Income”, “Experience with Python (Months)”?

import pandas as pd
import matplotlib.pyplot as plt
file_path = r'C:\Users\Sudhanshu\Desktop\IAC\Data analyst Data.xlsx'
df = pd.read_excel(file_path)

plt.figure(figsize=(12, 8))

# Scatter plot for Expected Salary vs. CGPA
plt.subplot(2, 2, 1)
plt.scatter(df['CGPA'], df['Expected salary (Lac)'], alpha=0.5)
plt.title('Expected Salary vs. CGPA')
plt.xlabel('CGPA')
plt.ylabel('Expected Salary (Lac)')

# Box plot for Expected Salary vs. Family Income
plt.subplot(2, 2, 2)
family_income_order = ['0-2 Lakh', '2-5 Lakh', '5-7 Lakh', '7 Lakh+']
df['Family Income'] = pd.Categorical(df['Family Income'], categories=family_income_order, ordered=True)
plt.boxplot([df[df['Family Income'] == value]['Expected salary (Lac)'] for value in family_income_order], labels=family_income_order)
plt.title('Expected Salary vs. Family Income')

plt.xlabel('Family Income')
plt.ylabel('Expected Salary (Lac)')

# Scatter plot for Expected Salary vs. Experience with Python
plt.subplot(2, 2, 3)
plt.scatter(df['Experience with python (Months)'], df['Expected salary (Lac)'], alpha=0.5)
plt.title('Expected Salary vs. Experience with Python')
plt.xlabel('Experience with Python (Months)')
plt.ylabel('Expected Salary (Lac)')

plt.tight_layout()
plt.show()

#Conclusion: Students with a family income of 5 – 7 lakh have high salary expectations, while students with a family income of 2 – 5 lakh have low salary expectations.



