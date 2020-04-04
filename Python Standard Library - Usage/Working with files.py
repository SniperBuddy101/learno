# In this program, we'll be working with files.

# Reading files
with open("file.txt", "r") as my_file:
    chunk = my_file.read(10)
    while len(chunk):
        print(chunk, end="")
        chunk = my_file.read(10)

# Writing to files
with open("file.txt", 'w') as write_file:
    for i in range(5):
        write_file.write("Wow \n")
