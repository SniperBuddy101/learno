# Randomizing :)

import random

print(f"A random floating point number: {random.random()}")
print(f"A random integer: {random.randint(2, 56)}")
print(f"A random item from a list {random.choice([2, 3, 4, 'Yes'])}")
print(f"2 random items from a list {random.choices([5, 6, 7, 8, 9], k=2)}")

print(f"Joining items in an iterable: {'.'.join('Shreyash')}")
