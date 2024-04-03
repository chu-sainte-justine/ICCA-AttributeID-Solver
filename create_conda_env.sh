#!/bin/bash

# Define environment name
ENV_NAME="ICCA_AttributeID_Solver"

# Create the Conda environment with packages listed in requirements.txt
conda create --name "$ENV_NAME" --file requirements.txt

echo "Conda environment '$ENV_NAME' created with packages from requirements.txt."
