import random
import estilos
import os

class JuegoTresEnRaya:

    # Constantes para los signos del usuario y la máquina
    SIGN_USER = estilos.color.amarillo + 'O' + estilos.color.cian
    SIGN_MAQUINA = estilos.color.rojo + 'X' + estilos.color.cian

    def __init__(self):
        """Esta clase representa el juego de tres en raya."""
        self.__board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.sign_user = self.SIGN_USER
        self.sign_maquina = self.SIGN_MAQUINA

    def mostrarTablero(self):
        """Muestra el estado actual del tablero en la consola"""
        print(estilos.color.cian + '\t+-------+-------+-------+', 
              '\t|       |       |       |', 
              f'\t|   {self.__board[0]}   |   {self.__board[1]}   |   {self.__board[2]}   |', 
              '\t|       |       |       |', 
              '\t+-------+-------+-------+',
              '\t|       |       |       |',
              f'\t|   {self.__board[3]}   |   {self.__board[4]}   |   {self.__board[5]}   |',
              '\t|       |       |       |',
              '\t+-------+-------+-------+',
              '\t|       |       |       |',
              f'\t|   {self.__board[6]}   |   {self.__board[7]}   |   {self.__board[8]}   |',
              '\t|       |       |       |',
              '\t+-------+-------+-------+' + estilos.color.RESET, sep='\n')

    def introducirEscribirMovimiento(self):
        """La función pregunta al usuario acerca de su movimiento y actualiza el tablero"""
        while True:
            try:
                user_move = input(estilos.color.azul + '\nIngresa tu movimiento (1-9) [exit -> para salir]: ' + estilos.color.RESET)
            
            except KeyboardInterrupt:
                print() # Salto de línea
                print(estilos.color.azul + '¡Adiós!' + estilos.color.RESET)
                exit() # Sale del juego

            if user_move == 'exit':
                print(estilos.color.azul + '\n¡Adiós!' + estilos.color.RESET)
                exit() # Sale del juego

            try:
                user_move = int(user_move)
                if user_move < 1 or user_move > 9:
                    # Lanzar una excepción si el movimiento está fuera de rango
                    raise ValueError(estilos.color.rojo + "\nMovimiento fuera de rango." + estilos.color.RESET)
            
            except ValueError:
                # Capturar la excepción y mostrar un mensaje de error
                print(estilos.color.rojo + "\nMovimiento no válido. Debes ingresar un número entre 1 y 9." + estilos.color.RESET)
                continue
            
            # Comprobar si el cuadrado está ocupado
            if self.__board[user_move - 1] in [self.sign_maquina, self.sign_user]:
                print(estilos.color.naranja + '\nCuadrado ocupado. Intenta de nuevo.' + estilos.color.RESET)

            # Si el cuadrado está vacío, actualiza el tablero
            else:
                self.__board[user_move - 1] = self.sign_user
                break

    def escribirMovimientoMaquina(self):
        """La función dibuja el movimiento de la máquina y actualiza el tablero."""
        while True:

            case = random.randint(1, 9) - 1  # Convertimos a índice de lista

            # Si el cuadrado está ocupado, la máquina lo intenta de nuevo
            if self.__board[case] not in [self.sign_maquina, self.sign_user]:
                self.__board[case] = self.sign_maquina
                break

    def comprobarTableroLleno(self):
        """La función examina el tablero y termina el juego si no hay cuadros vacíos."""
        # Si todos los cuadros están ocupados, el juego termina en empate
        if all(spot in [self.sign_maquina, self.sign_user] for spot in self.__board):
            print(estilos.color.naranja + '\nEmpate.' + estilos.color.RESET)
            return True
        
        # Si hay cuadros vacíos, el juego continúa
        else:
            return False

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

        # Comprobar si hay una combinación ganadora
        for combinacion in combinaciones_ganadoras:
            if all(self.__board[i] == sign for i in combinacion):
                # Cambiar el color de los cuadrados ganadores
                for i in combinacion:
                    self.__board[i] = estilos.color.verde + f"{self.__board[i]}" + estilos.color.cian
                
                return True
            
        # Si no hay combinaciones ganadoras, el juego continúa
        return False
    
    def limpiarTerminal(self):
        """Limpia la pantalla de la terminal"""
        os.system("cls" if os.name == "nt" else "clear")
    
    def mostrarCabecera(self):
        """Muestra el título del juego"""
        print(estilos.color.purpura + '\n\t\tTRES EN RAYA' + estilos.color.RESET) # Título del juego

    def iniciarJuego(self):
        """Inicia el juego y alterna los turnos entre el usuario y la máquina"""
        
        # Bucle principal del juego
        while True:
            # Limpiar la pantalla
            self.limpiarTerminal()

            # Mostrar la cabecera del juego
            self.mostrarCabecera()
 
            # Muestra el tablero
            self.mostrarTablero()

            # Pide al usuario su movimiento
            self.introducirEscribirMovimiento()

            # Comprobar si el usuario ha ganado
            if self.comprobarVictoria(self.sign_user):
                self.limpiarTerminal() # Limpiar la pantalla
                self.mostrarTablero()
                print(estilos.color.verde + '\nEl ganador eres tú.' + estilos.color.RESET)
                break

            # Comprobar si el tablero está lleno
            if self.comprobarTableroLleno():
                break
            
            # Vuelve a mostrar el tablero
            self.mostrarTablero()

            # Hace el movimiento del robot
            self.escribirMovimientoMaquina()

            # Comprobar si la máquina ha ganado
            if self.comprobarVictoria(self.sign_maquina):
                print(estilos.color.rojo + '\nHas perdido. El ganador es la máquina.' + estilos.color.RESET)
                break

            # Comprobar si el tablero está lleno
            if self.comprobarTableroLleno():
                break

# Inicia el juego
if __name__ == "__main__":
    juego = JuegoTresEnRaya()
    juego.iniciarJuego()
