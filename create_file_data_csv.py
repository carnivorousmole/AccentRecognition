import os
import csv
import re

def create_file_data_csv(directory_path):
    # Define the regex pattern to extract the language from the filename
    pattern = r"^(\D+)"

    # Create a list to store the file data
    file_data = []

    # Loop through all the files in the directory and its subdirectories
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            # Check if the file is a WAV file
            if file_name.endswith(".wav"):
                # Extract the language from the filename using the regex pattern
                language = re.match(pattern, file_name).group(1)
                # Get the full path of the file
                file_path = os.path.join(root, file_name)
                # Add the file path and language to the file data list
                file_data.append([language, file_path])

    # Define the output CSV file path
    output_path = os.path.join(directory_path, "file_data.csv")

    # Open the output CSV file for writing
    with open(output_path, "w", newline="") as csv_file:
        # Create a CSV writer object
        writer = csv.writer(csv_file)
        # Write the header row
        writer.writerow(["language", "filepath"])
        # Write the file data rows
        writer.writerows(file_data)

    # Return the path to the output CSV file
    return output_path
