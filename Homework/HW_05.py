
# HOMEWORK 5: NUMPY ARRAYS

import numpy as np

# 1) The Odd Ones Out

def onlyOdd(arr):
    arr1 = np.array(arr)
    odd_arrs = np.empty((0, arr1.shape[1]), int)
    for j in range(len(arr1)):
        if all(x % 2 == 1 for x in arr1[j]):
            odd_arrs = np.append(odd_arrs, [arr1[j]], axis = 0)
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
