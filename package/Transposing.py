# Creating a reusable function to transpose a list.

def sk_transpose(*my_list):
    my_list = list(my_list)
    result = [[my_list[b][i] for b in range(len(my_list))] for i in range(len(my_list[0]))]
    return result


print(sk_transpose([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]))
