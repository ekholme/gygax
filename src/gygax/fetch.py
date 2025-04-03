import requests
import json
import os

base_url = "https://api.open5e.com/monsters/"

def fetch_all_data(base_url: str):
    """
    Fetches all data from a given Open5e API endpoint by recursively following the 'next' links.

    Args:
        base_url (str): The base URL of the API endpoint.
        
    Returns:
        A list of dictionaries containing the fetched data
    """
    all_data = []
    next_url = base_url
    
    while next_url:
        try:
            response = requests.get(next_url)
            response.raise_for_status()

            data = response.json()
            all_data.extend(data['results'])
            next_url = data['next']
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {next_url}: {e}")
            return []
        
        except ValueError as e:
            print(f"Error decoding JSON from {next_url}: {e}")
            return []
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return []
    
    return all_data


def save_to_json(data: list[dict], filepath: str):
    """
    Saves a list of dictionaries out as JSON to a given filepath.

    Args:
        data (list[dict]): A list of dictionaries to be saved
        filepath (str): The filepath to save the data to.
    """
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to {filepath}")
    except (TypeError, OSError) as e:
        print(f"Error saving data to {filepath}: {e}")

# fetch monster data and save to disk
rr = fetch_all_data(base_url)

save_to_json(rr, 'data-raw/monsters_raw.json')