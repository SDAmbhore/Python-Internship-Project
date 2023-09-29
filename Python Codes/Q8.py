#Q8- What is the average GPA for student from each city?

import pandas as pd
file_path = r'C:\Users\Sudhanshu\Desktop\IAC\Data analyst Data.xlsx'
df = pd.read_excel(file_path)

city_cgpa = df.groupby('City')['CGPA'].mean()
print("Average CGPA for Students from Each City:")
print(city_cgpa)

#Conclusion:
#Average CGPA for Students from Each City (Top 5):
#City
#Agartala: 8.100000
#Agra: 8.283333
#Ahmedabad: 8.245455
#Ajmer: 8.316667
#Akola: 7.975000

