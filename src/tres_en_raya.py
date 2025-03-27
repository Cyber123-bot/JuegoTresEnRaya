import random
import estilos # Archivo
import os
import time

class JuegoTresEnRaya:

    # Constantes para los signos del usuario1, la máquina/usuario2 y las combinaciones ganadoras
    SIGN_USER1 = estilos.color.amarillo + 'O' + estilos.color.cian
    SIGN_MAQUINA = estilos.color.rojo + 'X' + estilos.color.cian
    COMBINACIONES_GANADORAS = (
            (0, 1, 2),  # Fila 1
            (3, 4, 5),  # Fila 2
            (6, 7, 8),  # Fila 3
            (0, 3, 6),  # Columna 1
            (1, 4, 7),  # Columna 2
            (2, 5, 8),  # Columna 3
            (0, 4, 8),  # Diagonal principal
            (2, 4, 6)   # Diagonal secundaria
    )

    def __init__(self):
        """Esta clase representa el juego de tres en raya."""
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.sign = (self.SIGN_USER1, self.SIGN_MAQUINA)
        self.__combinaciones_ganadoras = self.COMBINACIONES_GANADORAS
        self.velocidad = 0.03

    def _texto_animado(self, texto):
        ''' Función que recibe un texto y lo imprime letra por letra con retraso especificado por el usuario (predeterminado 0.03 segundos) '''
        # Recorrer carácter por caracter el texto/frase introducida
        for char in texto:
            print(char, end="", flush=True)
            time.sleep(self.velocidad) # Retraso

        print() # Añadir salto de línea

    def _comprobarTableroLleno(self):
        """La función examina el tablero y termina el juego si no hay cuadros vacíos."""
        # Si todos los cuadros están ocupados, el juego termina en empate
        if all(spot in [self.sign[1], self.sign[0]] for spot in self.board):
            self._texto_animado(estilos.color.naranja + '\nEmpate.' + estilos.color.RESET)
            return True
        
        # Si hay cuadros vacíos, el juego continúa
        else:
            return False

    def _comprobarVictoria(self, sign):
        """La función analiza el estado del tablero para verificar el ganador"""
        # Comprobar si hay una combinación ganadora
        for combinacion in self.__combinaciones_ganadoras:
            if all(self.board[i] == sign for i in combinacion):
                return True
            
        # Si no hay combinaciones ganadoras, el juego continúa
        return False
    
    def _limpiarTerminal(self):
        """Limpia la pantalla de la terminal"""
        os.system("cls" if os.name == "nt" else "clear") # Usar os.system para ejecutar un comando en la terminal
    
    def _mostrarCabecera(self):
        """Muestra el título del juego y más datos"""
        print(estilos.color.purpura + '\n\t\tTRES EN RAYA' + estilos.color.RESET) # Título del juego

    def _mostrarTablero(self):
        """Muestra el estado actual del tablero en la consola"""
        print(estilos.color.cian + '\t+-------+-------+-------+', 
              '\t|       |       |       |', 
              f'\t|   {self.board[0]}   |   {self.board[1]}   |   {self.board[2]}   |',
              '\t|       |       |       |', 
              '\t+-------+-------+-------+',
              '\t|       |       |       |',
              f'\t|   {self.board[3]}   |   {self.board[4]}   |   {self.board[5]}   |',
              '\t|       |       |       |',
              '\t+-------+-------+-------+',
              '\t|       |       |       |',
              f'\t|   {self.board[6]}   |   {self.board[7]}   |   {self.board[8]}   |',
              '\t|       |       |       |',
              '\t+-------+-------+-------+' + estilos.color.RESET, sep='\n')

    def _preguntar_nombre(self, n_usuario: int):
        """ Función que pregunta al usuario su nombre """

        try:
            print() # Salto de línea

            # Preguntar el nombre al usuario
            nombre = input(estilos.color.azul + f"¿Cual es tu nombre usuario {n_usuario}?: " + estilos.color.RESET)

            return nombre.capitalize() # Retornar nombre

        # Si el usuario presiona Ctrl + C, salimos
        except KeyboardInterrupt:
            self._texto_animado("\n¡Adiós!")
            exit() # Salir

    def _entradaUsuario(self, usuario: tuple):
        """La función pregunta al usuario acerca de su movimiento y actualiza el tablero"""
        while True:
            try:
                user_move = input(estilos.color.azul + f'\nIngresa tu movimiento, {estilos.color.cian + usuario[0] + estilos.color.azul} [1-9 | exit -> para salir]: ' + estilos.color.RESET)

            # Cuando el usuario pulse Ctrl + C salir del juego
            except KeyboardInterrupt:
                self._texto_animado(estilos.color.cian + '\n¡Adiós!' + estilos.color.RESET)
                exit() # Salir del juego

            # Comprobamos si el usuario quiere salir
            if user_move == 'exit':
                self._texto_animado(estilos.color.cian + '\n¡Adiós!' + estilos.color.RESET)
                exit() # Salir del juego

            try:
                user_move = int(user_move)

                if user_move < 1 or user_move > 9:
                    # Lanzar una excepción si el movimiento está fuera de rango
                    raise ValueError(estilos.color.rojo + "\nMovimiento fuera de rango." + estilos.color.RESET)
            
            except ValueError:
                # Capturar la excepción y mostrar un mensaje de error
                self._texto_animado(estilos.color.rojo + "\nMovimiento no válido. Debes ingresar un número entre 1 y 9." + estilos.color.RESET)
                continue
            
            # Comprobar si el cuadrado está ocupado
            if self.board[user_move - 1] in self.sign:
                self._texto_animado(estilos.color.naranja + '\nCuadrado ocupado. Intenta de nuevo.' + estilos.color.RESET)

            # Si el cuadrado está vacío, actualiza el tablero dependiendo del usuario
            else:
                if usuario[1] == 1:
                    self.board[user_move - 1] = self.sign[0]
                    break

                else:
                    self.board[user_move - 1] = self.sign[1]
                    break

    def _escribirMovimientoMaquina(self):
        """La máquina realiza su movimiento de manera estratégica."""
        for combinacion in self.COMBINACIONES_GANADORAS:
            # Verificar si la máquina puede ganar
            valores = [self.board[i] for i in combinacion]
            if valores.count(self.sign[1]) == 2 and valores.count(self.sign[0]) == 0:
                for i in combinacion:
                    if self.board[i] not in [self.sign[0], self.sign[1]]:
                        self.board[i] = self.sign[1]
                        return

        for combinacion in self.COMBINACIONES_GANADORAS:
            # Verificar si puede bloquear al usuario
            valores = [self.board[i] for i in combinacion]
            if valores.count(self.sign[0]) == 2 and valores.count(self.sign[1]) == 0:
                for i in combinacion:
                    if self.board[i] not in [self.sign[0], self.sign[1]]:
                        self.board[i] = self.sign[1]
                        return

        # Movimiento aleatorio si no puede ganar ni bloquear
        movimientos_disponibles = [i for i, spot in enumerate(self.board) if spot not in [self.sign[0], self.sign[1]]]
        if movimientos_disponibles:
            self.board[random.choice(movimientos_disponibles)] = self.sign[1]

    def iniciarJuego(self):
        """Inicia el juego y alterna los turnos entre el usuario y la máquina"""
        # Variables para los modos de juego
        modo_juego = {"1": "Usuario1 contra usuario2", "2": "Usuario contra máquina"}

        # Limpiar la terminal
        self._limpiarTerminal()

        # Imprimir cabecera del juego
        self._mostrarCabecera()

        # Imprimimos un salto de línea
        print()

        # Preguntamos al usuario que modo de juego desea
        self._texto_animado(estilos.color.cian + f"1. {modo_juego['1']}" + estilos.color.RESET)
        self._texto_animado(estilos.color.cian + f"2. {modo_juego['2']}" + estilos.color.RESET)
        try:
            modo = input(estilos.color.azul + f"\n¿Qué modo de juego deseas [1 | 2]?: " + estilos.color.RESET).replace(" ", "")

        # Capturamos el KeyboardInterrupt
        except KeyboardInterrupt:
            self._texto_animado(estilos.color.cian + '\n¡Adiós!' + estilos.color.RESET)
            exit() # Sale del juego
            
        # Comprobamos la validez de la respuesta
        if modo not in modo_juego.keys():
            self._texto_animado(estilos.color.rojo + f"Respuesta inválida. Solo se puede responder: {modo_juego['1']} o {modo_juego['2']}" + estilos.color.RESET)

        # Si la respuesta es válida iniciamos el modo de juego que el ha dicho
        else:
            if modo == "1":
                # Pedimos los nombres
                nombre_usuario_1 = self._preguntar_nombre("1")
                nombre_usuario_2 = self._preguntar_nombre("2")

                # Comprobamos si los nombres son válidos son validos
                if nombre_usuario_1 == nombre_usuario_2:
                    print(estilos.color.rojo + "Error: los dos nombres son iguales.")
                    exit() # Salir

                elif nombre_usuario_1.replace(" ", "") == "" or nombre_usuario_2.replace(" ", "") == 0:
                    print(estilos.color.rojo + "El nombre no es válido." + estilos.color.RESET)
                    exit() # Salir

                while True:
                    # Limpiar la pantalla
                    self._limpiarTerminal()

                    # Mostrar la cabecera del juego
                    self._mostrarCabecera()

                    # Muestra el tablero
                    self._mostrarTablero()

                    # Pide al usuario 1 su movimiento
                    self._entradaUsuario((nombre_usuario_1, 1))

                    # Comprobar si el usuario 1 ha ganado
                    if self._comprobarVictoria(self.sign[0]):
                        self._limpiarTerminal() # Limpiar la pantalla
                        self._mostrarCabecera() # Mostrar la cabecera
                        self._mostrarTablero() # Mostrar el tablero
                        self._texto_animado(estilos.color.verde + f'\nEl ganador es {nombre_usuario_1}.' + estilos.color.RESET)
                        break

                    # Comprobar si el tablero está lleno
                    if self._comprobarTableroLleno():
                        break
            
                    # Limpiar la terminal
                    self._limpiarTerminal()

                    # Imprimir cabecera del juego
                    self._mostrarCabecera()

                    # Mostrar el tablero
                    self._mostrarTablero()

                    # Pide al usuario 2 su movimiento
                    self._entradaUsuario((nombre_usuario_2, 2))

                    # Comprobar si el usuario 2 ha ganado
                    if self._comprobarVictoria(self.sign[1]):
                        self._limpiarTerminal() # Limpiar la pantalla
                        self._mostrarCabecera() # Mostrar la cabecera
                        self._mostrarTablero() # Mostrar el tablero
                        self._texto_animado(estilos.color.verde + f'\nEl ganador es {nombre_usuario_2}.' + estilos.color.RESET)
                        break

                    # Comprobar si el tablero está lleno
                    if self._comprobarTableroLleno():
                        break

            else:
                nombre_usuario_1 = self._preguntar_nombre(1)

                while True:
                    # Limpiar la pantalla
                    self._limpiarTerminal()

                    # Mostrar la cabecera del juego
                    self._mostrarCabecera()

                    # Muestra el tablero
                    self._mostrarTablero()

                    # Pide al usuario su movimiento
                    self._entradaUsuario((nombre_usuario_1, 1))

                    # Comprobar si el usuario ha ganado
                    if self._comprobarVictoria(self.sign[0]):
                        self._limpiarTerminal() # Limpiar la pantalla
                        self._mostrarCabecera() # Mostrar la cabecera
                        self._mostrarTablero() # Mostrar el tablero
                        self._texto_animado(estilos.color.verde + f"\nEl ganador eres tú, felicidades {nombre_usuario_1}." + estilos.color.RESET)
                        break

                    # Comprobar si el tablero está lleno
                    if self._comprobarTableroLleno():
                        break
            
                    # Limpiar la terminal
                    self._limpiarTerminal()

                    # Imprimir cabecera del juego
                    self._mostrarCabecera()

                    # Hace el movimiento del robot
                    self._escribirMovimientoMaquina()

                    # Comprobar si la máquina ha ganado
                    if self._comprobarVictoria(self.sign[1]):
                        self._limpiarTerminal() # Limpiar la pantalla
                        self._mostrarCabecera() # Mostrar la cabecera
                        self._mostrarTablero() # Mostrar el tablero
                        self._texto_animado(estilos.color.rojo + f'\nHas perdido {nombre_usuario_1}. El ganador es la máquina.' + estilos.color.RESET)
                        break

                    # Comprobar si el tablero está lleno
                    if self._comprobarTableroLleno():
                        break

        try:
            # Pregunta al usuario si quiere reiniciar el juego
            resp = input(estilos.color.azul + "\n¿Quieres volver a jugar [s | n]?: " + estilos.color.RESET).lower()

        # Capturamos una interrupción de teclado
        except KeyboardInterrupt:
            self._texto_animado(estilos.color.cian + "\n¡Adios!" + estilos.color.RESET)
            exit()

        # Esperamos 0.5 segundos
        time.sleep(0.5)

        # En caso de que quiera reiniciar el juego lo reiniciamos
        if resp == "s":
            self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Ponemos el tablero en su posición original
            self.iniciarJuego() # Volvemos a iniciar el juego

        # En caso de que no quiera reiniciar el juego salimos
        elif resp == "n":
            self._texto_animado(estilos.color.cian + "\n¡Adios!" + estilos.color.RESET)
            exit()

        # Si la respuesta es inválida lanzamos un mensaje de error y salimos
        else:
            self._texto_animado(estilos.color.rojo + "\nLa respuesta no es válida. Solo se puede responder 's' o 'n'." + estilos.color.RESET)


# Iniciar el juego
if __name__ == "__main__":
    juego = JuegoTresEnRaya()
    juego.iniciarJuego()
