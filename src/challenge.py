import math

# Representación del tablero: lista de 9 elementos (' ', 'X', 'O')
# Índices de la consola:
# 0 | 1 | 2
# ---------
# 3 | 4 | 5
# ---------
# 6 | 7 | 8

def print_board(board: list[str]) -> None:
    """Dibuja el tablero en la consola."""
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_winner(board: list[str]) -> str | None:
    """Retorna 'X' o 'O' si hay ganador, 'Empate' si no hay espacio, o None si el juego sigue."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontales
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Verticales
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    for r in win_conditions:
        if board[r[0]] == board[r[1]] == board[r[2]] != " ":
            return board[r[0]]
    if " " not in board:
        return "Empate"
    return None

def get_terminal_score(winner: str | None) -> int | None:
    """Mapea el estado final del juego a su respectivo valor numérico."""
    scores = {"O": 1, "X": -1, "Empate": 0}
    return scores.get(winner) if winner else None

def _maximize(board: list[str], alpha: float, beta: float) -> int:
    """Evalúa los movimientos para el jugador maximizador (Inteligencia Artificial)."""
    best_score = -math.inf
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"  # Simular jugada de la IA
            score = alpha_beta_ttt(board, False, alpha, beta)
            board[i] = " "  # Deshacer jugada
            best_score = max(score, best_score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break  # Poda Alfa-Beta
    return best_score

def _minimize(board: list[str], alpha: float, beta: float) -> int:
    """Evalúa los movimientos para el jugador minimizador (Usuario Humano)."""
    best_score = math.inf
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"  # Simular jugada del Humano
            score = alpha_beta_ttt(board, True, alpha, beta)
            board[i] = " "  # Deshacer jugada
            best_score = min(score, best_score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break  # Poda Alfa-Beta
    return best_score

def alpha_beta_ttt(board: list[str], is_maximizing: bool, alpha: float, beta: float) -> int:
    """Algoritmo Poda Alfa-Beta adaptado dinámicamente para Tres en Raya."""
    winner = check_winner(board)
    score = get_terminal_score(winner)
    if score is not None:
        return score

    if is_maximizing:
        return _maximize(board, alpha, beta)
    return _minimize(board, alpha, beta)

def get_best_move(board: list[str]) -> int:
    """Encuentra el mejor movimiento posible para la IA ('O') en el estado actual."""
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = alpha_beta_ttt(board, False, -math.inf, math.inf)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    """Bucle principal de control del juego por consola."""
    board = [" "] * 9
    print("=== RETO: TRES EN RAYA CON PODA ALFA-BETA ===")
    print("Tú juegas como 'X' y la Inteligencia Artificial como 'O'")
    print("Ingresa un número del 0 al 8 para elegir tu casilla.")
    print_board(board)

    while check_winner(board) is None:
        # Turno del Humano
        try:
            human_move = int(input("Tu turno (0-8): "))
            if board[human_move] != " ":
                print("¡Esa casilla ya está ocupada! Elige otra.")
                continue
        except (ValueError, IndexError):
            print("Entrada inválida. Ingresa un número válido entre 0 y 8.")
            continue

        board[human_move] = "X"
        print_board(board)

        if check_winner(board) is not None:
            break

        # Turno de la IA
        print("La Inteligencia Artificial está calculando su mejor jugada...")
        ai_move = get_best_move(board)
        if ai_move != -1:
            board[ai_move] = "O"
            print(f"La IA eligió la posición: {ai_move}")
            print_board(board)

    # Resultado final
    result = check_winner(board)
    if result == "Empate":
        print("¡Es un empate! El agente adversarial es imbatible.")
    elif result == "O":
        print("¡La Inteligencia Artificial te ha ganado!")
    else:
        print("¡Increíble, lograste ganarle a la IA!")

if __name__ == "__main__":
    play_game()