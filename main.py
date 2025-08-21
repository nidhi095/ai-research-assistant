import csv
import numpy as np
from collections import Counter
from config import project_metadata
from utils import load_json


print("Project Author:", project_metadata["author"])
print("Version:", project_metadata["version"])
print("Features:", ", ".join(project_metadata["features"]))


class DataAnalyzer:
    def __init__(self, data):
        self.data = data
    
    def preview(self, rows=5):
        for row in self.data[:rows]:
            print(row)

    def unique_values(self, col_idx):
        """Return all unique values from a given column index."""
        if not self.data:
            return set()
        return set(row[col_idx] for row in self.data[1:] if len(row) > col_idx and row[col_idx])

    def summarize_column(self, col_idx):
        """Compute min, max, mean of a numeric column."""
        values = [float(row[col_idx]) for row in self.data[1:] if row[col_idx]]
        return {
            "min": min(values),
            "max": max(values),
            "mean": np.mean(values)
        }


def load_csv(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            data = list(csv.reader(csvfile))
            return data
    except FileNotFoundError:
        print("File not found!")
        return []


def column_mean(data, col_idx):
    values = [float(row[col_idx]) for row in data[1:] if row[col_idx]]
    return np.mean(values)


# ---- MAIN EXECUTION ----
print("\n--- Project Metadata ---")
for key, value in project_metadata.items():
    print(f"{key}: {value}")

# Load and preview CSV
data = load_csv("sample.csv")
analyzer = DataAnalyzer(data)
analyzer.preview()

# Show column mean
print("Average Age:", column_mean(data, 1))

# Extract words
words = []
for row in data:
    for cell in row:
        words.extend(cell.split())

# Word frequency
freq = Counter(words)
print(freq.most_common(10))

# Keyword search
sentences = [" ".join(row) for row in data]
keyword = input("Enter keyword to search: ")
matches = [s for s in sentences if keyword.lower() in s.lower()]
print(f"Found {len(matches)} matches:")
for m in matches:
    print("-", m)

# ---- Test unique values ----
print("\nUnique Ages:", analyzer.unique_values(1))
print("Unique Cities:", analyzer.unique_values(2))

# ---- JSON Data Handling ----
print("\nLoaded JSON data:")
json_data = load_json("sample.json")
print(json_data)

# Example: if JSON contains thresholds or metadata, use it
if "threshold" in json_data:
    threshold = json_data["threshold"]
    avg_age = analyzer.summarize_column(1)["mean"]
    print(f"\nThreshold from JSON: {threshold}")
    if avg_age > threshold:
        print("Average age exceeds threshold!")
    else:
        print("Average age is within safe range.")

# ---- Summary Stats ----
print("\nSummary of Ages:", analyzer.summarize_column(1))
