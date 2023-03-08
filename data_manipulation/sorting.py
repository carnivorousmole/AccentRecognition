import json
import os

# Load the JSON file
with open('/Users/dylanwalsh/Code/AccentRecognition_Dylan/metadata2.json') as f:
    data = json.load(f)

# Define the name of the output file
output_file = "filtered_filenames.txt"

# Create a dictionary to store the counts for each value of english_residence
english_residence_counts = {}

# Create a list of tuples containing the key, original count, and filtered count
counts = []


# make a list of all the unique values of english_residence
english_residence_list = []
for key, sample_list in data.items():
    if isinstance(sample_list, list):
        for element in sample_list:
            if isinstance(element, dict) and "english_residence" in element:
                english_residence_list.append(element["english_residence"])

# remove duplicates
english_residence_list = list(set(english_residence_list))
# make everything lowercase
english_residence_list = [element.lower() for element in english_residence_list]
# separate any elements that have a comma in them into their indivdual elements
english_residence_list = [element.split(",") for element in english_residence_list]
# remove spaces from the beginning and end of each element
english_residence_list = [element.strip() for sublist in english_residence_list for element in sublist]
# replace some common errors
# english_residence_list = [element.replace("ausstralia", "australia") for element in english_residence_list]
# english_residence_list = [element.replace("wales", "uk") for element in english_residence_list]
# english_residence_list = [element.replace("scotland", "uk") for element in english_residence_list]
# english_residence_list = [element.replace("england", "uk") for element in english_residence_list]
# english_residence_list = [element.replace("england", "uk") for element in english_residence_list]
# english_residence_list = [element.replace("usq", "usa") for element in english_residence_list]
# english_residence_list = [element.replace("uk", "british") for element in english_residence_list]
# english_residence_list = [element.replace("ireland", "uk") for element in english_residence_list]

# remove duplicates again
english_residence_list = list(set(english_residence_list))
# remove any elements that contain a number
english_residence_list = [element for element in english_residence_list if not any(char.isdigit() for char in element)]
#remove any empty strings
english_residence_list = [element for element in english_residence_list if element != ""]

# Loop through every key-value pair in the dictionary
for language, sample_list in data.items():
    if isinstance(sample_list, list):
        # Count the number of elements in the original array
        original_count = len(sample_list)
        
        for country in english_residence_list:
            country_filtered_array = [sample for sample in sample_list if country in sample["english_residence"].lower()]
            english_residence_counts[country] = english_residence_counts.get(country, 0) + len(country_filtered_array)
        
        # Filter the array according to conditions
        filtered_array = [sample for sample in sample_list if "usa" in sample["english_residence"].lower()]

        # Count the number of elements in the filtered array
        filtered_count = len(filtered_array)

        # Add the language, original count, and filtered count to the list of counts
        counts.append((language, original_count, filtered_count))

        # Loop through every filtered element in the array
        for element in filtered_array:
            if isinstance(element, dict) and "file_location" in element:
                # Get the value of "file_location"
                file_location = element["file_location"]

                # Extract the file name without the path and remove the file extension
                filename = os.path.splitext(os.path.basename(file_location))[0]

                # Append the filename to the output file
                with open(output_file, "a") as f:
                    f.write(filename +".wav" +"\n")

# Sort the list of counts in descending order with respect to filtered count
counts.sort(key=lambda x: x[2], reverse=True)


# Print the sum of the original and filtered counts
original_count = sum([count[1] for count in counts])
filtered_count = sum([count[2] for count in counts])
print(f"Original count: {original_count}")
print(f"Filtered count: {filtered_count}")

# sort english_residence_counts by value
english_residence_counts = {k: v for k, v in sorted(english_residence_counts.items(), key=lambda item: item[1], reverse=True)}
# print english_residence_counts line by line
for key, value in english_residence_counts.items():
    print(f"{key}: {value}")
    
# Print a message to confirm that the file has been created
print(f"File names have been saved to {output_file}.")
