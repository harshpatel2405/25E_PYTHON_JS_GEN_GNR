import numpy as np

# * creating array
arr1 = np.array([10, 20, 30])
print(arr1)

# * type
print(type(arr1))

# * 2d Array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

# * dimension of array
print(arr1.ndim)
print(arr2.ndim)

# * shape of array / order (matrix)
print(arr1.shape)
print(arr2.shape)

# * size
print(arr1.size)
print(arr2.size)

# * datatype
print(arr1.dtype)
print(arr2.dtype)

# * creating arrays
arr3 = np.zeros(3, int)
print(arr3)
print(arr3.dtype)

arr4 = np.ones(4)
print(arr4)

arr5 = np.eye(3)
print(arr5)

# * indexing
arr6 = np.array(["Apple", "Banana", "Mango", "Blueberry", "Kiwi", "Litchie"])
print(arr6[0])
print(arr6[-1])
print(arr6[1:4])

# * mathematical operations
# * for list it is repetition
a = [10, 20, 30]
print(a*2)

arr7 = np.array([10, 20, 30])
print(arr7 * 2)
print(arr7 + 2)
print(arr7 - 2)
print(arr7 // 2)

#  ^ 2d Array
print(arr2 * 2)
print(arr2 + 2)
print(arr2 - 2)
print(arr2 / 2)


# * aggregate function 
arr8 = np.array([10,20,30])
print(np.mean(arr8))
print(np.min(arr8))
print(np.max(arr8))
print(np.sum(arr8))
print(np.std(arr8))


# * flatten 
arr9 = np.array([[1,2,3],[4,5,6]])
print(arr9)
print(arr9.flatten())

# * boolean filtering 
arr10 = np.array([10,11 , 34 , 56 , 45,  20 , 30])
print(arr10[arr10 % 2 == 0])