# We'll be working with zip files in this program.

from zipfile import ZipFile
from pathlib import Path

path_object = Path()

with ZipFile("zip_file.zip", "w") as zip_file:
    for i in path_object.rglob("*.*"):
        zip_file.write(i)
    print(zip_file.namelist())

with ZipFile("zip_file.zip", "r") as zip_file:
    print(zip_file.namelist())
    info_object = zip_file.getinfo("Path - Directories.py")
    print(info_object.file_size, info_object.compress_size)
    zip_file.extractall("extracted_zip")
