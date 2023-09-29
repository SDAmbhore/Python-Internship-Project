#Q16) Find the total number of students who attended the event related to Data Science (From all Data Science related courses)

import pandas as pd
import matplotlib.pyplot as plt
file_path = r'C:\Users\Sudhanshu\Desktop\IAC\Data analyst Data.xlsx'
df = pd.read_excel(file_path)

data_science_events = ['Data Visualization using Power BI', 'Artificial Intelligence', 'Hello ML and DL', 'IS DATA SCIENCE FOR YOU?']
data_science_attendees = df[df['Events'].isin(data_science_events)]

total_data_science_attendees = data_science_attendees.shape[0]
print("Total number of students who attended data science events:", total_data_science_attendees)

#Conclusion: Total 764 students have attended the event related to Data Science