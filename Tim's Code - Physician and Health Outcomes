import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns

# Read Physician info by county
df_phys = pd.read_excel('/Users/popsah/Documents/MSIS 5193/Project/2024_county_health_release_oklahoma_data_-_v1.xlsx', sheet_name='Select Measure Data')

# Select the desired rows and columns
df_phys = df_phys.iloc[2:81, [0, 2, 134, 135, 136, 137]]  # Assuming EE, EF, EG, EH
# Print the selected DataFrame
# print(df_phys)


# Read Health Outcomes
df_outcomes= pd.read_excel('/Users/popsah/Documents/MSIS 5193/Project/2024_county_health_release_oklahoma_data_-_v1.xlsx', sheet_name='Health Outcomes & Factors')

# Select the desired rows and columns
df_outcomes = df_outcomes.iloc[2:81, [3, 4, 5, 6]]  # Health Outcomes and Health Factors (Z-score and ranges)

# print(df_outcomes)

###############################################
### Combine Physician data and Outcome data ###

df = pd.concat([df_phys, df_outcomes], axis=1)

# Rename Columns
df.columns = ['FIPS', 'County', 'PCP', 'PCP per 100k', 'PCP Ratio','PCP z-score','Outcomes','OutcomesRange','Factors','FactorsRange']
print(df)
# df.to_csv(f"/Users/popsah/Downloads/projtest1.csv", index=False, encoding='utf-8')



# Basic scatter plot
plt.scatter(df['Outcomes'], df['Factors'])
plt.xlabel('Outcomes')
plt.ylabel('Factors')
plt.title('Scatter Plot')
plt.show()

print('Correlation for Outcomes vs Factors')
# Pearson correlation coefficient
correlation = df['Outcomes'].corr(df['Factors'])
print('Pearson correlation coefficient:', correlation)

# Spearman correlation coefficient (for non-linear relationships)
correlation_spearman = df['Outcomes'].corr(df['Factors'], method='spearman')
print('Spearman correlation coefficient:', correlation_spearman)

print()
print('Correlation for PCP per 100k vs Outcomes')
# Pearson correlation coefficient
correlation = df['PCP per 100k'].corr(df['Outcomes'])
print('Pearson correlation coefficient:', correlation)

# Spearman correlation coefficient (for non-linear relationships)
correlation_spearman = df['PCP per 100k'].corr(df['Outcomes'], method='spearman')
print('Spearman correlation coefficient:', correlation_spearman)
