import random
import estilos

class JuegoTresEnRaya:
    def __init__(self):
        """Esta clase representa el juego de tres en raya."""
        self.__board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # self.__board = [estilos.color.amarillo + str(i) + estilos.color.RESET for i in range(10)]

    def mostrarTablero(self):
        """Muestra el estado actual del tablero en la consola"""
        print(estilos.color.cian + '+-------+-------+-------+', 
              '|       |       |       |', 
              f'|   {self.__board[0]}   |   {self.__board[1]}   |   {self.__board[2]}   |', 
              '|       |       |       |', 
              '+-------+-------+-------+',
              '|       |       |       |',
              f'|   {self.__board[3]}   |   {self.__board[4]}   |   {self.__board[5]}   |',
              '|       |       |       |',
              '+-------+-------+-------+',
              '|       |       |       |',
              f'|   {self.__board[6]}   |   {self.__board[7]}   |   {self.__board[8]}   |',
              '|       |       |       |',
              '+-------+-------+-------+' + estilos.color.RESET, sep='\n')

    def introducirMovimiento(self):
        """ La función pregunta al usuario acerca de su movimiento y actualiza el tablero"""

        # Comprueba si hay ganador
        if self.comprobarVictoria('X'):
            print(estilos.color.naranja + 'El ganador es la máquina.' + estilos.color.RESET)
            exit()

        elif self.comprobarVictoria('O'):
            print(estilos.color.verde + 'El ganador eres tú.' + estilos.color.RESET)
            exit()

        while True:
            user_move = input(estilos.color.azul + 'Ingresa tu movimiento (1-9) o "exit" para salir: ' + estilos.color.RESET)
            if user_move == 'exit':
                print('¡Adiós!')
                exit()

            try:
                user_move = int(user_move)
                if user_move < 1 or user_move > 9:
                    raise ValueError(estilos.color.rojo + "Movimiento fuera de rango." + estilos.color.RESET)
            
            except ValueError:
                print(estilos.color.rojo + "Movimiento no válido. Debes ingresar un número entre 1 y 9." + estilos.color.RESET)
                continue

            if self.__board[user_move - 1] in ['X', 'O']:
                print(estilos.color.naranja + 'Cuadrado ocupado. Intenta de nuevo.' + estilos.color.RESET)
            else:
                self.__board[user_move - 1] = estilos.color.naranja + 'O' + estilos.color.RESET
                break

    def escribirMovimiento(self):
        """La función dibuja el movimiento de la máquina y actualiza el tablero."""

        while True:
            case = random.randint(1, 9) - 1  # Convertimos a índice de lista
            if self.__board[case] not in ['X', 'O']:
                self.__board[case] = estilos.color.rojo + 'X' + estilos.color.RESET
                break

        # Comprueba si hay ganador
        if self.comprobarVictoria('X'):
            print(estilos.color.naranja + 'El ganador es la máquina.' + estilos.color.RESET)
            exit()

        elif self.comprobarVictoria('O'):
            print(estilos.color.verde + 'El ganador eres tú.' + estilos.color.RESET)
            exit()

    def comprobarTableroLleno(self):
        """La función examina el tablero y termina el juego si no hay cuadros vacíos."""
        if all(spot in ['X', 'O'] for spot in self.__board):
            print(estilos.color.naranja + 'Empate.' + estilos.color.RESET)
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
            if all(self.__board[i] == sign for i in combinacion):
                return True
        return False

    def iniciarJuego(self):
        """Inicia el juego y alterna los turnos entre el usuario y la máquina"""
        while True: 
            # Muestra el tablero
            self.mostrarTablero()

            # Pide al usuario su movimiento
            self.introducirMovimiento()

            # Comprobar si el tablero está lleno
            self.comprobarTableroLleno()

            # Vuelve a mostrar el tablero
            self.mostrarTablero()

            # Hace el movimiento del robot
            self.escribirMovimiento()

            # Comprobar si el tablero está lleno
            self.comprobarTableroLleno()

# Crear una instancia del juego y comenzar
juego = JuegoTresEnRaya()
juego.iniciarJuego()
