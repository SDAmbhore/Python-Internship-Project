#Q7- Are there any outliers between “attending status” and “quantity (number of courses completed)” attribute?

import pandas as pd
import matplotlib.pyplot as plt
file_path = r'C:\Users\Sudhanshu\Desktop\IAC\Data analyst Data.xlsx'
df = pd.read_excel(file_path)


plt.figure(figsize=(6, 6))

# bar plot for the distribution of 'Attendee Status'
attendee_counts = df['Attendee Status'].value_counts(dropna=False)
attendee_counts.plot(kind='bar')
plt.title('Distribution of Attendee Status')
plt.xlabel('Attendee Status')
plt.ylabel('Count')

plt.tight_layout()
plt.show()

#Conclusion: There are no outliers between “attending status” and “quantity (number of courses completed)” attribute