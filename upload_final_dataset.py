import pandas as pd

file_path = "newsroom_analysis_ready.csv.gz"

df = pd.read_csv(file_path)

print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nPublishers:")
print(df["publisher_clean"].value_counts().head(30))

print("\nYear distribution:")
print(df["year"].value_counts().sort_index())