from time import time


def iterations(list_structure):
    for i in list_structure:
        print(i)


start = time()

iterations([1, 2, 3, 4, 5, 6, 7, 8, 9])

end = time()
time_to_run_the_function = end - start
print(time_to_run_the_function)
