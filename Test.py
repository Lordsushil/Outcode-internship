# import time

# # Create a large Python list
# python_list = list(range(1000000))

# # Start time
# start_time = time.time()

# # Perform multiple calculations using a Python loop
# result = 0
# for x in python_list:
#     result += (x**2 + x**3 + x**4)

# # End time and print the time taken
# end_time = time.time()
# print(f"Python Loop Time Taken: {end_time - start_time:.6f} seconds")


import numpy as np
import time

# Create a large NumPy array with float data type
numpy_arr = np.arange(1000000, dtype=np.float64)

# Start time
start_time = time.time()

# Perform the same multiple calculations with vectorized operations
np_result = np.sum(numpy_arr**2 + numpy_arr**3 + numpy_arr**4)

# End time and print the time taken
end_time = time.time()
print(f"NumPy Time Taken: {end_time - start_time:.6f} seconds")