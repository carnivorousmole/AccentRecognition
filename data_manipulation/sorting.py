import json
import os

# Load the JSON file
with open('/Users/dylanwalsh/Code/AccentRecognition_Dylan/metadata.json') as f:
    data = json.load(f)

# Define the name of the output file
output_file = "filtered_filenames.txt"

# Create a list of tuples containing the key, original count, and filtered count
counts = []
for key, value in data.items():
    # Check if the value is an array
    if isinstance(value, list):
        # Count the number of elements in the original array
        original_count = len(value)
        # Filter the array to only include elements with english_residence equal to usa
        filtered_array = [element for element in value if isinstance(element, dict) and "english_residence" in element and element["english_residence"] == "usa"]
        # Count the number of elements in the filtered array
        filtered_count = len(filtered_array)
        # Add the key, original count, and filtered count to the list of counts
        counts.append((key, original_count, filtered_count))

# Sort the list of counts in descending order with respect to filtered count
counts.sort(key=lambda x: x[2], reverse=True)

# print the sum of the original and filtered counts
print(f"Original count: {sum([count[1] for count in counts])}")
print(f"Filtered count: {sum([count[2] for count in counts])}")

# Loop through the sorted list of counts and print the key, original count, and filtered count
for count in counts:
    print(f"{count[0]}: {count[1]} -> {count[2]}")

    # Loop through every filtered element in the array
    for element in data[count[0]]:
        # Check if the element is a dictionary with english_residence equal to usa
        if isinstance(element, dict) and "english_residence" in element and element["english_residence"] == "usa":
            # Get the value of "file_location"
            file_location = element["file_location"]
            # Extract the file name without the path and remove the file extension
            filename = os.path.splitext(os.path.basename(file_location))[0]
            # Append the filename to the output file
            with open(output_file, "a") as f:
                f.write(filename +".wav" +"\n")

# Print a message to confirm that the file has been created
print(f"File names have been saved to {output_file}.")
