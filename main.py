import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns

# Read Physician info by county
df_phys = pd.read_excel('C:/Users/rmerr/Desktop/MSIS5193/2024_county_health_release_oklahoma_data_-_v1.xlsx', sheet_name='Select Measure Data')

# Select the desired rows and columns
df_phys = df_phys.iloc[2:81, [0, 2, 134, 135, 136, 137]]  # Assuming EE, EF, EG, EH
# Print the selected DataFrame
# print(df_phys)

# Read Health Outcomes
df_outcomes= pd.read_excel('C:/Users/rmerr/Desktop/MSIS5193/2024_county_health_release_oklahoma_data_-_v1.xlsx', sheet_name='Health Outcomes & Factors')
