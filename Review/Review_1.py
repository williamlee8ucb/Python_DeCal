# REVIEW 1

# Problem 1: Changing It Up

list = [1,5, "hello world", 6, "oink"]

new_dict = {}

for i in list:
    if type(i) == int:
        powers = []
        for r in range(4):
            powers.append(i**r)
        new_dict[i] = powers
    else:
        repeat = []
        for k in range(4):
            repeat.append(i)
        new_dict[i] = repeat

print(new_dict)


# Problem 2: Prime Condition...
