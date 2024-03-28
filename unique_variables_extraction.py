import re
import csv

# Read SQL query from file
with open("/path/to/query.sql", "r") as file:
    sql_query = file.read()

# Find matches in the SQL query
matches = re.findall(r'attributeId\s*IN\s*\((\d+(?:,\s*\d+)*)\)|attributeId\s*=\s*(\d+)', sql_query, re.IGNORECASE)
print('Total matches found:', len(matches))
# Flatten the list of tuples and split comma-separated values
values = [value.split(',') for match in matches for value in match if value]

# Convert values to integers and create a set of unique values
unique_values = set(int(val) for sublist in values for val in sublist)

print('unique_values:{',unique_values,'}')
print('total unique_values:{',len(unique_values),'}')

# Write unique values to a CSV file
with open("unique_values.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["attributeId"])  # Write header
    for value in unique_values:
        writer.writerow([value])