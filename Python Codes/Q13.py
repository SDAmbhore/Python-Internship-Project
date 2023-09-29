#Q13- Is there a correlation between leadership skills and expected salary of the students?

import pandas as pd
from scipy.stats import mannwhitneyu
file_path = r'C:\Users\Sudhanshu\Desktop\IAC\Data analyst Data.xlsx'
df = pd.read_excel(file_path)

yes_salary = df[df['Leadership- skills'] == 'Yes']['Expected salary (Lac)']
no_salary = df[df['Leadership- skills'] == 'No']['Expected salary (Lac)']

# Check if either group has zero size
if len(yes_salary) == 0 or len(no_salary) == 0:
    print("One of the groups has zero size. Cannot perform the test.")
else:
    # Perform the Mann-Whitney U test
    statistic, p_value = mannwhitneyu(yes_salary, no_salary, alternative='two-sided')

    print("Mann-Whitney U Test Results:")
    print("Statistic:", statistic)
    print("P-value:", p_value)

    # Determine if the result is statistically significant
    alpha = 0.05
    if p_value < alpha:
        print("There is a statistically significant difference.")
    else:
        print("There is no statistically significant difference.")

#Conclusion: No. There is no statistically significant difference.