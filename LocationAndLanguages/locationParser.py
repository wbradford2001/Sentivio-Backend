import csv
import json

# The path to the input CSV file
input_filename = 'output.csv'
# The path to the output JSON file
output_filename = 'locations.json'

# Initialize an empty list to store the JSON objects
locations_list = []

# Open the CSV file and create a reader object
with open(input_filename, mode='r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)  # Using DictReader for easy access by column header

    # Iterate over each row in the CSV file
    for row in reader:
        # Create a dictionary for the current language
        location_entry = {
            "location_name": row['location_name'],
            "country_iso_code": row['country_iso_code'],
            "flag": row['country_iso_code']+ ".svg" 
        }
        # Append the dictionary to the list
        locations_list.append(location_entry)

# Write the list of dictionaries to a JSON file
with open(output_filename, mode='w') as jsonfile:
    json.dump(locations_list, jsonfile, indent=4)

print("Languages data has been saved to 'languages.json'.")
