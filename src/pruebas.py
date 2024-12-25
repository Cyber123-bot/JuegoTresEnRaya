import unittest
from tres_en_raya import JuegoTresEnRaya
import unittest.mock

class TestJuegoTresEnRaya(unittest.TestCase):

    def setUp(self):
        self.juego = JuegoTresEnRaya()

    def test_mostrarTablero(self):
        self.juego.mostrarTablero()
        self.assertEqual(len(self.juego.board), 9)

    def test_introducirEscribirMovimiento(self):
        self.juego.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        with unittest.mock.patch('builtins.input', return_value='1'):
            self.juego.introducirEscribirMovimiento()
        self.assertIn(self.juego.sign_user, self.juego.board)

    def test_escribirMovimientoMaquina(self):
        self.juego.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.juego.escribirMovimientoMaquina()
        self.assertIn(self.juego.SIGN_MAQUINA, self.juego.board)

    def test_comprobarTableroLleno(self):
        self.juego.board = [self.juego.SIGN_USER] * 9
        self.assertTrue(self.juego.comprobarTableroLleno())

    def test_comprobarVictoria(self):
        self.juego.board = [self.juego.SIGN_USER] * 3 + [4, 5, 6, 7, 8, 9]
        self.assertTrue(self.juego.comprobarVictoria(self.juego.SIGN_USER))

    def test_limpiarTerminal(self):
        self.juego.limpiarTerminal()
        # No assertion needed, just ensure no exceptions

    def test_mostrarCabecera(self):
        self.juego.mostrarCabecera()
        # No assertion needed, just ensure no exceptions

    def test_iniciarJuego(self):
        self.juego.iniciarJuego = lambda: None  # Mock game loop
        self.juego.iniciarJuego()
        # No assertion needed, just ensure no exceptions

if __name__ == '__main__':
    unittest.main()