import pandas as pd

df = pd.read_csv("dm-lab-2-private-competition/submission_distilbert_weighted.csv")

df = df.rename(columns={"post_id": "id"})

df.to_csv("dm-lab-2-private-competition/submission_distilbert_weighted.csv", index=False)

print(df.head())
