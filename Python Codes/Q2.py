#Q2- What is the average GPA of the students?

import pandas as pd
file_path = r'C:\Users\Sudhanshu\Desktop\IAC\Data analyst Data.xlsx'
df = pd.read_excel(file_path)

average_cgpa = df['CGPA'].mean()
print("Average CGPA of students:", average_cgpa)

#Conclusion: The average GPA of the students is 8.033184656556646