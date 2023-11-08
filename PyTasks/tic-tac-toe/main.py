class Cell:
    def __init__(self, number):
        self.number = number
        self.value = ' '

    def is_empty(self):
        return self.value == ' '

    def __str__(self):
        return self.value


class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]

    def display(self):
        for i in range(0, 9, 3):
            row = self.cells[i:i + 3]
            print(' | '.join(map(str, row)))
            if i < 6:
                print('---------')

    def make_move(self, cell_number, player):
        cell = self.cells[cell_number - 1]
        if cell.is_empty():
            cell.value = player.symbol
            return True
        else:
            return False

    def check_win(self, player):
        winning_combinations = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],
            [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [1, 5, 9], [3, 5, 7]
        ]

        for combo in winning_combinations:
            if all(self.cells[i - 1].value == player.symbol for i in combo):
                return True
        return False

    def is_full(self):
        return all(cell.is_empty() for cell in self.cells)


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Game:
    def __init__(self):
        self.players = [Player('Player 1', 'X'), Player('Player 2', 'O')]
        self.board = Board()
        self.current_player = self.players[0]

    def play(self):
        while True:
            self.board.display()
            print('{}, your turn.'.format(self.current_player.name))
            cell_number = int(input('Enter cell number: '))

            if cell_number < 1 or cell_number > 9:
                print('Invalid input. Choose a number between 1 and 9.')
                continue

            if not self.board.make_move(cell_number, self.current_player):
                print('Cell is already occupied. Try again.')
                continue

            if self.board.check_win(self.current_player):
                self.board.display()
                print('{} wins!'.format(self.current_player.name))
                break
            elif self.board.is_full():
                self.board.display()
                print('It\'s a tie!')
                break

            self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]


game = Game()
game.play()
