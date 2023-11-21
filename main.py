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
        for column in self.board:
            for row in column:
                if row == 'X':
                    hit_ships += 1
        return hit_ships
    
#Game logic

def RunGame():
    computer_board = GameBoard([[' '] * 8 for i in range(8)])
    users_guess_board = GameBoard([[' '] * 8 for i in range(8)])
    battleship.create_ships(computer_board)
    # start 10 turn
    turns = 10
    while turns > 0:
        GameBoard.print_board(users_guess_board)
        #get users input
        user_x_row,user_y_column = battleship.get_user_input(object)
        #check if duplicate guess
        while users_guess_board.board[user_x_row][user_y_column] == '-' or users_guess_board.board[user_x_row][user_y_column] == 'X':
            print('You gues that already')
            user_x_row,user_y_column = battleship.get_user_input(object)
        #check you hit or miss
        if  computer_board.board[user_x_row][user_y_column] == 'X':
            print('You sunk 1 of my battleships')
            users_guess_board.board[user_x_row][user_y_column] = 'X'
        else:
            print('You have miss the shoot')
            users_guess_board.board[user_x_row][user_y_column] = '-'
        #check for win or losses
        if battleship.count_hit_ships(users_guess_board) == 5:
            print('You hit all 5 battleships')
            break
        else:
            turns -= 1
            print(f'you have {turns} turns remaining')
            if turns == 0:
                print('The enemy has won the battle')
                GameBoard.print_board(users_guess_board)
                break

if __name__ == '__main__':
    RunGame()
