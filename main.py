import csv

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
print(data)
