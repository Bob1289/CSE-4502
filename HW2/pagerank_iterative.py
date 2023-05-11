# import numpy as np

# matrix = [[0,0,1,0],
#           [1/2,0,0,0],
#           [1/2,1,0,1],
#           [0,0,0,0]]

# r = [1,1,1,1]

# for i in range(0,33):
#     r = (.9 * np.dot(matrix,r)) + (.1 * np.array([1,1,1,1]))
#     print(r)

# import numpy as np

# matrix = [[1/2,0,1/2],
#           [0,0,1/2],
#           [1/2,1,0]]

# r = [1,1,1]

# for i in range(0,33):
#     r = np.dot(matrix,r)
#     print(r)

import numpy as np

matrix = [[0,   1/2,    1/2,    1],
          [1,   0,      0,      0],
          [0, 1/2,      0,      0],
          [0,   0,      1/2,    0]]

r = [1,1,1,1]

for i in range(0,33):
    r = np.dot(matrix,r)
    print(r)