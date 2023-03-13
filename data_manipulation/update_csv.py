import pandas as pd

for filename in ["mfccs.csv", "filtered_mfccs.csv"]:
    # Load the CSV file into a DataFrame
    df = pd.read_csv(filename)
    print(df.head())

    # Update the "Path" column to extract the filename
    # catch the error if the column doesn't exist
    try:
        df["filename"] = df["path"].apply(lambda x: x.split("/")[-1])
        # Drop the original "Path" column
        df = df.drop("path", axis=1)
        # Save the updated DataFrame to a new CSV file
        df.to_csv(filename, index=False)
    except KeyError:
        print("Error: Path column not found")
        pass

