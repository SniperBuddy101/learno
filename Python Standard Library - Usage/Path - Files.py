from pathlib import Path
from time import ctime
import shutil

# Creating a new path object.
nf_p = Path("file_2.txt")

# Writing text the file, it'll create a new file if it's not already present
nf_p.write_text("Merry Christmas!")

# Prints the stats of the path object.
print(nf_p.stat())

# Creating a new Path object
nf_np = Path("file_3.txt")

# Writing the text from nf_p to nf_np
nf_np.write_text(nf_p.read_text())
print(nf_p.read_text(), nf_np.read_text())

# Printing out the creation time of the file.
print(f"The creation time of file_2.txt is {ctime(nf_p.stat().st_ctime)}")

# Creating a copy with shutil

source = nf_p
target = Path() / "file_2_copy.txt"

shutil.copy(source, target)
