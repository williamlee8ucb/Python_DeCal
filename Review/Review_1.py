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




# Problem 2: Prime Condition...

def isPrime(int):
    factors = []
    i = 1
    while i <= int:
        if int%i == 0:
            factors.append(i)
        i += 1
    
    if int == 1:
        return (int, True)
    if factors == [1, int]:
        return (int, True)
    else:
        return (int, False)

print(isPrime(13))