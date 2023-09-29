#Q1- How many unique students are included in the dataset?

import pandas as pd
file_path = r'C:\Users\Sudhanshu\Desktop\IAC\Data analyst Data.xlsx'
df = pd.read_excel(file_path)

unique_students = df['First Name'].nunique()
print("Number of Unique Students:", unique_students)

#Conclusion: There are 2242 unique students are included in the dataset