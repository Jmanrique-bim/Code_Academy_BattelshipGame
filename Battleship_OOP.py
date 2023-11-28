import random

class BattleshipGame:
    def __init__(self):
        self.LENGTH_OF_SHIPS = [2, 3, 3, 4, 5]
        self.PLAYER_BOARD = [[" "] * 8 for _ in range(8)]
        self.COMPUTER_BOARD = [[" "] * 8 for _ in range(8)]
        self.PLAYER_GUESS_BOARD = [[" "] * 8 for _ in range(8)]
        self.COMPUTER_GUESS_BOARD = [[" "] * 8 for _ in range(8)]
        self.LETTERS_TO_NUMBERS = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

    def print_board(self, board):
        print("  A B C D E F G H")
        print("  +-+-+-+-+-+-+-+")
        row_number = 1
        for row in board:
            print('{}|{}'.format(row_number, '|'.join(row)))
            row_number += 1

    def check_ship_fit(self, SHIP_LENGTH, row, column, orientation):
        if orientation == "H":
            return column + SHIP_LENGTH <= 8
        else:
            return row + SHIP_LENGTH <= 8

    def ship_overlaps(self, board, row, column, orientation, ship_length):
        if orientation == "H":
            return any(board[row][i] == "X" for i in range(column, column + ship_length))
        else:
            return any(board[i][column] == "X" for i in range(row, row + ship_length))

    def place_ships(self, board):
        for ship_length in self.LENGTH_OF_SHIPS:
            while True:
                if board == self.COMPUTER_BOARD:
                    orientation, row, column = random.choice(["H", "V"]), random.randint(0, 7), random.randint(0, 7)
                    if self.check_ship_fit(ship_length, row, column, orientation) and not self.ship_overlaps(board, row, column, orientation, ship_length):
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "X"
                        break
                else:
                    place_ship = True
                    print('Place the ship with a length of ' + str(ship_length))
                    row, column, orientation = self.user_input(place_ship)
                    if self.check_ship_fit(ship_length, row, column, orientation) and not self.ship_overlaps(board, row, column, orientation, ship_length):
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "X"
                        self.print_board(self.PLAYER_BOARD)
                        break

    def user_input(self, place_ship):
        if place_ship:
            while True:
                try:
                    orientation = input("Enter orientation (H or V): ").upper()
                    if orientation == "H" or orientation == "V":
                        break
                except TypeError:
                    print('Enter a valid orientation H or V')
            while True:
                try:
                    row = input("Enter the row 1-8 of the ship: ")
                    if row in '12345678':
                        row = int(row) - 1
                        break
                except ValueError:
                    print('Enter a valid letter between 1-8')
            while True:
                try:
                    column = input("Enter the column of the ship: ").upper()
                    if column in 'ABCDEFGH':
                        column = self.LETTERS_TO_NUMBERS[column]
                        break
                except KeyError:
                    print('Enter a valid letter between A-H')
            return row, column, orientation
        else:
            while True:
                try:
                    row = input("Enter the row 1-8 of the ship: ")
                    if row in '12345678':
                        row = int(row) - 1
                        break
                except ValueError:
                    print('Enter a valid letter between 1-8')
            while True:
                try:
                    column = input("Enter the column of the ship: ").upper()
                    if column in 'ABCDEFGH':
                        column = self.LETTERS_TO_NUMBERS[column]
                        break
                except KeyError:
                    print('Enter a valid letter between A-H')
            return row, column

    def count_hit_ships(self, board):
        return sum(row.count("X") for row in board)

    def turn(self, board):
        if board == self.PLAYER_GUESS_BOARD:
            row, column = self.user_input(True)
            if board[row][column] == "-":
                self.turn(board)
            elif board[row][column] == "X":
                self.turn(board)
            elif self.COMPUTER_BOARD[row][column] == "X":
                board[row][column] = "X"
            else:
                board[row][column] = "-"
        else:
            row, column = random.randint(0, 7), random.randint(0, 7)
            if board[row][column] == "-":
                self.turn(board)
            elif board[row][column] == "X":
                self.turn(board)
            elif self.PLAYER_BOARD[row][column] == "X":
                board[row][column] = "X"
            else:
                board[row][column] = "-"

    def play_game(self):
        self.place_ships(self.COMPUTER_BOARD)
        self.print_board(self.COMPUTER_BOARD)
        self.print_board(self.PLAYER_BOARD)
        self.place_ships(self.PLAYER_BOARD)

        while True:
            # Player turn
            while True:
                print('Guess a battleship location')
                self.print_board(self.PLAYER_GUESS_BOARD)
                self.turn(self.PLAYER_GUESS_BOARD)
                break
            if self.count_hit_ships(self.PLAYER_GUESS_BOARD) == 17:
                print("You win!")
                break

            # Computer turn
            while True:
                self.turn(self.COMPUTER_GUESS_BOARD)
                break
            self.print_board(self.COMPUTER_GUESS_BOARD)
            if self.count_hit_ships(self.COMPUTER_GUESS_BOARD) == 17:
                print("Sorry, the computer won.")
                break

# Create an instance of the BattleshipGame class and start the game
game = BattleshipGame()
game.play_game()
