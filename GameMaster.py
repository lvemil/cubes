from TerminalTable import TerminalTable
from random import choice, sample

class GameMaster:
    def __init__(self, table_rows: int, table_cols: int):
        self.Table = TerminalTable(table_rows, table_cols)

    def SetupChallenge1(self):
        color = choice(["R","A","V"])
        count = choice(range(1,10))    
        self.Table.RandomSet(color, count)
        return count

    def SetupChallenge2(self):
        how_many_colors = choice(range(3,4))
        colors = sample(["R","A","V"], how_many_colors)
        count_by_color = {color: choice(range(1,10)) for color in colors }
        for color, count in count_by_color.items():
            self.Table.RandomSet(color, count)
        return count_by_color