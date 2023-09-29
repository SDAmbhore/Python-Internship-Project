#Q18- How many students know about these events from their colleges? Which of these top 5 colleges?

import pandas as pd
file_path = r'C:\Users\Sudhanshu\Desktop\IAC\Data analyst Data.xlsx'
df = pd.read_excel(file_path)

college_name_column = 'College Name'
event_source_column = 'How did you come to know about this event?'


college_sources = ['SPOC/ College Professor', 'College']

# Filter the data 
college_students = df[df[event_source_column].isin(college_sources)]

# Count the occurrences 
college_counts = college_students[college_name_column].value_counts()

# top 5 colleges
top_5_colleges = college_counts.head(5)

# Display the top 5 colleges
print("Top 5 Colleges with Students Knowing About the Event from Their College:")
print(top_5_colleges)

#Conclusion: Top 5 Colleges with Students Knowing About the Event from Their College:
#kle society's college of bca, rls institute, belagavi: 10
#mit academy of engineering ,alandi: 7
#symbiosis institute of technology, pune: 7
#dkte society's textile and engineering institute ichalkaranji: 7
#adhiyamaan college of engineering: 6
