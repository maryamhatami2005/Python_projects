import random

from prettytable import PrettyTable, TableStyle


class TicTacToe:
    def __init__(self):
        """Initialize an empty list for the board and randomly choses the firt player
        """
        self.board = [" "] * 10 # ignre index 0
        self.player_turn = self.get_random_first_player()

    def get_random_first_player(self) -> str:
        return random.choice(("X", "O"))
    
    def show_board(self) -> None:
        table = PrettyTable()
        table.add_row([self.board[1], self.board[2], self.board[3]])
        table.add_divider()
        table.add_row([self.board[4], self.board[5], self.board[6]])
        table.add_divider()
        table.add_row([self.board[7], self.board[8], self.board[9]])
        table.set_style(TableStyle.SINGLE_BORDER)
        table.header = False
        print(table)
    
    def swap_player_turn(self) -> str:
        if self.player_turn == "X":
            self.player_turn = "O"
        else:
            self.player_turn = "X"
        return self.player_turn 
    
    def is_board_filled(self) -> bool:
        return " " not in self.board[1:]
    
    def fix_spot(self, cell, player)-> None:
        self.board[cell] = player
    
    def winner(self, player)-> bool:
        win_combinations = [
            [1,2,3], [4,5,6], [7,8,9],
            [1,4,7], [2,5,8], [3,6,9],
            [1,5,9], [3,5,7]
        ]

        for combination in win_combinations:
            if all(self.board[cell] == player for cell in combination):
                return True

        return False

    def start(self):
        while True:
            self.show_board()
            print(f"{self.player_turn}'s turn")

            cell = input("Enter cell number from 1 to 9: ")

            while not cell.isdigit():
                print("Enter a number from 1 to 9")
                cell = input("Enter cell number from 1 to 9: ")
            cell = int(cell)


            while cell not in range(1,10):
                print("Invalid cell number.Try again.")
                cell = int(input("Enter cell number from 1 to 9: "))
            
            while self.board[cell] != " ":
                print("Cell already taken. Choose another.")
                cell = int(input("Enter cell number from 1 to 9: "))


            if self.board[cell] == " ":
                self.fix_spot(cell, self.player_turn)


            if self.winner(self.player_turn):
                self.show_board()
                print(f"Player {self.player_turn} won!")
                break

            self.player_turn  = self.swap_player_turn()

            if self.is_board_filled():
                print("Draw!")
                break


if __name__ == "__main__":
    game = TicTacToe()
    game.start()