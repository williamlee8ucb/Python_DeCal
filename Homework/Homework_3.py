# HOMEWORK 3: DATA TYPES, FUNCTION, CONDITIONALS, AND LOOPS

# 1) Oski Stole Your Power
def computePower(x, y):
    base = x
    for i in range(y - 1):
        x *= base
    return x



# 2) What Should I Wear?
def temperatureRange(readings):
    return (min(readings), max(readings))



# 3) Check if its the Weekend
def isWeekend(day):
    if day == 6 or day == 7:
        return True
    else:
        return False



# 4) Fuel Efficiencey Calculator
def fuel_efficiency(distance, fuel):
    return distance/fuel



# 5) Secret Code
def decodeNumbers(n):
   n_last_removed = n//10 
   last_digit = n%10 
   
   power = 0
   divide = n
   while divide > 10:
       divide /= 10
       power += 1

   return n_last_removed + (last_digit*(10**(power)))



# 6.1) Min & Max with For Loops

# min
def find_min_with_for_loop(nums):
    absolute_min = nums[0]
    current_min = nums[0]

    for i in nums:
        if i < current_min:
            current_min = i
            if current_min < absolute_min:
                absolute_min = i
    return absolute_min

# max
def find_max_with_for_loop(nums):
    absolute_max = nums[0]
    current_max = nums[0]

    for i in nums:
        if i > current_max:
            current_max = i
            if current_max > absolute_max:
                absolute_max = i
    return absolute_max



# 6.2) Min & Max with While Loops

# min
def find_min_with_while_loop(nums):
    absolute_min = nums[0]
    current_min = nums[0]

    i = 0

    while i < len(nums):
        if nums[i] < current_min:
            current_min = nums[i]
            if current_min < absolute_min:
                absolute_min = nums[i]
        i += 1
    return absolute_min

# max
def find_max_with_while_loop(nums):
    absolute_max = nums[0]
    current_max = nums[0]

    i = 0

    while i < len(nums):
        if nums[i] > current_max:
            current_max = nums[i]
            if current_max > absolute_max:
                absolute_max = nums[i]
        i += 1
    return absolute_max



# 7) Counting Vowels
def vowel_and_consonant_count(text):
    lower = text.lower()
    num_vowels = 0
    num_consonants = 0
    for i in lower:
        if i.isalpha():
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                num_vowels += 1
            else:
                num_consonants += 1
    
    return (num_vowels, num_consonants)



# 8) Calculate Digital Root
def digital_root(num):
    d_root = 0
    for digit in str(num):
        d_root += int(digit)
    return d_root








