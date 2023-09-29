#Q15- Which promotion channel brings in more student participations for the event?

import pandas as pd
import matplotlib.pyplot as plt
file_path = r'C:\Users\Sudhanshu\Desktop\IAC\Data analyst Data.xlsx'
df = pd.read_excel(file_path)


df['First Promotion Channel'] = df['How did you come to know about this event?'].str.split('|').str[0]

# Calculate the count of each first promotion channel
promotion_channel_counts = df['First Promotion Channel'].value_counts()

# Display the count of each first promotion channel
print("First Promotion Channel Counts:")
print(promotion_channel_counts)

# Create a bar plot to visualize the distribution of student participation by the first promotion channel
plt.figure(figsize=(10, 6))
promotion_channel_counts.plot(kind='bar')
plt.title('Student Participation by First Promotion Channel')
plt.xlabel('Promotion Channel')
plt.ylabel('Number of Students')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#Conclusion: WhatsApp brings in more student participations for the event.

