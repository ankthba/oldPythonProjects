#!/usr/bin/python3

def GetMaxSumRectangle(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    # Inclusion Exclusion Principle
    for r in range(rows):
        for c in range(cols):

            # Add element from the previous column
            if(r > 0): 
               matrix[r][c] += matrix[r-1][c]

            # Add element from the previous row
            if(c > 0): 
               matrix[r][c] += matrix[r][c-1]

            # Subtract diagonal element that got added twice from previous row and column additions
            if(r > 0 and c > 0): 
               matrix[r][c] -= matrix[r-1][c-1]

    maxsum = -100*100*100

    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):

                    sum_subrectangle = matrix[k][l]

                    if(i > 0): 
                       sum_subrectangle -= matrix[i-1][l]
                    if(j > 0): 
                       sum_subrectangle -= matrix[k][j-1]
                    if(i > 0 and j > 0): 
                       sum_subrectangle += matrix[i-1][j-1]

                    if(sum_subrectangle > maxsum):
                       # Co-ordinates of maximum sum sub rectangle
                       from_row = i 
                       from_column = j 
                       to_row = k 
                       to_column = l 
                       maxsum = sum_subrectangle

    print("Maximum sum in sub-rectangle: "+str(maxsum))
    print("Maximum sum rectangle co-ordinates: (" + str(from_row) + "," + str(from_column) + ")" + "-" + "(" + str(to_row) + "," + str(to_column) + ")")

matrix1 = [[  0, -2, -7],
           [  9,  2, -6],
           [ -4,  1, -4],
           [ -1, 8, 0],
           [ -2,  4,  -3],
           
          ]
GetMaxSumRectangle(matrix1)