#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
<<<<<<< HEAD
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end="")
            if j != (len(matrix[i]) - 1):
                print(" ", end="")

                print("")
=======
    """Print a matrix of integers."""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
                print("{:d}".format(matrix[i][j]), end="")
                if j != (len(matrix[i]) - 1):
                    print(" ", end="")

        print("")
>>>>>>> c7b8dd0faa6415f52540cd4bcadf0880b26737da
