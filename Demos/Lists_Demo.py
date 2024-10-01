# INTRODUCTION TO LISTS

# Examples

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
planets = ["Jupiter", "Mars", "Venus"]
mixed = [1, "Jupiter", True, 4.5]
nested = [[1, 2], [3, 4]]
empty = []

# print a whole list
print(nums)
print(planets)

# printing specific items in a list
print(nums[0])
print(planets[2])

# Add elements to the end of a list with .append()
nums.append(11)
print(nums)
print(nums[10])

# Add elements to a list at a specific index and shift all other items over with .insert()
planets.insert(1, "Earth")
print(planets)

# Modify list at specific locations 
nums[1] = 222
print(nums)

# Delete specific values with .remove()
planets.remove("Jupiter")
print(planets)

# Delete values at a specific index with .pop()
planets.pop(0)
print(planets)


# ADVANCED SECTION

# Concatenating Lists

list1 = [1,2,3]
list2 = [4,5,6]

list3 = list1 + list2
print(list3)

# order matters!
rev_list = list2 + list1
print(rev_list)

# list2 is one data chunk, not separate ints (not concatenating!)
list1.append(list2)
print(list1)


# Slicing Lists: shortening a list
# inside brackets, put indexes -> [inclusive, exclusive]
numbers = [1,2,3,4,5,6,7,8]
print(numbers[1: 5])



