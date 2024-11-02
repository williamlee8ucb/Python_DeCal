
# HOMEWORK 5: NUMPY ARRAYS

import numpy as np

# 1) The Odd Ones Out

def onlyOdd(arr):
    odd_arrs = np.array([])
    for j in arr:
        if np.all(j % 2 != 0):
            odd_arrs = np.append(odd_arrs, [j])
    return odd_arrs

arr = np.array([[1, 2, 3], [5, 7, 9], [2, 4, 6], [7, 7, 7]])
print(onlyOdd(arr))


# 2) Let's Play Checkers!

# 2.1:
def checkerboard():
    return np.zeros((8,8))

board = checkerboard()
print(board)

# 2.2:
def checkerboard1():
    board = np.zeros((8,8))
    for j in range(len(board)):
        if j % 2 == 0:
            for k in range(len(board[j])):
                if k % 2 == 0:
                    board[j][k] = 1
    return board

board1 = checkerboard1()
print(board1)

# 2.3:
def checkerboard2():
    board = np.zeros((8,8))
    for j in range(len(board)):
        if j % 2 == 0:
            for k in range(len(board[j])):
                if k % 2 == 0:
                    board[j][k] = 1
        if j % 2 == 1:
            for k in range(len(board[j])):
                if k % 2 == 1:
                    board[j][k] = 1
    return board
board2 = checkerboard2()
print(board2)

# 2.4:
def reverse_checkerboard():
    board = np.zeros((8,8))
    for j in range(len(board)):
        if j % 2 == 1:
            for k in range(len(board[j])):
                if k % 2 == 0:
                    board[j][k] = 1
        if j % 2 == 0:
            for k in range(len(board[j])):
                if k % 2 == 1:
                    board[j][k] = 1
    return board

reverse_board = reverse_checkerboard()
print(reverse_board)


# 3) The Expanding Universe

def expansion(phrase, spaces):
    expanded_words = []
    for word in phrase:
        expanded = ""
        for char in word:
            expanded = expanded + char + " " * spaces
        expanded_words.append(expanded)

    return expanded_words

universe = np.array(["galaxy", "clusters"])
print(expansion(universe, 2))


# 4) 

def secondLargest(planets):
    planets = np.transpose(planets)
    list_seconds = []
    for system in planets:
        planets.sort()
        list_seconds.append(system[len(planets)-2])
    return list_seconds

np.random.seed(42)
planets = np.random.randint(100, 1000, (5, 5))
print(planets)
print(secondLargest(planets))



