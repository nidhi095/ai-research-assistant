# utils/json_loader.py
import json

def load_json(file_path):
    """
    Load JSON file and return dictionary.
    """
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File {file_path} not found!")
        return {}
    except json.JSONDecodeError:
        print(f"Error decoding JSON in {file_path}!")
        return {}
