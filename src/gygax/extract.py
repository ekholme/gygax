import os
import json

def extract_name_description(data: dict) -> str:
    """
    Extracts the 'name' and 'desc' field from a given dictionary and concatenates into a single string

    Args:
        data (dict): A dictionary containing the 'name' and 'desc' fields.

    Returns:
        A string containing the concatenated 'name' and 'desc' fields.
    """
    nm = data['name']
    desc = data['desc']
    return f"{nm}: {desc}"
    

d = json.load(open('data-raw/monsters_raw.json'))

res = [extract_name_description(i) for i in d]
