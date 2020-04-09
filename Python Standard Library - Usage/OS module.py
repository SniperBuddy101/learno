# Working with the os module

import os

print(os.listdir())
os.chdir("Python Project")
print(os.listdir())

print(os.path.basename("Python Project/Abstract methods.py"))
print(os.getcwd().split("/"))
