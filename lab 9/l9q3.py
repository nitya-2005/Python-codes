import numpy as np

def create_array(dim1, dim2, dim3, value):
    """Creates and returns a 3D array with the given dimensions, initialized to a specified value."""
    return np.full((dim1, dim2, dim3), value)


array = create_array(3, 4, 5, 7)
print(array)

