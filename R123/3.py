
class Board:
    def __init__(self):
        self.board = [['.' for _ in range(8)] for _ in range(8)]
        self.board[3][3] = 'N'
        self.board[3][4] = 'B'
        self.board[4][3] = 'B'
        self.board[4][4] = 'N'

    def print_board(self):
        print("  A B C D E F G H")
        for i in range(8):
            print(f"{i+1} " + " ".join(self.board[i]))
        print()

    def on_board(self, r, c):
        return 0 <= r < 8 and 0 <= c < 8

    def get_flips(self, row, col, color):
        if self.board[row][col] != '.':
            return []
        opponent = 'B' if color == 'N' else 'N'
        flips = []
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            line = []
            while self.on_board(r, c) and self.board[r][c] == opponent:
                line.append((r, c))
                r += dr
                c += dc
            if self.on_board(r, c) and self.board[r][c] == color and line:
                flips.extend(line)
        return flips

    def is_valid_move(self, row, col, color):
        return bool(self.get_flips(row, col, color))

    def place_disc(self, row, col, color):
        flips = self.get_flips(row, col, color)
        if not flips:
            return []
        self.board[row][col] = color
        for r, c in flips:
            self.board[r][c] = color
        return flips

    def has_valid_moves(self, color):
        for r in range(8):
            for c in range(8):
                if self.is_valid_move(r, c, color):
                    return True
        return False

    def full(self):
        return all(self.board[r][c] != '.' for r in range(8) for c in range(8))


class Player:
    def __init__(self, color):
        self.color = color

    def get_move(self, board):
        name = 'Negras' if self.color == 'N' else 'Blancas'
        while True:
            move = input(f"Turno de {name} ({self.color}). Ingresa coordenada (A1–H8): ").upper().strip()
            if len(move) == 2 and move[0] in "ABCDEFGH" and move[1] in "12345678":
                col = ord(move[0]) - ord('A')
                row = int(move[1]) - 1
                if board.is_valid_move(row, col, self.color):
                    return row, col
                else:
                    print("Movimiento inválido: no voltea ninguna ficha. Intenta de nuevo.")
            else:
                print("Formato inválido. Usa letra A–H seguida de número 1–8 (ej. D3).")


class Game:
    def __init__(self):
        self.board = Board()
        self.player_black = Player('N')
        self.player_white = Player('B')
        self.current_player = self.player_black

    def switch_player(self):
        self.current_player = (
            self.player_white
            if self.current_player == self.player_black
            else self.player_black
        )

    def play(self):
        while True:
            self.board.print_board()
            color = self.current_player.color
            name = 'Negras' if color == 'N' else 'Blancas'

            if self.board.has_valid_moves(color):
                row, col = self.current_player.get_move(self.board)
                flips = self.board.place_disc(row, col, color)
                flips_str = [f"{chr(c + ord('A'))}{r+1}" for r, c in flips]
                print(f"Se voltearon {len(flips)} fichas en: {', '.join(flips_str)}")
                self.switch_player()
                next_name = 'Negras' if self.current_player.color == 'N' else 'Blancas'
                print(f"Siguiente turno: {next_name}\n")
            else:
                print(f"No hay movimientos válidos para {name}. Turno saltado.\n")
                self.switch_player()
                if not self.board.has_valid_moves(self.current_player.color):
                    break

            if self.board.full() or (
               not self.board.has_valid_moves('N') and
               not self.board.has_valid_moves('B')
            ):
                break

        self.board.print_board()
        self.declare_winner()

    def declare_winner(self):
        black_count = sum(row.count('N') for row in self.board.board)
        white_count = sum(row.count('B') for row in self.board.board)
        print("Juego terminado.")
        print(f"Fichas Negras (N): {black_count} | Fichas Blancas (B): {white_count}")
        if black_count > white_count:
            print("¡Ganador: Negras (N)!")
        elif white_count > black_count:
            print("¡Ganador: Blancas (B)!")
        else:
            print("¡Empate!")


if __name__ == "__main__":
    Game().play()