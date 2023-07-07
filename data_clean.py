import csv

# Specify the input and output file paths
input_file = 'all_NFL_players_ever.csv'
output_file = 'all_NFL_players_ever_real.csv'

# Specify the target column index (0-based)
target_column_index = 0

# Open the input and output files
with open(input_file, 'r') as csv_input, open(output_file, 'w', newline='') as csv_output:
    reader = csv.reader(csv_input)
    writer = csv.writer(csv_output)

    # Iterate over each row
    for row in reader:
        # Modify the target column by removing commas
        row[target_column_index] = row[target_column_index].replace(',', '')

        # Write the modified row to the output file
        writer.writerow(row)