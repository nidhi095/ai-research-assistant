import csv
from collections import Counter

class DataAnalyzer:
    def __init__(self, data):
        self.data = data
    
    def preview(self, rows=5):
        for row in self.data[:rows]:
            print(row)


def load_csv(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            data = list(csv.reader(csvfile))
            return data
    except FileNotFoundError:
        print("File not found!")
        return []

# Test loading CSV
data = load_csv("sample.csv")

analyzer = DataAnalyzer(data)
analyzer.preview()


# Extract words from CSV data
words = []
for row in data:
    for cell in row:
        words.extend(cell.split())  # split by spaces

# Count most common words
freq = Counter(words)
print(freq.most_common(10))

# Create list of sentences (one sentence per CSV row joined together)
sentences = [" ".join(row) for row in data]

keyword = input("Enter keyword to search: ")
matches = [s for s in sentences if keyword.lower() in s.lower()]
print(f"Found {len(matches)} matches:")
for m in matches:
    print("-", m)

