from Table import Table
from Cube import Cube
from CubeManager import CubeManager

class TerminalTable(Table):
        
    def __init__(self, rows = 10, cols = 20):
        super().__init__(rows, cols)
        
    def SetDigit(self, digit: int, pos: int, length: int, cols_by_digit = 1, row = 1, col = 1):
        cubes = CubeManager().PutTogether(digit, length - pos + 1, cols_by_digit)
        self.SetCubes(cubes, row, col)
        
    def Build(self, d: int):
        return ("1" * d).ljust(9,".")
    
    def DrawCube(self, c: Cube):
        if c != None:
            print(c.color, end = '')
        else:
            print("-", end = '')
                 