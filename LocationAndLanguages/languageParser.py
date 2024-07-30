import csv
import json

# The path to the input CSV file
input_filename = 'locations_serp_google_2024_04_04.csv'
# The path to the output JSON file
output_filename = 'UnitedStates.json'

# Initialize an empty list to store the JSON objects
languages_list = []
types = set()
count = 0
# Open the CSV file and create a reader object
with open(input_filename, mode='r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)  # Using DictReader for easy access by column header

    # Iterate over each row in the CSV file
    for row in reader:

        # Create a dictionary for the current language
        if row['country_iso_code']=="US":
            count += 1
        # Append the dictionary to the list
            types.add(row['location_type'])
            languages_list.append(row)

# Write the list of dictionaries to a JSON file
with open(output_filename, mode='w') as jsonfile:
    json.dump(languages_list, jsonfile, indent=4)
print(types, count)
print("Languages data has been saved to 'UnitedStates.json'.")
