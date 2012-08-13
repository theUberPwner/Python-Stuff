#Python: Tic Tac Toe
#Computer blocks winning moves and plays randomly otherwise
#If number of games to play is greater than 1 the computer will automatically
#play out that many games and return the results. You can also view any of these
#games (including each turn taken) once they are complete.
import random

class TicTacToe():
    #variables used for computer play
    x_wins = 0
    o_wins = 0
    ties = 0
    
    #display the game board    
    def show(self,board=None):
        if board == None:
            board = self.board
            
        print '##############'
        print ' ',board[0],'|',board[1],'|',board[2]
        print '  ----------'
        print ' ',board[3],'|',board[4],'|',board[5]
        print '  ----------'
        print ' ',board[6],'|',board[7],'|',board[8]
        print '##############'
        
    #display game board from list of turns
    def show_old(self,turns):
        b = [1,2,3,4,5,6,7,8,9]
        
        for t in turns:
            b[t[1]-1] = t[0]
            
        self.show(board=b)

    #initial take_turn method that passes the player to either take_cturn 
    #or take_pturn depending on whether or not is computer player
    def take_turn(self, p):
        if self.computer[p]:
            self.take_cturn(p)
        else:
            self.take_pturn(p)
        
    #human turn
    def take_pturn(self, p):
        input = int(raw_input(p + ': Select a spot: '))
        while input < 1 or input > 9:
            input = int(raw_input(p + ': Select a spot'))  

        self.check_spot(input, p, False)
        
        self.show()

    #computer turn
    def take_cturn(self, p):
        #first check if you can win
        if p == 'X' and self.win_next('X') != -1:
            s = self.win_next('X')          
            self.check_spot(s, p, True)
        elif p == 'O' and self.win_next('O') != -1:
            s = self.win_next('O')
            self.check_spot(s, p, True)
        else:
            #then check if the opponent can win and stop him
            if p == 'X' and self.win_next('O') != -1:
                s = self.win_next('O')
                self.check_spot(s, p, True)
            elif p == 'O' and self.win_next('X') != -1:
                s = self.win_next('X')
                self.check_spot(s, p, True)
            else:
                random.seed() #create random generator
                s = random.randint(1, 9)
                
                self.check_spot(s, p, True)
        
        if not self.speed_mode:
            self.show()

    #change the spot if a valid spot was selected
    #otherwise call alert invalid spot and call take_turn again
    def check_spot(self, s, p, comp):
        board = self.board
        if not board[s-1] == 'X' and not board[s-1] == 'O' and s >= 1 and s <= 9:
            board[s-1] = p
            self.path.append((p, s))
            if not self.speed_mode:
                print str(p) + ' takes spot ' + str(s)
        else:
            if comp:
                self.take_cturn(p)
            else:
                print 'This spot is taken!'
                self.take_pturn(p)

    #check for win or end of game
    #returns 'X' if 'X' wins
    #        'O' if 'O' wins
    #        't' if tie
    #        'p' if game is not over
    def check_win(self): 
        board = self.board
        for line in self.win_lines:
            if board[line[0]] == board[line[1]] and board[line[1]] == board[line[2]]:
                #someone won!
                return board[line[0]]
        
        #if no winner then check for full board
        for spot in board:
            if not spot == 'X' and not spot == 'O':
                #deteted an unused spot so not an empty board
                return 'p'
                
        #made it through the loop so it is an empty board
        return 't'

    #check if a player is about to win and return
    #the spot it needs to win so the computer can block it
    def win_next(self, p):
        board = self.board
        for line in self.win_lines:
            if board[line[0]] == board[line[1]] and board[line[0]] == p:
                if board[line[2]] == (line[2] + 1):
                    return line[2] + 1
            elif board[line[1]] == board[line[2]] and board[line[1]] == p:
                if board[line[0]] == (line[0] + 1):
                    return line[0] + 1
            elif board[line[0]] == board[line[2]] and board[line[0]] == p:
                if board[line[1]] == (line[1] + 1):
                    return line[1] + 1
        
        return -1

    def new_game(self, allcomp=False):
        self.speed_mode=allcomp

        self.path = []

        #the game board
        #board numbers do not match array index to avoid confusion between '0' and 'o'
        self.board = [1,2,3,
                      4,5,6,
                      7,8,9]

        #list of all possible ways to win
        self.win_lines = [(0,1,2),(3,4,5),(6,7,8),
                          (0,3,6),(1,4,7),(2,5,8), 
                          (0,4,8),(2,4,6)]

        self.computer = {'X': False, 'O':False}      

        #get number of players from user input
        #loop while invalid number
        players = -1
        if not allcomp:
            while not players == '1' and not players == '2':
                players = raw_input('Number of Players (1 or 2):')
                if players == '1':
                    self.computer['O'] = True
                    self.show() #show the initial game board
                elif players == '2':
                    self.show() #show the initial game board
                else:
                    print 'Please select either 1 or 2'
        else:
            self.computer['X'] = True
            self.computer['O'] = True
            
            
        #main game loop
        while 1:
            #x turn
            self.take_turn('X')
            if not self.speed_mode:
                print ""

            if not self.check_win() == 'p':
                break

            #o turn
            self.take_turn('O')
            if not self.speed_mode:
                print ""

            if not self.check_win() == 'p':
                break
                
        #game is over, lets see who one
        if self.check_win() == 'X':
            print 'X Wins!'
            self.x_wins += 1
        elif self.check_win() == 'O':
            print 'O Wins!'
            self.o_wins += 1
        elif self.check_win() == 't':
            print 'Tie Game!'
            self.ties += 1

if __name__ == '__main__':
    loop = int(raw_input('Enter number of games to play: '))

    game_data = {}

    TTT = TicTacToe()

    if loop == 1:
        TTT.new_game()
    else:
        for x in range(1,loop):
            print 'Game ' + str(x)
            TTT.new_game(allcomp=True) #set allcomp = True to prevent stuff being printed to the screen and bypass player prompt
            game_data[x] = TTT.path
            TTT.show()
            print ''

        x_perc = (TTT.x_wins / float(loop)) * 100
        o_perc = (TTT.o_wins / float(loop)) * 100
        t_perc = (TTT.ties / float(loop)) * 100
        
        print ''
        print 'Results'
        print '-------'
        print 'X: ' + str(TTT.x_wins) + ' wins.' + str(x_perc) + '%'
        print 'O: ' + str(TTT.o_wins) + ' wins.' + str(o_perc) + '%'
        print str(TTT.ties) + ' ties.' + str(t_perc) + '%'

        while 1:
            game = raw_input('Enter the game you wish to view (q: quit):')
            if game == 'q':
                break

            game = int(game)
            print game_data[game]
            TTT.show_old(game_data[game])
