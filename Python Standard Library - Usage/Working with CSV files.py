# In this program, we'll be working with CSV files.

import csv
from pathlib import Path

p1 = Path("file.csv")

# If the file doesn't exist, it'll create a new file and write to it.

if not p1.exists():
    with open(p1, "w") as csv_file:
        writer = csv.writer(csv_file)
        print("Writing started..", "\n")
        writer.writerow(["id", "name", "email", "contact_number"])
        writer.writerow(["1", "Steve Rogers", "captainamerica@avengers.com", "1800CAPTAINAVENGERS"])
        writer.writerow(["2", "Tony Stark", "ironman@avengers.com", "1800IRONAVENGERS"])
        print("Writing done.", "\n")

# Reading the CSV file after writing to it.
with open(p1, "r") as my_csv_file:
    print("Reading begins..", "\n")
    reader = csv.reader(my_csv_file)
    for a in reader:
        print(a)
    print("""
Reading done""")
