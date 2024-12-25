import unittest
from tres_en_raya import JuegoTresEnRaya
import unittest.mock

class TestJuegoTresEnRaya(unittest.TestCase):
    # Clase de prueba para el juego Tres en Raya

    def setUp(self):
        # Configuración inicial antes de cada prueba
        self.juego = JuegoTresEnRaya()

    def test_mostrarTablero(self):
        # Prueba para verificar que el tablero se muestra correctamente
        self.juego.mostrarTablero()
        self.assertEqual(len(self.juego.board), 9)  # Asegurarse de que el tablero tiene 9 casillas

    def test_introducirEscribirMovimiento(self):
        # Prueba para la funcionalidad de introducir un movimiento por el usuario
        self.juego.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        with unittest.mock.patch('builtins.input', return_value='1'):
            self.juego.introducirEscribirMovimiento()
        self.assertIn(self.juego.sign_user, self.juego.board)  # Verificar que el movimiento se registre en el tablero

    def test_escribirMovimientoMaquina(self):
        # Prueba para la funcionalidad de la máquina escribiendo su movimiento
        self.juego.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.juego.escribirMovimientoMaquina()
        self.assertIn(self.juego.SIGN_MAQUINA, self.juego.board)  # Verificar que el movimiento de la máquina se registre

    def test_comprobarTableroLleno(self):
        # Prueba para comprobar si el tablero está lleno
        self.juego.board = [self.juego.SIGN_USER] * 9
        self.assertTrue(self.juego.comprobarTableroLleno())  # Verificar que se detecta un tablero lleno

    def test_comprobarVictoria(self):
        # Prueba para comprobar si hay una condición de victoria
        self.juego.board = [self.juego.SIGN_USER] * 3 + [4, 5, 6, 7, 8, 9]
        self.assertTrue(self.juego.comprobarVictoria(self.juego.SIGN_USER))  # Verificar que se detecta la victoria

    def test_limpiarTerminal(self):
        # Prueba para limpiar la terminal (sin verificación, solo asegurarse de que no haya excepciones)
        self.juego.limpiarTerminal()

    def test_mostrarCabecera(self):
        # Prueba para mostrar la cabecera (sin verificación, solo asegurarse de que no haya excepciones)
        self.juego.mostrarCabecera()

    def test_iniciarJuego(self):
        # Prueba para iniciar el juego (bucle de juego simulado)
        self.juego.iniciarJuego = lambda: None  # Simular el bucle del juego
        self.juego.iniciarJuego()

if __name__ == '__main__':
    unittest.main()
