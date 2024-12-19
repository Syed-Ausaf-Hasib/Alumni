import pandas as pd
import json

file_path = "Complete Data.xlsx"  
df = pd.read_excel(file_path)

df = df.rename(columns={
    "Name": "name",
    "Degree": "stream",
    "Branch": "branch",
    "RegNo": "rollNumber",
    "AdmissionBatch": "gradYear"
})

def calculate_grad_year(row):
    try:
        roll_year = int(''.join(filter(str.isdigit, row["rollNumber"][:4])))
        if "BACHELOR" in row["stream"].upper() or "BTECH" in row["stream"].upper() or "BE" in row["stream"].upper():
            return roll_year + 4
        else:
            return roll_year + 2
    except (ValueError, TypeError):
        return None

df["gradYear"] = df.apply(calculate_grad_year, axis=1)

data = df[["name", "stream", "branch", "rollNumber", "gradYear"]].to_dict(orient="records")

output_file = "output.json"
with open(output_file, "w") as f:
    json.dump(data, f, indent=4)

print(f"JSON file saved as {output_file}")
