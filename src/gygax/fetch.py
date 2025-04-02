import requests

#fix later to get from all pages
def fetch_monster_data(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data from {url}. Status code: {response.status_code}")


base_url = "https://api.open5e.com/monsters/"

data = fetch_monster_data(base_url)

print(data)