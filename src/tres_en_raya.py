import random

class JuegoTresEnRaya:
    def __init__(self):
        """Esta clase representa el juego de tres en raya."""
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def mostrarTablero(self):
        """Muestra el estado actual del tablero en la consola"""
        print('+-------+-------+-------+', 
              '|       |       |       |', 
              f'|   {self.board[0]}   |   {self.board[1]}   |   {self.board[2]}   |', 
              '|       |       |       |', 
              '+-------+-------+-------+',
              '|       |       |       |',
              f'|   {self.board[3]}   |   {self.board[4]}   |   {self.board[5]}   |',
              '|       |       |       |',
              '+-------+-------+-------+',
              '|       |       |       |',
              f'|   {self.board[6]}   |   {self.board[7]}   |   {self.board[8]}   |',
              '|       |       |       |',
              '+-------+-------+-------+', sep='\n')

    def introducirMovimiento(self):
        """ La función pregunta al usuario acerca de su movimiento y actualiza el tablero"""

        # Comprueba si hay ganador
        if self.victory_for('X'):
            print('El ganador es la máquina.')
            exit()

        elif self.victory_for('O'):
            print('El ganador eres tú.')
            exit()

        while True:
            user_move = input('Ingresa tu movimiento (1-9) o "exit" para salir: ')
            if user_move == 'exit':
                print('¡Adiós!')
                exit()

            try:
                user_move = int(user_move)
                if user_move < 1 or user_move > 9:
                    raise ValueError("Movimiento fuera de rango.")
            except ValueError:
                print("Movimiento no válido. Debes ingresar un número entre 1 y 9.")
                continue

            if self.board[user_move - 1] in ['X', 'O']:
                print('Cuadrado ocupado. Intenta de nuevo.')
            else:
                self.board[user_move - 1] = 'O'
                break

    def escribirMovimiento(self):
        """La función dibuja el movimiento de la máquina y actualiza el tablero."""

        while True:
            case = random.randint(1, 9) - 1  # Convertimos a índice de lista
            if self.board[case] not in ['X', 'O']:
                self.board[case] = 'X'
                break

        # Comprueba si hay ganador
        if self.victory_for('X'):
            print('El ganador es la máquina.')
            exit()

        elif self.victory_for('O'):
            print('El ganador eres tú.')
            exit()

    def comprobarTableroLleno(self):
        """La función examina el tablero y termina el juego si no hay cuadros vacíos."""
        if all(spot in ['X', 'O'] for spot in self.board):
            print('Empate.')
            exit()

    def comprobarVictoria(self, sign):
        """La función analiza el estatus del tablero para verificar el ganador"""
        combinaciones_ganadoras = (
            (0, 1, 2),  # Fila 1
            (3, 4, 5),  # Fila 2
            (6, 7, 8),  # Fila 3
            (0, 3, 6),  # Columna 1
            (1, 4, 7),  # Columna 2
            (2, 5, 8),  # Columna 3
            (0, 4, 8),  # Diagonal principal
            (2, 4, 6)   # Diagonal secundaria
        )

        for combinacion in combinaciones_ganadoras:
            if all(self.board[i] == sign for i in combinacion):
                return True
        return False

    def iniciarJuego(self):
        """Inicia el juego y alterna los turnos entre el usuario y la máquina"""
        while True: 
            # Muestra el tablero
            self.display_board()

            # Pide al usuario su movimiento
            self.enter_move()

            # Comprobar si el tablero está lleno
            self.check_board_is_full()

            # Vuelve a mostrar el tablero
            self.display_board()

            # Hace el movimiento del robot
            self.draw_move()

            # Comprobar si el tablero está lleno
            self.check_board_is_full()

# Crear una instancia del juego y comenzar
juego = JuegoTresEnRaya()
juego.iniciar_juego()
