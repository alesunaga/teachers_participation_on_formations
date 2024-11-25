# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style for better visualization aesthetics
sns.set(style="whitegrid")

# Import the dataset using the correct delimiter and encoding
# The dataset is loaded with semicolon (;) as the delimiter and 'latin1' encoding
teachers = pd.read_csv('teachers2.csv', sep=';', encoding='latin1')

# 1. Display basic information about the dataset
print("Dataset Overview:")
print(teachers.info())  # Prints the columns, data types, and non-null counts

# Print summary statistics for all columns
print("\nSummary Statistics:")
print(teachers.describe(include='all'))  # Summary statistics for numeric and non-numeric data

# 2. Handling missing values
# Checking for missing values in each column
print("\nMissing Values in Each Column:")
print(teachers.isna().sum())

# 3. Visualizing participation in different formations
# Plot the count of teachers who participated in each type of formation
plt.figure(figsize=(14, 6))
teachers.iloc[:, 3:].count().plot(kind='bar', color='skyblue')
plt.title("Number of Teachers Participating in Each Formation")
plt.xlabel("Formation Type")
plt.ylabel("Count of Participants")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 4. Participation by Segment
# Use countplot to visualize the number of teachers across each segment ('Segmento')
plt.figure(figsize=(10, 6))
sns.countplot(x='Segmento', data=teachers, order=teachers['Segmento'].value_counts().index, palette='viridis')
plt.title('Number of Teachers in Each Segment')
plt.xlabel('Segment')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. Participation by Unidade (School Unit)
# Visualize the number of teachers in each school unit
plt.figure(figsize=(10, 6))
sns.countplot(x='Unidade', data=teachers, order=teachers['Unidade'].value_counts().index, palette='Set2')
plt.title('Number of Teachers in Each Unidade')
plt.xlabel('Unidade')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6. Percentage of participation in each formation category
# Calculate the percentage of teachers participating in each formation category
participation_percentage = teachers.iloc[:, 3:].count() / len(teachers) * 100
print("\nPercentage of Participation in Each Formation Category:")
print(participation_percentage)

# Plot the participation percentage as a bar plot
plt.figure(figsize=(14, 6))
participation_percentage.plot(kind='bar', color='cadetblue')
plt.title("Percentage of Participation in Each Formation")
plt.xlabel("Formation Type")
plt.ylabel("Percentage of Participants")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
