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

# Create a column 'ABSENT_LABELS' with NaN values
merged_df['ABSENT_LABELS'] = pd.NA

# Get labels present in label_results but absent in unique_values
absent_labels = label_results_df[~label_results_df['Matching AttributeIds'].isin(unique_values_df['attributeId'])][['Longlabel', 'Matching AttributeIds']]

for index, row in merged_df.iterrows():
    if index in absent_labels.index:
        merged_df.at[index, 'ABSENT_LABELS'] = absent_labels.loc[index, 'Matching AttributeIds']

# Save the final dataframe to a new CSV file
merged_df.rename(columns={'Matching AttributeIds': 'Absent_AttributeIds', 'attributeId': 'ignore', 'ABSENT_LABELS': 'Other_labels'}, inplace=True)

merged_df.to_csv("merged_results.csv", index=False)
