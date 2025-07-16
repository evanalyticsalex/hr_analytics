# Install dependencies with:
# pip install kaggle kagglehub pandas

import os
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set API config path (optional, useful if you had issues before)
os.environ['KAGGLE_CONFIG_DIR'] = os.path.join(os.getcwd(), '.kaggle')

# Set the path to the dataset file
file_path = "WA_Fn-UseC_-HR-Employee-Attrition.csv"

# Load the dataset using kagglehub
df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "pavansubhasht/ibm-hr-analytics-attrition-dataset",
  file_path,
)

print("First 5 records:\n", df.head())
