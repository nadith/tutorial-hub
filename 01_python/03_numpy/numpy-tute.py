# Numpy for matlab users
# Ref: https://numpy.org/doc/stable/user/numpy-for-matlab-users.html

import numpy as np

def dtypes():
    # i - integer
    # b - boolean
    # u - unsigned integer
    # f - float
    # c - complex float
    # m - timedelta
    # M - datetime
    # O - object
    # S - string
    # U - unicode string
    # V - fixed chunk of memory for other type ( void )

    arr = np.array([1, 2, 3, 4])
    print(arr.dtype)

    # Create an array with data type string:
    arr = np.array(['apple', 'banana', 'cherry'])
    print(arr.dtype)

    arr = np.array([1, 2, 3, 4], dtype='S')
    print(arr) # [b'1' b'2' b'3' b'4']
    print(arr.dtype) # |S1

    # Create an array with data type 4 bytes integer:
    # For i, u, f, S and U we can define size as well.
    arr = np.array([1, 2, 3, 4], dtype='i4') # or arr = np.array([1, 2, 3, 4], dtype='int32')
    print(arr) # [1 2 3 4]
    print(arr.dtype) # int32


    ##### Casting #####
    # Change data type from float to integer by using 'i' as parameter value:
    arr = np.array([1.1, 2.1, 3.1])
    newarr = arr.astype('i') # or 'int32' or int

    # Change data type from integer to boolean:
    arr = np.array([1, 0, 3])
    newarr = arr.astype(bool)



def join():
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    arr = np.concatenate((arr1, arr2))
    print(arr)

    # Join two 2-D arrays along rows (axis=1):
    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6], [7, 8]])
    arr = np.concatenate((arr1, arr2), axis=1)
    print(arr)

    # Joining Arrays Using Stack Functions
    # Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
    # We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.
    # We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicitly passed it is taken as 0.
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    arr = np.stack((arr1, arr2), axis=1)
    print(arr)

    # NumPy provides a helper function: hstack() to stack along rows.
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    arr = np.hstack((arr1, arr2))
    print(arr)

    # NumPy provides a helper function: vstack()  to stack along columns.
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    arr = np.vstack((arr1, arr2))
    print(arr)

    # NumPy provides a helper function: dstack() to stack along height (depth), which is the same as depth.
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    arr = np.dstack((arr1, arr2))
    print(arr)

def indexing_with_int_arr():

    # 1D Array ---------------------------
    a = np.arange(12) ** 2                  # the first 12 square numbers
    i = np.array([1, 1, 3, 8, 5])           # an array of indices
    a[i] = np.array([ 1,  1,  9, 64, 25])   # the elements of a at the positions i

    j = np.array([[3, 4], [9, 7]])          # a bidimensional array of indices
    print("a[j] = ")
    print(a[j])

    # array([[ 9, 16],
    #         [81, 49]])                    # the same shape as j


    # 2D Array -----------------------------
    print("\n2D Array -----------------------------")
    palette = np.array([[0, 0, 0],         # black
                        [255, 0, 0],       # red
                        [0, 255, 0],       # green
                        [0, 0, 255],       # blue
                        [255, 255, 255]])  # white

    image = np.array([[0, 1, 2, 0],        # each value corresponds to a color in the palette
                       [0, 3, 4, 0]])

    print("palette[image] =")
    print(palette[image])    # the (2, 4, 3) color image
    # array([[[  0,   0,   0],
    #         [255,   0,   0],
    #         [  0, 255,   0],
    #         [  0,   0,   0]],
    #
    #        [[  0,   0,   0],
    #         [  0,   0, 255],
    #         [255, 255, 255],
    #         [  0,   0,   0]]])


    # 2D Array --- Individual Dim Indexing ----
    print("\n2D Array ---Individual Dim Indexing ---")
    a = np.arange(12).reshape(3,4)
    print("a =", a.shape)
    print(a, end="\n\n")
    # array([[ 0,  1,  2,  3],
    #        [ 4,  5,  6,  7],
    #        [ 8,  9, 10, 11]])

    i = np.array([[0, 1],                       # indices for the first dim of a
                    [1, 2]])

    j = np.array([[2, 1],                       # indices for the second dim
                    [3, 3]])

    print("i =", i.shape)
    print(i, end="\n\n")

    print("j =", j.shape)
    print(j, end="\n\n")

    print("a[i, j] =")                          # i and j must have equal shape
    print(a[i, j], end="\n\n")
    # array([[ 2,  5],
    #        [ 7, 11]])

    print("a[i, 2] =")
    print(a[i, 2], end="\n\n")
    # array([[ 2,  6],
    #        [ 6, 10]])

    print("a[i, :] = a[i] =", a[i, :].shape)   # (2, 2 <from indexing array>, 4 <from 'a' dim 1>)
    print(a[i, :], end="\n\n")                 # i.e., a[ : , j]

    print("a[:, j] =", a[:, j].shape)           # (3 <from 'a' dim 0>, 2, 2 <from indexing array>)
    print(a[:, j])                              # i.e., a[ : , j]
    # array([[[ 2,  1],
    #         [ 3,  3]],
    #
    #        [[ 6,  5],
    #         [ 7,  7]],
    #
    #        [[10,  9],
    #         [11, 11]]])


    # 2D Array --- Indexing with tuple ----
    print("\n2D Array --- Indexing with tuple ---")
    l = (i, j)

    # equivalent to a[i, j]
    print(a[l])

    # array([[ 2,  5],
    #        [ 7, 11]])

    # However, we can not do this by putting i and j into an array, because this array will be interpreted
    # as indexing the first dimension of a.

    s = np.array([i, j])

    # not what we want
    # a[s] # ??

    print(a[tuple(s)]) # ok


def indexing_with_bool_arr():
    pass

def vector_stack():
    # Vector Stacking
    # How do we construct a 2D array from a list of equally-sized row vectors?
    # In MATLAB this is quite easy: if x and y are two vectors of the same length you only need do m=[x;y].
    # In NumPy this works via the functions column_stack, dstack, hstack and vstack, depending on the dimension
    # in which the stacking is to be done. For example:
    pass

# dimensions_in_arrays
# slice()
# slice_2d()
# dtypes()
# copy_vs_view()
# join()
# indexing()


a = np.array([2, 3, 4])
print(id(a))
a + 1
print(id(a))
print(a)