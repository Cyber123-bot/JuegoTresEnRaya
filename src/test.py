import unittest
from tres_en_raya import JuegoTresEnRaya
import unittest.mock

class TestJuegoTresEnRaya(unittest.TestCase):
    """Clase de prueba para el juego Tres en Raya"""

    def setUp(self):
        """Configuración inicial antes de cada prueba"""
        self.juego = JuegoTresEnRaya()

    def test_mostrarTablero(self):
        """Prueba para verificar que el tablero se muestra correctamente"""
        with unittest.mock.patch('builtins.print'):
            self.juego._mostrarTablero()
        self.assertEqual(len(self.juego.board), 9)  # Asegurarse de que el tablero tiene 9 casillas

    def test_entradaUsuario(self):
        """Prueba para la funcionalidad de introducir un movimiento por el usuario"""
        with unittest.mock.patch('builtins.input', return_value='1'):
            self.juego._entradaUsuario(("test", 1))
        self.assertIn(self.juego.sign[0], self.juego.board)  # Verificar que el movimiento se registre en el tablero

    def test_escribirMovimientoMaquina(self):
        """Prueba para la funcionalidad de la máquina escribiendo su movimiento"""
        self.juego.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.juego._escribirMovimientoMaquina()
        self.assertIn(self.juego.sign[1], self.juego.board)  # Verificar que el movimiento de la máquina se registre

    def test_comprobarTableroLleno(self):
        self.juego.board = [self.juego.sign[0]] * 9
        self.assertTrue(self.juego._comprobarTableroLleno())  # Verificar que se detecta un tablero lleno

    def test_comprobarVictoria(self):
        self.juego.board = [self.juego.sign[0]] * 3 + [4, 5, 6, 7, 8, 9]
        self.assertTrue(self.juego._comprobarVictoria(self.juego.sign[0]))  # Verificar que se detecta la victoria

    def test_limpiarTerminal(self):
        """Prueba para limpiar la terminal (sin verificación, solo asegurarse de que no haya excepciones)"""
        self.juego._limpiarTerminal()

    def test_mostrarCabecera(self):
        """Prueba para mostrar la cabecera (sin verificación, solo asegurarse de que no haya excepciones)"""
        with unittest.mock.patch('builtins.print'):
            self.juego._mostrarCabecera()

    def test_iniciarJuego(self):
        """Prueba para iniciar el juego (bucle de juego simulado)"""
        with unittest.mock.patch('builtins.input', side_effect=['2', '1', 'exit']):
            with self.assertRaises(SystemExit):  # Captura la excepción SystemExit
                self.juego.iniciarJuego()


if __name__ == '__main__':
    unittest.main()
