import numpy as np

# matrix = [[4,1],
#           [2,3],
#           [5,4],
#           [1,0]]

# matrix = [[90,60,90],
#           [90,90,30],
#           [60,60,60],
#           [60,60,90],
#           [30,30,30]]

# matrix = [[1,2,3], 
#          [3,4,5], 
#          [5,6,7]]

matrix = [[1,1,9],
          [2,4,6],
          [3,7,4],
          [4,11,4],
          [5,9,2]]

# get mean of each column
mean = np.mean(matrix, axis=0)

centered = matrix - mean

# get covariance matrix
covariance = np.cov(centered, rowvar=False)
print(covariance)

# get eigenvalues and eigenvectors and print them
eigenvalues, eigenvectors = np.linalg.eig(covariance)

# print(eigenvectors)



