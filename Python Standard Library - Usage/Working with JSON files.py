# Working with JSON files.

import json
from pathlib import Path

p1 = Path("file.json")

# If the file doesn't exist, creating a new json file and writing to it.
if not p1.exists():
    movies = [{"id": 1, "name": "Captain America"}, {"id": 2, "name": "Iron Man"}]
    data = json.dumps(movies)
    p1.write_text(data)

# Reading data from JSON files.
data = p1.read_text()
print(json.loads(data))
