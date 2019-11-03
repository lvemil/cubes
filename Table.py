from Value import Value
from Cube import Cube
import math
import random

'''A table to put'''
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
    
    def ValueWidth(self, value: int, cols_by_digit = 1):
        return sum([(x if x < cols_by_digit else cols_by_digit) for x in [int(x) for x in str(value)]])
    
    def SetValue(self, value: int, cols_by_digit = 1):
        initial_row = int(self.rows / 2 - self.ValueHeigth(value, cols_by_digit) / 2)
        initial_col = int(self.cols / 2 + self.ValueWidth(value, cols_by_digit) / 2)
        vs = str(value)
        p = len(vs)                
        col = 0
                       
        for d in [int(x) for x in reversed(vs)]:                  
            if p == len(vs):
                col = initial_col - (d if d < cols_by_digit else cols_by_digit)
            else:
                if d < cols_by_digit:
                    col -= d
                else:
                    col -= cols_by_digit

            self.SetDigit(d, p, len(vs), cols_by_digit, row = initial_row, col = col)
            p -= 1
        
    def SetDigit(self, d: int, p: int, l: int, cols: int, row: int, col: int):
        pass
    
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

    def DrawCube(self, cubes):
        pass

    def RandomSet(self, color: str, count: int):
        for i in range(count):
            not_free = True
            while not_free:
                r = random.choice(range(self.rows))
                c = random.choice(range(self.cols))
                not_free = self.IsFree(r, c) == False
            cube = Cube(color, r, c)
            self.SetCube(cube, r, c)
    
    def IsFree(self, row: int, col: int):
        return self.__cubes[row][col] == None

    def CountCubes(self, color: str = "ALL"):
        if color == "ALL":
            count = sum([sum(1 for x in r if x != None) for r in self.__cubes])
        else:
            count = sum([sum(1 for x in r if (x != None and x.color == color)) for r in self.__cubes])
        return count

    def CountCubesByColors(self):
        colors = ["R","A","V"]
        counts = {c: self.CountCubes(c) for c in colors}
        return counts