# Gygax

Fiddling around with AI and D&D

The initial plan is to build a RAG model that has the description of every D&D monster in a vector database, and to enable this to answer questions about D&D monsters.

## Progress

- `fetch.py`: Fetched monster data from [Open5e API](https://api.open5e.com/v1/monsters/) and saved out to `data-raw/monsters_raw.json`
- `extract.py`: Concatenate the name and description fields for each monster in the JSON, returning a list of strings

## TODO

- Next step is to generate embeddings from these strings and save them into a vector database.