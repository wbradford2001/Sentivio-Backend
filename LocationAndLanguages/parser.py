import csv

# File names for input and output
input_filename = 'locations_serp_google_2024_04_04.csv'
output_filename = 'output.csv'

# Open the input CSV file and create a reader object
with open(input_filename, mode='r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)  # Read the header row

    # Open the output CSV file and create a writer object
    with open(output_filename, mode='w', newline='') as outputfile:
        writer = csv.writer(outputfile)

        # Write the headers to the output file
        writer.writerow(headers)

        # Iterate over the rows in the input CSV
        for row in reader:
            if row[headers.index('location_type')] == 'Country':
                writer.writerow(row)  # Write only the rows with 'Country' in 'location_type'

print("Filtered data has been saved to 'output.csv'.")
