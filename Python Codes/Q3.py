#Q3- What is the distribution of the students across different graduation years?

import pandas as pd
import matplotlib.pyplot as plt
file_path = r'C:\Users\Sudhanshu\Desktop\IAC\Data analyst Data.xlsx'
df = pd.read_excel(file_path)

graduation_year_distribution = df['Year of Graduation'].value_counts()

# Create a bar plot
plt.figure(figsize=(10, 6))
graduation_year_distribution.plot(kind='bar')
plt.title('Distribution of students across different graduation years')
plt.xlabel('Year of Graduation')
plt.ylabel('Number of Students')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#Conclusion: 2023 has the highest number of graduating students and 2026 has the lowest number of graduating students