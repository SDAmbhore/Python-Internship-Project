#Q4- What is the distribution of student’s experience with Python programming?

import pandas as pd
import matplotlib.pyplot as plt
file_path = r'C:\Users\Sudhanshu\Desktop\IAC\Data analyst Data.xlsx'
df = pd.read_excel(file_path)

experience_distribution = df['Experience with python (Months)'].value_counts()

# Create a bar plot
plt.figure(figsize=(10, 6))
experience_distribution.sort_index().plot(kind='bar')
plt.title('Distribution of students experience with Python programming')
plt.xlabel('Experience with Python (in months)')
plt.ylabel('Number of Students')
plt.xticks(rotation=0)

plt.show()

#Conclusion: Most students have 5 months of experience in Python programming