import json
from typing import Sequence

with open("data.json", "r") as handle:
    data = json.load(handle)

    print(type(data))

    for elem in data:
        print(f'{elem["id"]}\t{elem["sequence"]}\t{elem["species"]}')
