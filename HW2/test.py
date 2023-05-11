import numpy as np

# Define the adjacency matrix M
M = np.array([[0, 0.5, 0.5, 0],
              [0.5, 0, 0.5, 0],
              [0.5, 0.5, 0, 0],
              [0, 0, 1, 0]])

# Define the initial hub and authority vectors
h = np.array([1, 1, 1, 1])
a = np.array([1, 1, 1, 1])

# Set the convergence threshold and maximum number of iterations
epsilon = 1e-6
max_iterations = 1000

# Run the HITS algorithm until convergence or maximum iterations reached
for i in range(max_iterations):
    # Update the authority vector based on incoming hub weights
    a_new = np.dot(M.T, h)
    
    # Update the hub vector based on outgoing authority weights
    h_new = np.dot(M, a)
    
    # Normalize the authority and hub vectors
    a_new /= np.linalg.norm(a_new)
    h_new /= np.linalg.norm(h_new)
    
    # Check for convergence
    if np.linalg.norm(a_new - a) < epsilon and np.linalg.norm(h_new - h) < epsilon:
        print("Converged after {} iterations".format(i+1))
        break
        
    # Update the authority and hub vectors
    a = a_new
    h = h_new

# Print the final authority and hub weights
print("Final authority weights: {}".format(a))
print("Final hub weights: {}".format(h))
