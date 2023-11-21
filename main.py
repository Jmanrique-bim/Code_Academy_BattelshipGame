import random

class GameBoard:
    def __init__(self,board):
        self.board = board
    # Create a dictionary for user input 
    def get_letters_to_numbers():
        letters_to_numners = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
        return letters_to_numners
    # Print the board
    def print_board(self):
        print(' A B C D E F G H')
        print(' +-+-+-+-+-+-+-+')
        row_number = 1
        for row in self.board:
            print('%d|%s' % (row_number, '|'.join(row)))
            row_number += 1
            
class battleship:
    
    #select a game board
    def __init__(self,board):
        self.board = board
        
    #Create ships by replacing '-' to 'X'
    def create_ships(self):
        for i in range(5):
            self.x_row,self.y_colum = random.randint(0,7),random.randint(0,7)
            # if the colum or the row has already a 'X' randomize again til find an empty space, then place a 'X'
            while self.board[self.x_row][self.y_colum] == 'X':
                self.x_row,self.y_colum = random.randint(0,7),random.randint(0,7)
            self.board[self.x_row][self.y_colum] = 'X'
        return self.board
    
    def get_user_input(self):
        try:
            x_row = input('Enter the row of the ship: ')
            while x_row not in '12345678':
                print('Not an appropiate choice, please select a valid row')
                x_row = input('Enter the row of the ship: ')
                
            y_column = input('Enter the column letter of the ship: ').upper()
            while y_column not in 'ABCDEFGH':
                print('Not an appropiate choice, please select a valid row')
            return int(x_row) -1, GameBoard.get_letters_to_numbers()[y_column]
        except ValueError and KeyError:
            print('Not valid input')
            return self.get_user_input
    
    def count_hit_ships(self):
        hit_ships = 0
        for column in hit_ships:
            for row in column:
                if row == 'X':
                    hit_ships += 1
        return hit_ships
