#python: Battleship

#This program is not fool-proof
#When moving your ships before the game, it does NOT
#check that there aren't other ships in the way of the
#new position

import os #used to clear the terminal during gameplay

###Your Playing Field###
class warzone(object):
    """
    ***LEGEND***
    X = hit ship
    + = unoccupied
    A = Aircraft Carrier
    B = Battleship
    S = Submarine
    D = Destroyer
    P = Patrol Boat
    """
    #constructor
    def __init__(self, pn):
                  #COL  0   1   2   3   4   5   6   7   8   9  ROW
        self.field = [['A','A','A','A','A','+','+','+','+','+'],#0
                      ['B','B','B','B','+','+','+','+','+','+'],#1
                      ['S','S','S','+','+','+','+','+','+','+'],#2
                      ['D','D','D','+','+','+','+','+','+','+'],#3
                      ['P','P','+','+','+','+','+','+','+','+'],#4
                      ['+','+','+','+','+','+','+','+','+','+'],#5
                      ['+','+','+','+','+','+','+','+','+','+'],#6
                      ['+','+','+','+','+','+','+','+','+','+'],#7
                      ['+','+','+','+','+','+','+','+','+','+'],#8
                      ['+','+','+','+','+','+','+','+','+','+']]#9

        self.ships = {'A':[0, 5, 'A'],
                      'B':[0, 4, 'B'],
                      'S':[0, 3, 'S'],
                      'D':[0, 3, 'D'],
                      'P':[0, 2, 'P']}
        self.name = pn

    #return the value of the given spot
    def get_spot(self, pos):
        row = pos[0]
        col = pos[1]
        
        return self.field[row][col]

    #set the value of the given spot
    def set_spot(self, pos, value):
        row = pos[0]
        col = pos[1]

        self.field[row][col] = value

    #remove a ship that has already been placed
    def clear_from_field(self, ship):
        for rindex, r in enumerate(self.field):
            for cindex, c in enumerate(r):
                if c == ship:
                    self.field[rindex][cindex] = '+'

    #initial game setup
    def prepare_for_battle(self):
        while 1:
            self.print_warzone()
            
            print 'Aircraft Carrier(5) = A'
            print 'Battleship(4) = B'
            print 'Submarine(3) = S'
            print 'Destroyer(3) = D'
            print 'Patrol Boat(2) = P'
            p_input = raw_input('Select Ship: (\'done\' to finish)')
            if p_input == 'done':
                break

            if p_input == 'A' or p_input == 'B' or p_input == 'S' or p_input == 'D' or p_input == 'P':
                print 'Select Location'
            else:
                continue

            self.clear_from_field(p_input)
            ship = self.ships[p_input]

            r1 = -1
            while r1 < 0 or r1 > 9:
                try:r1 = int(raw_input('Enter start row (0-9): '))
                except:print 'row index must be from 0 to 9'
                    
            c1 = -1
            while c1 < 0 or c1 > 9:
                try:c1 = int(raw_input('Enter start col (0-9): '))
                except:print 'row index must be from 0 to 9'

            r2 = -1
            while r2 < 0 or r2 > 9:
                try:r2 = int(raw_input('Enter end row (0-9): '))
                except:print 'row index must be from 0 to 9'

            c2 = -1
            while c2 < 0 or c2 > 9:
                try:c2 = int(raw_input('Enter end col (0-9): '))
                except:print 'row index must be from 0 to 9'

            pos1 = (r1, c1)
            pos2 = (r2, c2)

            ship_len = ship[1]

            if r1 == r2 and (c2 - c1 + 1) == ship_len:
                for i in range(c1, c2+1):
                    self.field[r1][i] = ship[2]
            elif c1 == c2 and (r2 - r1 + 1) == ship_len:
                for j in range(r1, r2+1):
                    self.field[j][c1] = ship[2]
            else:
                print 'invalid'

    #check for defeat
    def defeat(self):
        for ship in self.ships:
            if not self.ships[ship][0] == self.ships[ship][1]:
                return False
        return True

    #print the battlefield
    def print_warzone(self):
        os.system('cls' if os.name=='nt' else 'clear')

        print '  ' + self.name + ' Warzone'
        print '  0 1 2 3 4 5 6 7 8 9'
        for index, r in enumerate(self.field):
            print index,
            for c in r:
                print c,
            print ''

####Enemy Radar###
class enemy_radar(object):
    #constructor
    def __init__(self, pn):
        
        """
        ***LEGEND***
        X = hit
        0 = miss
        - = unknown
        """
              #COL 0   1   2   3   4   5   6   7   8   9  ROW
        field = [['-','-','-','-','-','-','-','-','-','-'],#0
                 ['-','-','-','-','-','-','-','-','-','-'],#1
                 ['-','-','-','-','-','-','-','-','-','-'],#2
                 ['-','-','-','-','-','-','-','-','-','-'],#3
                 ['-','-','-','-','-','-','-','-','-','-'],#4
                 ['-','-','-','-','-','-','-','-','-','-'],#5
                 ['-','-','-','-','-','-','-','-','-','-'],#6
                 ['-','-','-','-','-','-','-','-','-','-'],#7
                 ['-','-','-','-','-','-','-','-','-','-'],#8
                 ['-','-','-','-','-','-','-','-','-','-']]#9

        self.clear_field()

        self.name = pn

    #update a position on the radar
    def update(self, pos, value):
        row = pos[0]
        col = pos[1]

        self.field[row][col] = value
    
    #set/reset the radar
    def clear_field(self):
                   #COL 0   1   2   3   4   5   6   7   8   9  ROW
        self.field = [['-','-','-','-','-','-','-','-','-','-'],#0
                      ['-','-','-','-','-','-','-','-','-','-'],#1
                      ['-','-','-','-','-','-','-','-','-','-'],#2
                      ['-','-','-','-','-','-','-','-','-','-'],#3
                      ['-','-','-','-','-','-','-','-','-','-'],#4
                      ['-','-','-','-','-','-','-','-','-','-'],#5
                      ['-','-','-','-','-','-','-','-','-','-'],#6
                      ['-','-','-','-','-','-','-','-','-','-'],#7
                      ['-','-','-','-','-','-','-','-','-','-'],#8
                      ['-','-','-','-','-','-','-','-','-','-']]#9

    #print the radar
    def print_radar(self):
        os.system('cls' if os.name=='nt' else 'clear')
        
        print '      ' + self.name
        print '      Enemy Radar'
        print '  0 1 2 3 4 5 6 7 8 9'
        for index, r in enumerate(self.field):
            print index,
            for c in r:
                print c,
            print ''



#THE GAME
if __name__ == '__main__':
    #create player 1 warzone and radar
    p1_warzone = warzone('Player 1')
    p1_radar = enemy_radar('Player 1')

    #create player 2 warzone and radar
    p2_warzone = warzone('Player 2')
    p2_radar = enemy_radar('Player 2')
    
    #Inital ship placement
    p1_warzone.prepare_for_battle()
    p2_warzone.prepare_for_battle()

    turn = 1 #players turn
    
    #Main Game Loop
    while 1:
        #Player 1
        if turn == 1:
            os.system('cls' if os.name=='nt' else 'clear')
            p1_radar.print_radar()

            row = -1
            while row < 0 or row > 9:
                row = raw_input('Enter Row [0-9](\'w\' to view your warzone): ')
                if row == 'w':
                    os.system('cls' if os.name=='nt' else 'clear')
                    p1_warzone.print_warzone()
                    pause = raw_input('Press Enter')
                    os.system('cls' if os.name=='nt' else 'clear')
                    p1_radar.print_radar()
                else:
                    try:
                        row = int(row)
                    except:
                        print 'Enter a valid Number!'
        
            col = -1
            while col < 0 or col > 9:
                col = int(raw_input('Enter Col [0-9]: '))

            spot = p2_warzone.get_spot((row,col))
            if not spot == '+' and not spot == '0' and not spot == 'X':
                p1_radar.update((row,col), 'X')
                p2_warzone.ships[p2_warzone.get_spot((row,col))][0] += 1
                p2_warzone.field[row][col] = 'X'
                os.system('cls' if os.name=='nt' else 'clear')
                p1_radar.print_radar()
                print 'HIT!'

            if p2_warzone.defeat():
                print p1_warzone.name, 'Wins!'
                break
            
            pause = raw_input('Press Enter For Player 2')
        
        #Player 2       
        elif turn == 2:
            os.system('cls' if os.name=='nt' else 'clear')
            p2_radar.print_radar()

            row = -1
            while row < 0 or row > 9:
                row = raw_input('Enter Row [0-9](\'w\' to view your warzone): ')
                if row == 'w':
                    os.system('cls' if os.name=='nt' else 'clear')
                    p2_warzone.print_warzone()
                    pause = raw_input('Press Enter')
                    os.system('cls' if os.name=='nt' else 'clear')
                    p2_radar.print_radar()
                else:
                    try:
                        row = int(row)
                    except:
                        print 'Enter a valid Number!'
        
            col = -1
            while col < 0 or col > 9:
                col = int(raw_input('Enter Col [0-9]: '))

            spot = p1_warzone.get_spot((row,col))
            if not spot == '+' and not spot == '0' and not spot == 'X':
                p2_radar.update((row,col), 'X')
                p1_warzone.ships[p1_warzone.get_spot((row,col))][0] += 1
                p1_warzone.field[row][col] = 'X'
                os.system('cls' if os.name=='nt' else 'clear')
                print 'HIT!'
                p2_radar.print_radar()

            if p1_warzone.defeat():
                print p2_warzone.name, 'Wins!'
                break

            pause = raw_input('Press Enter For Player 1')
        
        #Change Turns
        if turn == 1: turn = 2
        elif turn == 2: turn = 1
