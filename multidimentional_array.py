import numpy as np

array = np.array("Arpit")
print(array.ndim)

array2 = np.array(["A" ,"B", "C"])
print(array2.ndim)

array3 = np.array([[1, 2, 3],["A","B","C"]])
print(array3.ndim)


array4 = np.array([[1,3,4,],
                   [5,7,4],
                   [645,45,245]])
print(array4.ndim)

array5 = (np.array([[[1,3,4,],[5,7,4],[645,45,245]],
                    [[245,65,62,],[45,56,13],[62,4762,632]],
                    [[1435,62,62],[7673,776,6736],[135,46622,2468356]]]))
print(array5.shape)
# It means 3 layers 3 rows 3 columns

array5 = (np.array([[[1,3,4,],[5,7,4],[645,45,245]],
                    [[245,65,62,],[45,56,13],[62,4762,632]]]))
print(array5.shape)

# It means 2 layers 3 rows 3 columns

# Chain Indexing

array5 = (np.array([[[1,3,4,],[5,7,4],[645,45,245]],
                    [[245,65,62,],[45,56,13],[62,4762,632]],
                    [[1435,62,62],[7673,776,6736],[135,46622,2468356]]]))
print(array5[0][0][0])          # 0 layers first row[0] first element[0]
print(array5[2][2][2])
print(array5[1][1][1])
print(array5[1][0][1])
print(array5[1][2][1])