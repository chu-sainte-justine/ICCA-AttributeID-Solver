In order to run this code you must:

1. Setup a python environment with access to the libraries listed in requirements.txt by running:
   `chmod +x create_conda_env.sh` if necessary, and then
   `./create_conda_env.sh`
   
2. Run, in order:
  1. python unique_variables_extraction.py
  2. python refresh_variables.py
  3. python compare.py

A CSV file is generated after every step, resulting in 3 csv files:
unique_values.csv - a file containing a list of the unique values in the SQL query.
label_results.csv - a file containing a list of the corresponding Longlabels and their matching AttributeIds.
merged_results.csv - a file containing a list of the extra AttributeIds that were not present in the original SQL query.
