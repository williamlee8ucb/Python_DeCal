# while loop: do something while a certain condition is true
    # make sure the condition eventually becomes false!
# Demo: print out "oink" 10 times
counter = 10

while counter > 0:
    print("oink")
    counter -= 1 # same as i - 1 = 1, prevents infinite loop

# if you accidentally have an infinite loop, hit ctrl + c

# for loop: iterate over an object a certain number of times and do a task
# Demo: find the sum of first 50 numbers (1-50)

sum_of_fifty = 0

for i in range (1, 51): # for ranges, last number is not included, so this goes from 1-50
    sum_of_fifty += i

print(sum_of_fifty)

# iterative for loop demo:

list_of_names = ['hanna', 'william', 'kalaia', 'taaha']

for name in list_of_names:
    print(len(name)) # make sure loop action is indented

# loops inside loops demo:

for i in range(2,5):
    for j in range (9,15): # goes through all j's for the i = 2 row, then all j's for the i = 3 row, etc.
        print((i, j))



