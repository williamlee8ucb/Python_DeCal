### This is the syntax of a for-loop ###

#for variable in range(start, stop, step):
    # Code block to be executed

### This is the syntax of a while-loop ###

#while condition == true:
    # Code block to be executed


# Note: It is normal to forget the syntax! That is why google is your bff and you just need to google "for loop syntax" or "while loop syntax"
# and there are tons of resources. I usually just go to images to quickly check the syntax.


'''### Problem 1: Your turn!

Print i 10 times using both a for and while loop.'''

for i in range(1,11):
    print('i', i) # comma means stick string and number into a combined string

print("break")

n = 1
while n < 11:
    print('n', n) 
    n += 1

print("break")

'''###Problem 2: Range()
Range is a cool function but there are a lot of parts to it so let's disect it!

What happens if the range is from (5, 5)?  How about from (10, 6)?  
Try different step sizes: (10, 6, -1), (1, 10, 2). Write down all your observations and answer the following questions.'''

for i in range(5,5):
    print("yes")
# the size of the range is 0, so nothing would be printed
print("Length: " + str(len(range(5,5))))
print("break")

for i in range(10,6):
    print(i)
# nothing is printed. I assume that the range function does not recognize this range because start is greater than stop,
# and it goes in ascending order.

print("Length: " + str(len(range(10,6))))
print("break")

for i in range(10,6,-1):
    print(i)
# The range is created with step -1, so now a range is created counting backwards from 10 to but not including 6

print("break")

for i in range (1,10,2):
    print(i)
# A range is created from 1 to 9 but increasing by 2 each step instead of the default 1.

print("break")
'''### Problem 3: Listness 

How do you loop through elements in a list using a for loop? '''

list = ["1","2","3","4","5"]

for element in list:
    print(element)

