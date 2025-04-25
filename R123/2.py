class Board:
    def __init__(self):
        # Inicializa el tablero 8x8 con las fichas centrales
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.board[3][3] = 'B'
        self.board[3][4] = 'W'
        self.board[4][3] = 'W'
        self.board[4][4] = 'B'
    
    def print_board(self):
        # Imprime el tablero con etiquetas de columnas y filas
        print("  A B C D E F G H")
        for i, row in enumerate(self.board):
            print(f"{8-i} {' '.join(row)}")
        print()
    
    def is_valid_move(self, row, col, player):
        # Detecta si un movimiento es válido para el jugador
        if self.board[row][col] != ' ':
            return False
        
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        valid = False
        for dr, dc in directions:
            r, c = row + dr, col + dc
            has_flipped = False
            while 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] != ' ':
                if self.board[r][c] == '.' + player:
                    valid = True
                    break
                elif self.board[r][c] == player:
                    has_flipped = True
                    break
                r += dr
                c += dc
            if has_flipped and valid:
                break
        return valid
    
    def make_move(self, row, col, player):
        # Realiza el movimiento en el tablero y voltea las fichas
        self.board[row][col] = '.' + player
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        flipped = []
        
        for dr, dc in directions:
            r, c = row + dr, col + dc
            to_flip = []
            while 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] != ' ':
                if self.board[r][c] == '.' + player:
                    flipped.extend(to_flip)
                    break
                elif self.board[r][c] == player:
                    break
                else:
                    to_flip.append((r, c))
                r += dr
                c += dc
            
            for fr, fc in to_flip:
                self.board[fr][fc] = '.' + player
        
        return flipped

class Player:
    def __init__(self, color):
        self.color = color
    
    def get_move(self, board):
        while True:
            try:
                move = input(f"Turno de jugador {self.color}. Ingresa una coordenada (A1-H8): ").upper()
                if len(move) != 2 or move[0] < 'A' or move[0] > 'H' or move[1] < '1' or move[1] > '8':
                    raise ValueError
                col = ord(move[0]) - ord('A')
                row = 8 - int(move[1])
                if board.is_valid_move(row, col, self.color):
                    return row, col
                else:
                    print("Movimiento inválido o no se flipa ninguna ficha.")
            except ValueError:
                print("Por favor, ingresa una coordenada válida en el formato 'A1' - 'H8'.")

class Game:
    def __init__(self):
        self.board = Board()
        self.player_black = Player('B')
        self.player_white = Player('W')
        self.current_player = self.player_black
    
    def play(self):
        while True:
            self.board.print_board()
            print(f"Turno de jugador {self.current_player.color}:")
            
            if not self.has_valid_moves(self.current_player.color):
                print(f"El jugador {self.current_player.color} no tiene movimientos válidos.")
                self.switch_player()
                if not self.has_valid_moves(self.current_player.color):
                    break
                continue
            
            row, col = self.current_player.get_move(self.board)
            flipped = self.board.make_move(row, col, self.current_player.color)
            
            print(f"Movimiento en {chr(col + ord('A'))}{8 - row}. Fichas volteadas: {len(flipped)} {flipped}")
            self.switch_player()
        
        self.board.print_board()
        self.count_and_declare_winner()
    
    def has_valid_moves(self, player):
        for row in range(8):
            for col in range(8):
                if self.board.is_valid_move(row, col, player):
                    return True
        return False
    
    def switch_player(self):
        self.current_player = self.player_white if self.current_player == self.player_black else self.player_black
    
    def count_and_declare_winner(self):
        black_count = sum(row.count('B') for row in self.board.board)
        white_count = sum(row.count('W') for row in self.board.board)
        
        print("Juego terminado.")
        print(f"Fichas negras: {black_count}")
        print(f"Fichas blancas: {white_count}")
        
        if black_count > white_count:
            print("¡Ganador: Jugador B!")
        elif white_count > black_count:
            print("¡Ganador: Jugador W!")
        else:
            print("¡Empate!")

# Inicia el juego
game = Game()
game.play()