# Creating an instance of the Path class.

from pathlib import Path

p1 = Path("/Users/shreyashkarnik/Documents")

print(p1.exists())
print(p1.is_dir(), "\n")

for p in p1.iterdir():
    print(p)

p1 = p1 / "Directory"
print("\n", p1.absolute())
print(p1.exists())
p1.exists()
