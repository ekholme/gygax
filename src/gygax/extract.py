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

def clean_monster_text(data: list[dict]) -> list[str]:    
    """
    Extracts 'name' and 'desc' fields from a given dictionary, concatenates each into a single string, and returns a list of these strings. Strings with fewer than 10 words are excluded
    
    Args:
        data (list[dict]): A list of dictionaries containing the 'name' and 'desc' fields.

    Returns:
        A list of strings containing the concatenated 'name' and 'desc' fields.
    """

    tmp = [extract_name_description(i) for i in data]
    ret = [i for i in tmp if len(i.split()) > 10]
    return ret

d = json.load(open('data-raw/monsters_raw.json'))

monster_txt = clean_monster_text(d)

#save out as json
with open('data/monster_descriptions.json', 'w') as f:
    json.dump(monster_txt, f, indent=4)
