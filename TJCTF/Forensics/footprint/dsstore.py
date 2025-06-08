from ds_store import DSStore

with DSStore.open(".DS_Store", "r") as d:
    for entry in d:
        print(entry)
