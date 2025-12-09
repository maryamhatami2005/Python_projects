import random

class TicTacToe:
    def __init__(self):
        self.board = [" "] * 10
        #list(map(str, range(10)))  # ignre index
        self.player_turn = self.get_random_first_player()

    def get_random_first_player(self):
        return random.choice(("X", "O"))
    
    def show_board(self):
        print('\n')
        print(self.board[1] + " | " + self.board[2] + " | " + self.board[3])
        print("----------")
        print(self.board[4] + " | " + self.board[5] + " | " + self.board[6])
        print("----------")
        print(self.board[7] + " | " + self.board[8] + " | " + self.board[9])
        print("\n")
    
    def swap_player_turn(self):
        if self.player_turn == "X":
            self.player_turn = "O"
        else:
            self.player_turn = "X"
        return self.player_turn
    
    def is_board_filled(self):
        return " " not in self.board[1:]
    
    def fix_spot(self, cell, player):
        self.board[cell] = player
    
    def winner(self, player):
        win_combinations = [
            [1,2,3], [4,5,6], [7,8,9],
            [1,4,7], [2,5,8], [3,6,9],
            [1,5,9], [3,5,7]
        ]

        for combination in win_combinations:
            if all([self.board[cell] == player for cell in combination]):
                return True
            else:
                False

    def start(self):
        while True:
            self.show_board()
            print(f"{self.player_turn} turn")
            cell = int(input("Enter cell number from 1 to 9: "))
            self.player_turn  = self.swap_player_turn()
            if self.board[cell] == " " and cell in range(1, 10):
                self.fix_spot(cell, self.player_turn)
            else:
                print("Invalid cell number")
            
            if self.winner(self.player_turn):
                self.show_board()
                print(f"Player {self.player_turn} won!")
                break
            
            if self.is_board_filled():
                print("Draw")
                break

            else:
                print("Invalid cell number")

if __name__ == "__main__":
    game = TicTacToe()
    game.start()