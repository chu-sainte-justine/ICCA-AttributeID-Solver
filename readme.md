## Description: 
### Objective:
The objective of this code is to identify all attributeID values present in an SQL query, and then log them into a `unique_values.csv` file that will be used to query an SQL server to find other values that correspond to the same `longlabel` description. This query is then saved to the `label_results.csv` file. These two files are then compared to produce a `merged_results.csv` file that contains all the extra updated values that were not present in your original query.

### Necessary Libraries:
   - The code imports the required libraries:
     - `pandas`: For data manipulation and analysis.
     - `sqlalchemy`: For communications with an SQL server.
     - `csv`: For csv files (comes with Python).
     - `ast`: For literal evaluation of strings to Python objects (comes with Python) ([read this](https://stackoverflow.com/questions/15197673/using-pythons-eval-vs-ast-literal-eval))
       
---

## Setup
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
