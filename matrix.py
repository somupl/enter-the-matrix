# create a matrix
# any dimension
# multiply 2 matrices
# add 2 matrices
# scale matrix
# create a random mxn matrix
# with values between 0 and 1

import random as r
from vector import Vector


class Matrix:

    def __init__(self, *vect):
        self.mat = vect
        self.row = len(vect)
        self.col = self.mat[0].len

    def __str__(self):
        msg1 = "This is a {} X {} matrix".format(self.row, self.col)
        msg2 = [x.nums for x in self.mat]
        return "{} \n {} \n".format(msg1, msg2)

    @staticmethod
    def random(row, col):
        v1 = []  # list of numbers
        vec = []
        for _ in range(row):
            for _ in range(col):
                v1.append(r.random())
            vec.append(Vector(*v1))
            v1 = []
        return Matrix(*vec)

    def __add__(self, other):
        return Matrix(*[c1 + c2 for c1, c2 in zip(self.mat, other.mat)])

    def scale(self, scalar):
        return Matrix(*[n.scale(scalar) for n in self.mat])

    def transpose(self):
        v = []
        m = []
        for col in range(self.col):
            for row in self.mat:
                v.append(row.nums[col])
            m.append(Vector(*v))
            v = []
        return Matrix(*m)

    def mul(self, other):
        t_other = other.transpose()
        print(self)
        print(t_other)
        v = []
        m = []
        for row in self.mat:
            # print(row)
            for col in t_other.mat:
                # print(col)
                v.append(row.dot(col))
            vec = Vector(*v)
            m.append(vec)
            v = []
        return Matrix(*m)
