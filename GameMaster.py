from TerminalTable import TerminalTable
from random import choice

class GameMaster:
    def __init__(self, table_rows: int, table_cols: int):
        self.Table = TerminalTable(table_rows, table_cols)

    def SetupChallenge1(self):
        color = choice(["R","A","V"])
        count = choice(range(1,10))    
        self.Table.RandomSet(color, count)
        return count