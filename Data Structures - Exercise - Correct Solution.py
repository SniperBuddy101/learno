sentence = "This is a common interview question"

this_dict = {}
for x in sentence:
    if x != " ":
        if x in this_dict:
            this_dict[x] += 1
        else:
            this_dict[x] = 1

sorted_dict = sorted(this_dict.items(), key=lambda this: this[1], reverse=True)
print(sorted_dict[0])
