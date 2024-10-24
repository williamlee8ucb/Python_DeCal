# HOMEWORK 4: LISTS AND DEBUGGING

# 1) DEBUGGING

def first_fifteen_elements(list):
    return list[0 : 15]
"""
I originally sliced using list[0 : 16] since I thought that the last element was exclusive. However, because 0 
was included in the slice, this actually returned the first 16 elements. I fixed the code to list[0:15] and it worked
"""

def every_fifth_element(list):
    return list[4:len(list):5]
"""
I originally had list [0:len(list):5]. I confused indexes with elements and forgot that we should not include the first element
in the list since we want every fifth element. I changed the code to list[4:len(list):5] to start at index 4, which is the fifth 
element, then go to the end of the list with a step size of 5 to get the appropriate output
"""
def create_2d_list():
    matrix = []
    count = 1
    for row in range(5):
        row = []
        for i in range(5):
            row.append(count)
            count += 1
        matrix.append(row)
    return matrix
"""
I originally had a nested for loop with row[column].append(count) on the innermost for loop and nothing on the outermost for loop. I got
an Index Error, and that was when I realized I was trying to append a value to the list at a location that didn't exist. I changed the code 
to the above after a google search to resolve this issue. 
"""


# 2) PRACTICING SLICING AND STRIDING


# 2.1: Making a List Variable
list_to_twenty = []
for i in range(21):
    list_to_twenty.append(i)
print(list_to_twenty)


#2.2: Working With List Elements

def squareList(list):
    squared_list = []
    for num in list:
        squared_list.append(num**2)
    return squared_list

squared_twenty_list = squareList(list_to_twenty)
print(squared_twenty_list)


# 2.3: Slicing

def first_fifteen_elements(list):
    return list[0 : 15]

print(first_fifteen_elements(list_to_twenty))


# 2.4: Striding

def every_fifth_element(list):
    return list[4:len(list):5]

print(every_fifth_element(squared_twenty_list))

# 2.5: Slicing and Striding
def fancy_function(list):
    last_30 = list[-30::]
    return last_30[::-3]

print(fancy_function(squared_twenty_list))



# 3) 3D LISTS

# 3.1: Creating a 5x5 2D List

def create_2d_list():
    matrix = []
    count = 1
    for row in range(5):
        row = []
        for i in range(5):
            row.append(count)
            count += 1
        matrix.append(row)
    return matrix

matrix = create_2d_list()
print(matrix)


# 3.2: Replacing 2D List with Multiples of 3

def modified_2d_list(matrix):
    for j in range(len(matrix)):
        for k in range(len(matrix[j])):
            if matrix[j][k] % 3 == 0:
                matrix[j][k] = "?"
    return matrix

modded = modified_2d_list(matrix)
print(modded)


# 3.3: Summing None- "?" Elements
def sum_non_question_elements(matrix):
    sum = 0
    for j in range(len(matrix)):
        for k in range(len(matrix[j])):
            if matrix[j][k] != "?":
                sum += matrix[j][k]
    return sum

print(sum_non_question_elements(modded))