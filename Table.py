from Value import Value
from Cube import Cube
import math

class Table:

    def __init__(self, rows = 10, cols = 20):
        self.__rows = rows
        self.__cols = cols
        self.__cubes = [[None for x in range(cols)] for y in range(rows)] 

    @property
    def rows(self):
        return self.__rows
    
    @property
    def cols(self):
        return self.__cols
    
    def ValueHeigth(self, value: int, cols_by_digit = 1):
        vs = str(value)
        max_digit = max([int(d) for d in vs])
        return math.ceil(max_digit / cols_by_digit)
                
    def SetValue(self, value: int, cols_by_digit = 1):
        initial_row =  int(self.rows / 2 - self.ValueHeigth(value, cols_by_digit) / 2)
        
        vs = str(value)
        p = len(vs)                
        col = 0
                       
        for d in reversed(vs):                  
            if p == len(vs):
                col = (p * cols_by_digit - cols_by_digit + 1)
            else:
                if int(d) < cols_by_digit:
                    col -= int(d)
                else:
                    col -= cols_by_digit

            self.SetDigit(int(d), p, len(vs), cols_by_digit, row = initial_row, col = col)
            p -= 1
        
    def SetDigit(self, d: int, p: int):
        return
    
    def SetCube(self, cube: Cube, row = 1, col = 1):
        self.__cubes[row][col] = cube
        cube.row = row
        cube.col = col
    
    def SetCubes(self, cubes, row = 1, col = 1):
        for r in range(len(cubes)):
            for c in range(len(cubes[r])):
                self.SetCube(cubes[r][c], row + r, col + c)
    
    def Show(self):
        for r in range(self.__rows):
            for c in range(self.__cols):
                self.DrawCube(self.__cubes[r][c])
            print("")