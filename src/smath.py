"""
======================= STRATA/SRC/SMATH.PY =======================
includes all the math stuff required for generating and analyzing 
the terrain.
"""
#############
### IMPORTS
#############
import os, sys

#############
### VARIABLES & TYPES
#############
type MATRIX     = list[tuple]
type COORDINATE = tuple[int, int]

#############
### CLASSES
#############
class matrix:
    """
    does NOT really create a matrix, it's more of a coordinate system.
    might have to rename it.
    """
    __matrix = MATRIX
    #: ignore __init__ as a professional programmer like myself should
    def __init__(self): ...

    #: create a new matrix with a size of (x,y)
    def create(self, size: tuple) -> MATRIX:
        self.__matrix = size

        #: check if size type is correct
        if type(size[0]) != int or type(size[1]) != int: exit('STRATA/SRC/SMATH.PY -> matrix.create(size=tuple) -> size must include two integers!')

        #: generate matrix
        _matrix = [(x,y) for x in range(size[0]+1)
                          for y in range(size[1]+1)]

        return _matrix

    #: find matrix coordinate and return stored data
    def access(self, _matrix: MATRIX, coordinate: tuple, as_var: bool = True) -> COORDINATE:
        x = int(coordinate[0])
        y = int(coordinate[1])

        ind = int

        #: check if coordinates are within matrix length
        for i in coordinate:
            if i != int: ...
            if i > (int(len(_matrix))**0.5)-1: exit('STRATA/SRC/SMATH.PY -> matrix.find(coordinate=tuple) -> coordinates cannot exceed matrix size!')

        #: calculate index of coordinate in matrix list -> x * columns + y
        ind = x * (self.__matrix[1]+1) + y
        print('index: '+str(ind))

        return _matrix[ind]
        
matrix = matrix()

m = matrix.create((100, 100))
n = matrix.access(m, (33,45))
print('length: '+str(len(m)))
print('coordinate: '+str(n))
print(m)