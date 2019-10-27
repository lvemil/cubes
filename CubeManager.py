from Cube import Cube

class CubeManager:
    
    def __init__(self):
        return
    
    def PutTogether(self, digit = 0, pos = 1, cols = 1):
        color_by_position = {1: "V", 2: "A", 0: "R"}
        color = color_by_position[pos % 3]        
        cubes = [Cube(color) for x in range(digit)]
        return [cubes[i:i + cols] for i in range(0, digit, cols)]