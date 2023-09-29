#Q12- Do students in leadership positions during their college years tend to have higher GPAs or better expected salary?

import pandas as pd
import matplotlib.pyplot as plt
file_path = r'C:\Users\Sudhanshu\Desktop\IAC\Data analyst Data.xlsx'
df = pd.read_excel(file_path)


plt.figure(figsize=(12, 8))

# Box plot for CGPA based on Leadership skills
plt.subplot(2, 1, 1)
df['Leadership- skills'] = df['Leadership- skills'].astype('category')
plt.boxplot([df[df['Leadership- skills'] == 'yes']['CGPA'], df[df['Leadership- skills'] == 'no']['CGPA']], labels=['yes', 'no'])
plt.title('CGPA Based on Leadership Skills')
plt.xlabel('Leadership Skills')
plt.ylabel('CGPA')

# Box plot for Expected Salary based on Leadership skills
plt.subplot(2, 1, 2)
plt.boxplot([df[df['Leadership- skills'] == 'yes']['Expected salary (Lac)'], df[df['Leadership- skills'] == 'no']['Expected salary (Lac)']], labels=['yes', 'no'])
plt.title('Expected Salary Based on Leadership Skills')
plt.xlabel('Leadership Skills')
plt.ylabel('Expected Salary (Lac)')

plt.tight_layout()
plt.show()

#Conclusion: Students in leadership positions during their college years tend to have better expected salary
