

#The code reads two CSV files,
#unique_values.csv and label_results.csv,
#and then merges them based on certain conditions.

#Specifically, it tries to match the 'Matching AttributeIds' from label_results.csv with the 'attributeId' column in unique_values.csv.
#However, it only keeps the rows from label_results.csv that do not have a corresponding match in unique_values.csv.

#The code identifies all values present in label_results.csv that are not present in unique_values.csv,
#based on the specified condition for the merge operation.
#These values are then stored in the resulting DataFrame as 'Extra AttributeIDs'.

import pandas as pd
import ast

# Read the CSV files
unique_values_df = pd.read_csv("unique_values.csv")
label_results_df = pd.read_csv("label_results.csv")

# Function to standardize the format of the 'Matching AttributeIds' column
def standardize_attributeIds(matching_ids):
    try:
        matching_ids = ast.literal_eval(matching_ids)
        if isinstance(matching_ids, int):  # Convert single integer to list
            matching_ids = [matching_ids]
        elif not isinstance(matching_ids, list):  # If not list or integer, set to empty list
            matching_ids = []
    except (ValueError, SyntaxError):  # Handle malformed data
        matching_ids = []
    return matching_ids

# Standardize the format of the 'Matching AttributeIds' column
label_results_df['Matching AttributeIds'] = label_results_df['Matching AttributeIds'].apply(standardize_attributeIds)

# Explode the 'Matching AttributeIds' column
exploded_df = label_results_df.explode('Matching AttributeIds')

# Merge with unique_values_df
merged_df = pd.merge(exploded_df, unique_values_df, left_on='Matching AttributeIds', right_on='attributeId', how='left')

# Remove rows where 'attributeId' column is not null
merged_df = merged_df[merged_df['attributeId'].isnull()]

# Drop duplicate rows based on 'Longlabel' column
merged_df.drop_duplicates(subset='Longlabel', inplace=True)

# Rename the last column to "Extra AttributeIDs"
merged_df.rename(columns={'Matching AttributeIds': 'Extra AttributeIDs'}, inplace=True)
merged_df.rename(columns={'attributeId': 'attributeId in Query'}, inplace=True)
# Save the final dataframe to a new CSV file
merged_df.to_csv("merged_results.csv", index=False)
