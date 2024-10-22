import numpy as np



# use np arrays since they are faster and easier to do math with for arrays
arr = np.array([1]) 

# DEMO

# Adding Arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = arr1 + arr2
print(arr3)

# Appending Arrays
# structure -> np.append(array to append, what to append)
arr4 = np.append(arr1, arr2)
print(arr4)

# Subtracting Arrays
arr5 = arr2 - arr1
print(arr5)

# Indexing 1D Arrays
arr6 = arr1[1]
print(arr6)

# Slicing Arrays
my_arr = np.array([10, 20, 30, 40, 50, 60])
arr7 = my_arr[4:6] # or my_arr[4:]
print(arr7)

# NumPy Array Functions -> look them up!
sum = np.sum(my_arr)
print(sum)

std = np.std(my_arr)
print(std)

# Practice: Take the sum of numbers 1-100 in two ways: once with a for loop and once with arrays

# for loop
sum1 = 0
for i in range(101):
    sum1 += i
print(sum1)

# arrays
arr = np.arange(101)
sum2 = np.sum(arr)
print(sum2)

#2D Arrays
one_d = np.array([1, 2, 3])
two_d = np.array([[1, 2, 3], [4, 5, 6]])
print(two_d)

#.shape specifies dimensions of array in format (rows, columns)
print(one_d.shape)
print(two_d.shape)

# Accessing 2D Arrays
print(two_d[1, 1]) # 2nd row, 2nd column (index starts at 0)
print(two_d[1, : ]) # entire row
print([2, 5]) # columns