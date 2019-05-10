#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    myMatrix = []
    for row in range(0, (len(matrix))):
        tempRow = []
        for item in range(0, (len(matrix[row]))):
            tempRow.append(matrix[row][item] ** 2)
        myMatrix.append(tempRow)
    return(myMatrix)
