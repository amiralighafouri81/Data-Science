from elasticsearch import Elasticsearch
import pandas as pd


es = Elasticsearch("http://localhost:9200")

df = (
    pd.read_csv("wiki_movie_plots_deduped.csv")
    .dropna()
    .sample(5000, random_state=42)
    .reset_index()
)

for i, row in df.iterrows():
    doc = {
        "title": row["Title"],
        "ethnicity": row["Origin/Ethnicity"],
        "director": row["Director"],
        "cast": row["Cast"],
        "genre": row["Genre"],
        "plot": row["Plot"],
        "year": row["Release Year"],
        "wiki_page": row["Wiki Page"]
    }
            
    es.index(index="movies", id=i, document=doc)