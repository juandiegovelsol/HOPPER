class Board:
    def __init__(self):
        self.size = 8
        self.grid = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        self.initialize_board()

    def initialize_board(self):
        self.grid[3][3] = 'W'
        self.grid[3][4] = 'B'
        self.grid[4][3] = 'B'
        self.grid[4][4] = 'W'

    def display(self):
        print("  A B C D E F G H")
        for i, row in enumerate(self.grid):
            print(f"{i + 1} " + ' '.join(row))

    def is_valid_move(self, x, y, color):
        # Verifica si el movimiento es válido (incluye chequeo de límites y voltear fichas)
        return False  # Este es un simplificación; debes implementar las verificaciones

    def place_disc(self, x, y, color):
        # Coloca ficha y voltea fichas, si el movimiento es válido
        flipped_discs = []  # Lista de las fichas volteadas (usada para reportar en Game)
        # Aquí código para voltear las fichas y validar las jugadas
        return flipped_discs

    def has_valid_moves(self, color):
        # Revisa si quedan movimientos válidos para el color dado
        return False  # Cambiar esto a lógica que detecta si hay movimientos válidos

class Player:
    def __init__(self, color):
        self.color = color

    def get_move(self):
        while True:
            try:
                move = input(f"Turno de {self.color}. Ingresa movimiento (ej: C4): ").strip().upper()
                if len(move) == 2 and move[0] in "ABCDEFGH" and move[1] in "12345678":
                    x = int(move[1]) - 1
                    y = ord(move[0]) - ord('A')
                    return (x, y)
                else:
                    print("Entrada inválida. Intenta de nuevo.")
            except Exception:
                print("Error en la entrada. Intenta de nuevo.")

class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player('B'), Player('W')]
        self.current_turn = 0

    def switch_turn(self):
        self.current_turn = 1 - self.current_turn

    def play(self):
        while True:
            self.board.display()
            current_player = self.players[self.current_turn]
            if self.board.has_valid_moves(current_player.color):
                x, y = current_player.get_move()
                if self.board.is_valid_move(x, y, current_player.color):
                    flipped_discs = self.board.place_disc(x, y, current_player.color)
                    print(f"{len(flipped_discs)} fichas voltedas en: {flipped_discs}")
                else:
                    print("Movimiento inválido. Intenta de nuevo.")
                    continue
            else:
                print(f"No hay movimientos para {current_player.color}. Turno saltado.")
            if not self.board.has_valid_moves(self.players[0].color) and \
               not self.board.has_valid_moves(self.players[1].color):
                break
            self.switch_turn()
        self.declare_winner()

    def declare_winner(self):
        black_count = sum(row.count('B') for row in self.board.grid)
        white_count = sum(row.count('W') for row in self.board.grid)
        if black_count > white_count:
            winner = 'Negras'
        elif white_count > black_count:
            winner = 'Blancas'
        else:
            winner = 'Empate'
        print(f"Resultado final - Negras: {black_count}, Blancas: {white_count}. Ganador: {winner}")

# Para ejecutar el juego
if __name__ == "__main__":
    game = Game()
    game.play()