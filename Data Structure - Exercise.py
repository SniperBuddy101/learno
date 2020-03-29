org_sentence = "This is a common interview question"
sentence = org_sentence.upper()
print(sentence)
my_list_count = []
for x in sentence:
    if x != " ":
        my_list_count.append(sentence.count(x))

max_count = (max(my_list_count))
index_max = (my_list_count.index(max_count))
print(org_sentence[index_max])

# that_list = [(x[0], sentence.count(x[1])) for x in enumerate(sentence) if x[1] != " "]
# print(that_list)
# maxiumum = (max(that_list, key=lambda count: count[1]))
# print(f"The maximum times that a character occurs is {maxiumum[1]} and the character is {org_sentence[maxiumum[0]]} ")

# Generator class
Cool = "This is a cool one"

gen = (x for x in Cool)
for x in gen:
    print(x)
