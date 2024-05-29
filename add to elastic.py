from elasticsearch import Elasticsearch
import pandas as pd

# Connect to Elasticsearch
es = Elasticsearch("http://localhost:9200")

# Read the DataFrame from the CSV file and preprocess
df = (
    pd.read_csv("modified_people.csv")
    .dropna()  # Drop rows with missing values
    .reset_index(drop=True)  # Reset the index after dropping rows
)

# Index each row as a document in Elasticsearch
for i, row in df.iterrows():
    doc = {
        "index": row["Index"],  # Adding index attribute
        "user_id": row["User Id"],
        "first_name": row["First Name"],
        "last_name": row["Last Name"],
        "sex": row["Sex"],
        "email": row["Email"],
        "phone": row["Phone"],
        "date_of_birth": row["Date of birth"],
        "job_title": row["Job Title"]
    }
            
    es.index(index="users", id=i, document=doc)
