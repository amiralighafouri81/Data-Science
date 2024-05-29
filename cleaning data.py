import pandas as pd

# cleaning data (null values)

# Read the CSV file into a DataFrame
df = pd.read_csv("people-500000.csv")

# Find null values and replace them with 'null' or 0
df.fillna({'Phone': 'null', 'OtherColumn': 0}, inplace=True)

# Save the DataFrame to a new CSV file
df.to_csv("modified_people.csv", index=False)

print("Modified DataFrame saved to modified_people.csv")
