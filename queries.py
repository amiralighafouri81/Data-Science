import pandas as pd

# Read the CSV file into a DataFrame and drop rows with missing values
df = pd.read_csv("modified_people.csv").dropna()

# Count the frequency of each first name
first_name_counts = df['First Name'].value_counts()

print(first_name_counts)

Date_of_birth = df['Date of birth'].value_counts()

print(Date_of_birth)

job_title = df['Job Title'].value_counts()

print(job_title)

gender_counts_by_job_title = df.groupby(['Job Title', 'Sex']).size()

print(gender_counts_by_job_title)
