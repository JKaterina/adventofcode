with open("inputs/input_ch8.txt") as f:
    data = [s.strip('\n') for s in list(f)]
    data = [[*a_str] for a_str in data]
    
data_int = []
for line in data:
    line = [int(a_str) for a_str in line]
    data_int.append(line)

print(data_int[:5])

import numpy as np
matrix = np.matrix(data_int)

# in matrix: check each node if x, y are the largest in row / column
# exclude row 0, column 0 --> also last row and column

visible_nodes = 0

for row in range(1, matrix.shape[0]):
    for column in range(1, matrix.shape[1]):

        node = matrix[row, column]
        current_row = matrix[row: ]
        current_column = matrix[: column]

        if (node == np.max(current_row)) | (node == np.max(current_column)):
            visible_nodes += 1

print(visible_nodes)

# add the exterior visible nodes
total = visible_nodes + matrix.shape[0]*2 + matrix.shape[1]*2 - 2

print(total)