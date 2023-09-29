#Q14- How many students are graduating by the end of 2024?

import pandas as pd
file_path = r'C:\Users\Sudhanshu\Desktop\IAC\Data analyst Data.xlsx'
df = pd.read_excel(file_path)

graduating_students = df[df['Year of Graduation'] <= 2024]

total_graduating_students = graduating_students.shape[0]
print("Number of students graduating by the end of 2024:", total_graduating_students)

#Conclusion: Total 1416 students will be graduating by the end of 2024