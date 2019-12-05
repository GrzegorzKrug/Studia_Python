import numpy as np
from copy import copy, deepcopy
from sympy import Matrix, zeros, ones, eye, diag
from itertools import permutations
import warnings
import time


class SymArray:
    # Class is defining symbolic Array using Matrix object,
    # Makes easy use of 2D elements
    def __init__(self, array, history=None):
        if type(array) == int:  # Number input
            array = [array]

        if array == [] or array is None:
            self.size = (0, 0)
            warnings.warn('Symbolic Array is empty!', RuntimeWarning)

        elif type(array[0]) != list:
            self.single = True
            self.size = (1, len(array))
            array = [array]  # Matrix always uses 2d !
        else:
            self.single = False
            self.size = (len(array), len(array[0]))

        if len(array) == 1:
            self.single = True

        for row in array:
            if type(row[0]) == list:
                warnings.warn(f'Array dimension is too big! Must be: n <= 2',
                              RuntimeWarning)

        self.array = Matrix(array)

        if history:
            self.history = history
        else:
            self.history = []
        self.history.append({'created': array})

    def __add__(self, other):
        return SymArray([[
            self.array[r * self.size[1] + c] +
            other.array[r * self.size[1] + c]
            for c in range(self.size[1])
        ]
            for r in range(self.size[0])
        ])

    def __eq__(self, other):
        return self.array == other.array

    def __getitem__(self, i):
        # Condition to extract row!
        if type(i) is slice:
            rstart = i.start if i.start else 0
            rstop = i.stop if i.stop else self.size[0]
            rstep = i.step if i.step else 1

            cstart = 0
            cstop = self.size[1]
            cstep = 1

        # Condition to Slice with number -> one Row
        elif type(i) is int:
            rstart = i
            rstop = i + 1
            rstep = 1

            cstart = 0
            cstop = self.size[1]
            cstep = 1

        # Condition Double slice
        elif type(i[0]) is slice and type(i[1]) is slice:
            rslice = i[0]
            cslice = i[1]

            rstart = rslice.start if rslice.start else 0
            rstop = rslice.stop if rslice.stop else self.size[0]
            rstep = rslice.step if rslice.step else 1
            cstart = cslice.start if cslice.start else 0
            cstop = cslice.stop if cslice.stop else self.size[1]
            cstep = cslice.step if cslice.step else 1
        else:
            raise ValueError(f"Incorrect Slice params: {i}")

        array = self.array
        if self.single:
            # array = array]
            out = [
                array[r * self.size[1] + c]
                for c in range(cstart, cstop, cstep)
                for r in range(rstart, rstop, rstep)
            ]
        else:
            out = [[
                array[r * self.size[1] + c]
                for c in range(cstart, cstop, cstep)
            ]
                for r in range(rstart, rstop, rstep)
            ]

        return SymArray(out)

    def __repr__(self):
        txt = '['
        for row in range(self.size[0]):
            if row == 0:
                txt += f"{'[':>1}"
            else:
                txt += f'\n{"[":>3}'

            for col in range(self.size[1]):
                txt += f' {self.array[self.size[1]*row +col]},'

            if row >= self.size[0] - 1:
                txt += ']'
            else:
                txt += f'],'
        txt += f']'
        return txt

    def __sub__(self, other):
        return SymArray([[
            self.array[r * self.size[1] + c] -
            other.array[r * self.size[1] + c]
            for c in range(self.size[1])
        ]
            for r in range(self.size[0])
        ])

    def __len__(self):
        if self.single:  # Lenght of vector, only if initiated as vector!
            return self.size[1]
        return self.size[0]

    def __mul__(self, other):
        result = self.array * other.array
        result = [result[other.size[1]*row: other.size[1]*row + other.size[1]]
                  for row in range(self.size[0])
                  ]
        return SymArray(result)

    def switch_rows(self, index_list: 'List[int]'):
        if len(index_list) != self.size[0]:
            raise IndexError('Switch rows requires equal amount of indexes!')

        col_len = self.size[1]
        new_Array = [self.array[col_len*ind: col_len*ind + col_len]
                     for ind in index_list
                     ]
        new_Array = SymArray(new_Array, history=[{'Row Switch': index_list}])
        new_Array.history = self.history + new_Array.history
        return new_Array

    def switch_cols(self, index_list: 'List[int]'):
        if len(index_list) != self.size[1]:
            raise IndexError('Switch rows requires equal amount of indexes!')

        col_len = self.size[1]
        new_Array = [[self.array[col_len * row + col_ind]
                      for col_ind in index_list]
                     for row in range(self.size[0])
                     ]
        new_Array = SymArray(new_Array, history=[{'Col Switch': index_list}])
        new_Array.history = self.history + new_Array.history
        return new_Array

    def transp(self):
        c = self.size[0]
        r = self.size[1]
        array_t = self.array.T
        return SymArray([array_t[row*c: row*c + c] for row in range(r)])

    def match_any_patern(self):
        # A | B
        # --|--
        # C | D
        if self.size[0] % 2 == 1 or self.size[1] % 2 == 1:
            raise ValueError("Matrix has to be even size!")

        half_rows = int(self.size[0]/2)
        half_cols = int(self.size[1]/2)

        square_a = self[0:half_rows, 0:half_cols]
        square_b = self[0:half_rows, half_cols:self.size[1]]
        square_c = self[half_rows:self.size[0], 0:half_cols]
        square_d = self[half_rows:self.size[0], half_cols:self.size[1]]

        return any([
            square_a == square_b,
            square_a == square_c,
            square_a == square_d,
            square_b == square_c,
            square_b == square_d,
            square_c == square_d
        ])


class Reduktor():
    def __init__(self, matrix_input):
        self.array_ojb = SymArray(matrix_input)

    def run(self):
        time0 = time.time()
        for i, row_perm in enumerate(permutations(range(8))):
            new_Array = self.array_ojb.switch_rows(row_perm)
            if i % 100 == 0:
                print(i)
            for j, col_perm in enumerate(permutations(range(8))):
                test_array = new_Array.switch_cols(col_perm)

                if test_array.match_any_patern():
                    print(f"\nFound one\n{test_array}")
                    print(test_array.history)
                    mid_time = time.time()
                    print(f"Time elapsed to this point: {(mid_time - time0)/60} min")
        end_time = time.time()
        print(f"Time elapsed: {(end_time - time0)/60} min")


if __name__ == "__main__":
    a = [['a', '-b', '-c', '-d', '-e', '-f', '-g', '-h'],
         ['b', 'a', 'd', '-c', 'f', '-e', '-h', 'g'],
         ['c', '-d', 'a', 'b', 'g', 'h', '-e', '-f'],
         ['d', 'c', '-b', 'a', 'h', '-g', 'f', '-e'],
         ['e', '-f', '-g', '-h', 'a', 'b', 'c', 'd'],
         ['f', 'e', '-h', 'g', '-b', 'a', '-d', 'c'],
         ['g', 'h', 'e', '-f', '-c', 'd', 'a', '-b'],
         ['h', '-g', 'f', 'e', '-d', '-c', 'b', 'a']]

    red = Reduktor(a)
    red.run()
