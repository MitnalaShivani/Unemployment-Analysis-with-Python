import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('unemployment_in_india.csv')

# Convert the 'Year' column to datetime format
df['Year'] = pd.to_datetime(df['Year'])

# Set the 'Year' column as the index
df.set_index('Year', inplace=True)

# Calculate the unemployment rate
df['Unemployment Rate'] = df['Unemployed'] / df['Labour Force'] * 100

# Plot the unemployment rate over time
plt.figure(figsize=(10, 6))
sns.lineplot(x=df.index, y=df['Unemployment Rate'])
plt.title('Unemployment Rate in India (2015-2020)')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate (%)')
plt.show()
