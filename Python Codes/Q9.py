#Q9- Can we identify any relationship between family income and GPA?

import pandas as pd
file_path = r'C:\Users\Sudhanshu\Desktop\IAC\Data analyst Data.xlsx'
df = pd.read_excel(file_path)

import matplotlib.pyplot as plt

df_sorted = df.sort_values(by='Family Income')

plt.figure(figsize=(10, 6))
plt.scatter(df_sorted['Family Income'], df_sorted['CGPA'], alpha=0.5)
plt.title('Relationship between Family Income and CGPA')
plt.xlabel('Family Income')
plt.ylabel('CGPA')
plt.tight_layout()
plt.show()

#Conclusion: Yes, we can identify and analyse relationship between family income and GPA with the help of dot chart or dot plot.