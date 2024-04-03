#!/bin/bash

# Define environment name
ENV_NAME="ICCA_AttributeID_Solver"

# Create the Conda environment with required packages
conda create --name "$ENV_NAME" pandas sqlalchemy

echo "Conda environment '$ENV_NAME' created with required packages."
