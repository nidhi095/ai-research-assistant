# utils.py

# Prefer json5 if available (allows comments, trailing commas), fallback to built-in json.
try:
    import json5 as json
except Exception:
    import json

import csv

def load_json(file_path: str):
    """Load and return data from a JSON/JSON5 file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_csv(file_path: str):
    """Load and return data from a CSV file as list of rows."""
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        return list(reader)

def clean_empty_rows(data):
    """Remove rows that are completely empty (all cells blank)."""
    return [row for row in data if any(str(cell).strip() for cell in row)]

def convert_to_float(data, col_idx: int):
    """Convert column values to float where possible, else None."""
    if not data:
        return data
    
    header, rows = data[0], data[1:]
    converted = []
    for row in rows:
        try:
            row[col_idx] = float(row[col_idx]) if row[col_idx] else None
        except (ValueError, IndexError):
            row[col_idx] = None
        converted.append(row)
    return [header] + converted
