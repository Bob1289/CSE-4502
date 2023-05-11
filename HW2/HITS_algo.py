import numpy as np

matrix = [[0,1,1,0],
          [0,0,1,0],
          [1,0,0,0],
          [0,0,1,0]]

# matrix = [[2,1,0,1],
#           [1,1,0,1],
#           [0,0,1,0],
#           [1,1,0,1]]

# matrix = [[3,1,2],
#           [1,1,0],
#           [2,0,2]]

# matrix = [[2,2,1],
#           [2,2,1],
#           [1,1,2]]

transpose = np.transpose(matrix)

matrix = np.dot(transpose,matrix)

h = [1,1,1,1]


for i in range(0,30):
    h = np.dot(matrix,h)
    normalize = np.sum(h)
    h = (h/normalize) * 4
    print(h)