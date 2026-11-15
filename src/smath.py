"""
======================= STRATA/SRC/SMATH.PY =======================
includes all the math stuff required for generating and analyzing 
the terrain.
"""
#############
### IMPORTS
#############
import os, sys

from utils import bubble

#############
### VARIABLES & TYPES
#############
type MATRIX     = list[tuple]
type COORDINATE = tuple[int, int]
type ANY        = int|float|str|list|tuple|dict|function

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
        """
        The matrix could be too large to effectively use regular indexing.
        Calculating the index is more effective than always using regular
        indexing whenever a coordinate is accessed.
        """
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

    def area(self, _matrix: MATRIX, coordinates: list) -> MATRIX:
        """
        Get a specific area within a given matrix. Returns a smaller
        matrix that contains only the variables and values in the given
        area. (0,0) will be equal to the the top right coordinate in
        the new 'area' matrix.
        """
        if len(coordinates) != 4: exit('STRATA/SRC/SMATH.PY -> matrix.area(coordinates=list) -> too few/many coordinates given. please provide 4 coordinates.')
        cor_a, cor_b, cor_c, cor_d = COORDINATE

        #: sort coordinates for x
        coordinates = bubble(coordinates)

        #: calculate slope of line between coordinates
        slope   = lambda cor_1, cor_2     : (cor_2[1] - cor_2[0]) / (cor_1[1] - cor_1[0])
        line    = lambda cor, _slope      : cor[0] - (_slope * cor[1])
        solve_y = lambda x, _line, _slope : (x - _line) / _slope

        lines = []

        #: get all connecting lines between the coordinates
        for _cor in coordinates:
            if _cor != coordinates[-1]:
                lines.append([line(_cor, slope(_cor, int(coordinates.index(_cor))+1))])
            else:
                lines.append([line(_cor, slope(_cor, int(coordinates[0])))])

        

matrix = matrix()

m = matrix.create((50, 50))
n = matrix.access(m, (33,45))
print('length: '+str(len(m)))
print('coordinate: '+str(n))
print(m)
