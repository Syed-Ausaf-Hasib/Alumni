import pandas as pd
import json

# Load the Excel file
file_path = "Complete Data.xlsx"  # Replace with the actual file path
df = pd.read_excel(file_path)

# Rename and map the columns to the desired JSON format
df = df.rename(columns={
    "Name": "name",
    "Degree": "stream",
    "Branch": "branch",
    "RegNo": "rollNumber",
    "AdmissionBatch": "gradYear"
})

# Function to calculate graduation year
def calculate_grad_year(row):
    try:
        # Extract the first 4 digits from rollNumber (assumes year is the first 4 digits)
        roll_year = int(''.join(filter(str.isdigit, row["rollNumber"][:4])))
        # Add +4 years for Bachelor's degrees and +2 years for others
        if "BACHELOR" in row["stream"].upper() or "BTECH" in row["stream"].upper() or "BE" in row["stream"].upper():
            return roll_year + 4
        else:
            return roll_year + 2
    except (ValueError, TypeError):
        return None  # Handle invalid or missing roll numbers

# Apply graduation year calculation
df["gradYear"] = df.apply(calculate_grad_year, axis=1)

# Select relevant columns and convert to dictionary
data = df[["name", "stream", "branch", "rollNumber", "gradYear"]].to_dict(orient="records")

# Save to JSON file
output_file = "output.json"
with open(output_file, "w") as f:
    json.dump(data, f, indent=4)

print(f"JSON file saved as {output_file}")
