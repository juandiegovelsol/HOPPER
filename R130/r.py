import random
import os

def assign_colors(players):
    colors = [
        "\033[94m", "\033[96m", "\033[92m", "\033[95m",
        "\033[93m", "\033[97m", "\033[34m", "\033[36m",
        "\033[32m", "\033[35m", "\033[33m", "\033[90m"
    ]
    player_colors = {}
    available_colors = colors.copy()
    random.shuffle(available_colors)

    for player in players:
        if available_colors:
            player_colors[player] = available_colors.pop()
        else:
            player_colors[player] = "\033[0m"  # Default color if out of unique ones

    return player_colors

def is_correct_sequence(original, new_input):
    if len(new_input) != len(original) + 1:
        return False
    for i in range(len(original)):
        if original[i] != new_input[i]:
            return False
    return True

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    print("Ingrese los nombres de los jugadores separados por una coma y un espacio:")
    input_line = input()
    players = [p.strip() for p in input_line.split(",") if p.strip()]

    if len(players) < 2:
        print("Debe haber al menos dos jugadores.")
        return

    sentence = []
    player_colors = assign_colors(players)

    while True:
        shuffled_players = players[:]
        random.shuffle(shuffled_players)

        for player in shuffled_players:
            clear_console()
            print(f"{player_colors[player]}Turno de {player}\033[0m")
            input_sentence = input("Ingrese la oración completa con una nueva palabra al final: ")
            input_words = input_sentence.strip().split()

            if not is_correct_sequence(sentence, input_words):
                print("\033[91m¡{} ha perdido! Fin del juego.\033[0m".format(player))
                print("Oración correcta era: " + (" ".join(sentence) if sentence else "(vacía)"))
                print("Oración ingresada: " + input_sentence)
                return

            sentence = input_words

if __name__ == "__main__":
    main()