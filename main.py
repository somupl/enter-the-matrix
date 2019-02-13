# read in the matrix.txt
# filter the 4x2 and 2x4 matrices into
# different lists

# add any 2 compatible matrices
# multiply any 2 compatible matrices
# scale any matrix
# create a list of 5 3x3 matrices of random values
# and add them together

# multiply a matrix times a vector


from matrix import Matrix
from vector import Vector
from functools import reduce

vectors = []
matrix = []
with open('matrix.txt') as f:
    for line in f:
        if len(line) > 1:
            v = Vector(*tuple(map(int, line.strip().split(' '))))
            vectors.append(v)
        else:
            m = Matrix(*vectors)
            matrix.append(m)
            vectors = []

# different list
mat_list1 = []
mat_list2 = []
for mat in matrix:
    if mat.row == 4 and mat.col == 2:
        mat_list1.append(mat)
    else:
        mat_list2.append(mat)

# add ans
add_m = mat_list1[0] + mat_list1[1]
# print(mat_list1[0], mat_list1[1], add_m)

# scale ans
scale_m = mat_list1[0].scale(3)
# print(mat_list1[0], scale_m)

# multiply ans
# print(add_m.transpose()) # needed transpose due to list
print(mat_list2[0].mul(mat_list1[0]))

# create a list of 5 3x3 matrices of random values and add them together
m1 = Matrix.random(3, 4)
# print(m1)

mat_5 = [Matrix.random(3, 3) for _ in range(5)]
empty_mat = Matrix(*[Vector(0, 0, 0), Vector(0, 0, 0), Vector(0, 0, 0)])
final_mat = reduce(lambda acc, mat: acc + mat, mat_5, empty_mat)
print(final_mat)
