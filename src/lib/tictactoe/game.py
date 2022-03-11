# write tick-tac-toe game
class game:
    def __init__(self):
        self.board = [[' ' for i in range(3)] for j in range(3)]
        self.player = 'X'
        self.winner = None
        self.game_over = False
        self.num_moves = 0

    def display_board(self):
        print('\n' * 100)
        print(' ' + self.board[0][0] + ' | ' + self.board[0][1] + ' | ' + self.board[0][2] + ' ')
        print('-----------')
        print(' ' + self.board[1][0] + ' | ' + self.board[1][1] + ' | ' + self.board[1][2] + ' ')
        print('-----------')
        print(' ' + self.board[2][0] + ' | ' + self.board[2][1] + ' | ' + self.board[2][2] + ' ')
        print('\n')

    def play_move(self, row, col):
        if self.game_over:
            print('Game is over!')
            return
        if self.board[row][col] == ' ':
            self.board[row][col] = self.player
            self.num_moves += 1
            self.switch_player()
        else:
            print('Invalid move!')

    def switch_player(self):
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

    def check_win(self):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != ' ':
                self.winner = self.board[row][0]
                self.game_over = True
                return
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                self.winner = self.board[0][col]
                self.game_over = True
                return
class game_test:
    def __init__(self):
        self.game = game()
        self.game.display_board()
        while not self.game.game_over:
            row = int(input('Enter row: '))
            col = int(input('Enter col: '))
            self.game.play_move(row, col)
            self.game.display_board()
        if self.game.winner == None:
            print('Tie!')
        else:
            print('Winner is ' + self.game.winner)
# def main():
#     game = game()
#     game.display_board()
#     while not game.game_over:
#         row = int(input('Enter row: '))
#         col = int(input('Enter col: '))
#         game.play_move(row, col)
#         game.display_board()
#     if game.winner == None:
#         print('Tie!')
#     else:
#         print('Winner is ' + game.winner)


        