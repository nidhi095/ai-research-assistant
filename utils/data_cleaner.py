# utils/data_cleaner.py

def clean_empty_rows(data):
    """
    Remove empty rows from CSV data.
    Each row is a list of cells.
    """
    return [row for row in data if any(cell.strip() for cell in row)]


def convert_to_float(data, col_idx):
    """
    Convert values in a column to float.
    Skips header (assumes first row is header).
    """
    for row in data[1:]:
        try:
            row[col_idx] = float(row[col_idx])
        except (ValueError, IndexError):
            row[col_idx] = 0.0
    return data
