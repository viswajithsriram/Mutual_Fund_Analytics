import pandas as pd
import os

data_folder = "data/raw"

for file in os.listdir(data_folder):
    if file.endswith(".csv"):
        file_path = os.path.join(data_folder, file)

        df = pd.read_csv(file_path)

        print("\nDataset:", file)
        print("Shape:", df.shape)
        print("Data Types:")
        print(df.dtypes)
        print("First 5 Rows:")
        print(df.head())

print("\nData ingestion completed!")