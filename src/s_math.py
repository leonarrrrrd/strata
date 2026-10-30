"""
======================= STRATA/SRC/SMATH.PY =======================
includes all the math stuff required for generating and analyzing 
the terrain.
"""
#############
### IMPORTS
#############
import os, sys
from dataclasses import dataclass

#############
### CLASSES
#############
@dataclass
class cell:
    coordinate_x:   int   = 0
    coordinate_y:   int   = 0
    biome:          int   = 0
    elevation:      float = 0.0
    erosion:        float = 0.0
    temperature:    float = 0.0
    moisture:       float = 0.0

    def create(self): ...

class coordinate_system:

    def __init__(self, width, height):
        self.width   = width
        self.height  = height

        self.grid    = [
            [cell() for _ in range(width)]
            for _ in range(height)
        ]

    def info(self):
        return self.width, self.height, self.grid

    def find(self, x: int, y: int, as_var: bool = True):
        return self.grid[y][x]

CS = coordinate_system(100, 100)

print(CS.info())
print(CS.find(34,40))