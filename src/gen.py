"""
======================= STRATA/SRC/GEN.PY =======================
includes the main terrain generator
"""
#############
### IMPORTS
#############
import sys, os

#############
### TYPES
#############
type MATRIX = list[tuple]

#############
### VARIABLES
#############
TERRAIN_SIZE   = tuple        # -> define terrain size on a blank 2D canvas (x,y)
TERRAIN_MATRIX = MATRIX       # -> create blank matrix with coordinate tuples
HEIGHTMAP      = MATRIX       # -> create custom smooth height map

#############
### FUNCTIONS
#############

#############
### CLASSES
#############
class strata_data:
    def __init__(self): ...

    
