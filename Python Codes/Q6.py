#Q6- How does GPA vary among different colleges? (Show top 5 results)

import pandas as pd
file_path = r'C:\Users\Sudhanshu\Desktop\IAC\Data analyst Data.xlsx'
df = pd.read_excel(file_path)

college_cgpa = df.groupby('College Name')['CGPA'].mean().sort_values(ascending=False).head(5)
print("Top 5 Colleges by Average CGPA:")
print(college_cgpa)

#Conclusion:
#Top 5 Colleges by Average CGPA:
#College Name
#THAKUR INSTITUTE OF MANAGEMENT STUDIES, CAREER DEVELOPMENT & RESEARCH - [TIMSCDR]: 8.638462
#St Xavier's College: 8.595000
#d y patil institute of mca and management akurdi pune: 8.522222
#Don Bosco College of Engineering Fatorda Goa: 8.376471
#AP SHAH INSTITUTE OF TECHNOLOGY: 8.360000

