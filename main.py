import numpy as np
import csv
from collections import Counter

# =====================
# Class for analyzing data
# =====================
class DataAnalyzer:
    def __init__(self, data):
        self.data = data
    
    def preview(self, rows=5):
        """Print the first few rows of the dataset."""
        for row in self.data[:rows]:
            print(row)

# =====================
# Function to load CSV
# =====================
def load_csv(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            data = list(csv.reader(csvfile))
            return data
    except FileNotFoundError:
        print("File not found!")
        return []

# =====================
# Function to calculate column mean using NumPy
# =====================
def column_mean(data, col_idx):
    """Calculate mean of a numeric column (excluding header)."""
    values = [float(row[col_idx]) for row in data[1:] if row[col_idx]]
    return np.mean(values)

# =====================
# Main Program
# =====================

# 1. Load CSV
data = load_csv("sample.csv")

# 2. Preview data
analyzer = DataAnalyzer(data)
analyzer.preview()

# 3. Calculate and print mean of Age column (index 1)
print("Average Age:", column_mean(data, 1))

# 4. Extract words from CSV data
words = []
for row in data:
    for cell in row:
        words.extend(cell.split())  # split by spaces

# 5. Count most common words
freq = Counter(words)
print(freq.most_common(10))

# 6. Keyword search
sentences = [" ".join(row) for row in data]
keyword = input("Enter keyword to search: ")
matches = [s for s in sentences if keyword.lower() in s.lower()]
print(f"Found {len(matches)} matches:")
for m in matches:
    print("-", m)
