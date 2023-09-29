#Q5- What is the average family income of the student?

import pandas as pd
file_path = r'C:\Users\Sudhanshu\Desktop\IAC\Data analyst Data.xlsx'
df = pd.read_excel(file_path)

income_mapping = {
    '0-2 Lakh': 2.0,
    '2-5 Lakh': 5.0,
    '5-7 Lakh': 7.0,
    '7 Lakh+': 7.0  # Consider '7 Lakh+' as 7
}

# use mapping to the 'Family Income' column
df['Family Income'] = df['Family Income'].map(income_mapping)

average_family_income = df['Family Income'].mean()

# Round the average to the nearest 
rounded_average_income = int(average_family_income)

# result
if rounded_average_income == 2:
    print("Average Family Income: 2 lakh")
elif rounded_average_income == 5:
    print("Average Family Income: 5 lakh")
elif rounded_average_income == 7:
    print("Average Family Income: 7 lakh")
else:
    print(f"Average Family income of the student: {rounded_average_income} lakhs")

#Conclusion: The average family income of the student is 2 lakhs