import json

def remove_keys(obj, keys_to_remove):
    if isinstance(obj, dict):
        return {
            k: remove_keys(v, keys_to_remove)
            for k, v in obj.items()
            if k not in keys_to_remove
        }
    elif isinstance(obj, list):
        return [remove_keys(item, keys_to_remove) for item in obj]
    else:
        return obj


with open("data/quaesta.json") as f:
    data = json.load(f)

keys_to_remove = {"source", "content_length"}

cleaned = remove_keys(data, keys_to_remove)

with open("data/output.json", "w") as f:
    json.dump(cleaned, f, indent=2)