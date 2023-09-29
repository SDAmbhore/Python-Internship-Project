#Q11- Which event tend to attract more students from specific field of study?

import pandas as pd
file_path = r'C:\Users\Sudhanshu\Desktop\IAC\Data analyst Data.xlsx'
df = pd.read_excel(file_path)

import matplotlib.pyplot as plt

event_counts = df['Events'].value_counts()

plt.figure(figsize=(10, 6))
event_counts.plot(kind='bar')
plt.title('Number of Students Attending Each Event')
plt.xlabel('Event')
plt.ylabel('Number of Students')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#Conclusion: Internship Program (IP) Success Conclave attract more students
