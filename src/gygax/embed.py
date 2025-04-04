import os
import json
import sys

#having to monkey patch sqlite3
try:
    import pysqlite3 as sqlite3_override
except ImportError:
    sqlite3_override = None

if sqlite3_override:
    sys.modules['sqlite3'] = sqlite3_override
    print(f"Replaced bundled sqlite3 with pysqlite3 version: {sqlite3_override.sqlite_version}")
else:
    import sqlite3
    print(f"Using bundled sqlite3 version: {sqlite3.sqlite_version}")

from chromadb import Documents, EmbeddingFunction, Embeddings
import chromadb

#load in monster description data
d = json.load(open('data/monster_descriptions.json'))

#creating DB
DB_NAME = 'gygax_vector_db'

chroma_client = chromadb.PersistentClient(path=DB_NAME)

# creating a collection using chroma's default embedding function
monster_collection = chroma_client.get_or_create_collection(name='monsters')

# add documents to the collection
monster_collection.add(
    documents=d,
    ids=[str(i) for i in range(len(d))]
)

#testing out querying
res = monster_collection.query(
    query_texts=["Find some examples of adult dragons"],
    n_results = 5
)

print(res['documents'][0][0])

# this doesn't use google tools for now -- only chroma.
