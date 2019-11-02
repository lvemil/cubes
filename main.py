from Value import Value
from Table import Table
from TerminalTable import TerminalTable
from GameMaster import GameMaster

if __name__ == '__main__':
    game = GameMaster(11,30)
    count = game.SetupChallenge1()
    game.Table.Show()
    print(count)
    print(game.Table.CountCubes())    
    #t.SetValue(1519, cols_by_digit = 3)
    
    