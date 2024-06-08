import json

path = "names.json"


def add_name(name: str) -> int:
    try:
        with open(path, "r") as file:
            names = json.load(file)
    except FileNotFoundError:
        names = []

    next_id = max((entry["id"] for entry in names), default=0) + 1
    names.append({"id": next_id, "name": name})

    with open(path, "w") as file:
        json.dump(names, file)

    return next_id


def get_names():
    try:
        with open(path, "r") as file:
            names = json.load(file)
    except FileNotFoundError:
        names = []

    names = [entry["name"] for entry in names]
    names.insert(0, '')
    return names


def get_ids():
    try:
        with open(path, "r") as file:
            names = json.load(file)
    except FileNotFoundError:
        names = []

    ids = [entry["id"] for entry in names]
    return ids
