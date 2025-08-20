# utils.py
# Prefer json5 if available (allows comments, trailing commas), fallback to built-in json.
try:
    import json5 as json
except Exception:
    import json

def load_json(file_path: str):
    """Load and return data from a JSON/JSON5 file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
