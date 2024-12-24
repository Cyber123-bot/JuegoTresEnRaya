import unittest

class JuegoTresEnRaya:
    def __init__(self):
        self.tablero = [str(i) for i in range(1, 10)]  # Inicia el tablero con números del 1 al 9
        self.sign_user = "X"
        self.sign_maquina = "O"
        
    def introducirEscribirMovimiento(self, movimiento, jugador):
        if self.tablero[movimiento - 1] not in [self.sign_user, self.sign_maquina]:
            self.tablero[movimiento - 1] = jugador
            return True
        return False

    def comprobarVictoria(self, jugador):
        combinaciones_ganadoras = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # filas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columnas
            [0, 4, 8], [2, 4, 6]              # diagonales
        ]
        for combinacion in combinaciones_ganadoras:
            if all(self.tablero[i] == jugador for i in combinacion):
                return True
        return False

    def comprobarTableroLleno(self):
        return all(c == self.sign_user or c == self.sign_maquina for c in self.tablero)


class TestJuegoTresEnRaya(unittest.TestCase):

    def setUp(self):
        self.juego = JuegoTresEnRaya()

    def test_iniciar_tablero(self):
        self.assertEqual(self.juego.tablero, [str(i) for i in range(1, 10)])  # Compara con el tablero inicial

    def test_movimiento_valido(self):
        # Verifica que un movimiento válido se realiza correctamente
        self.assertTrue(self.juego.introducirEscribirMovimiento(1, self.juego.sign_user))
        self.assertEqual(self.juego.tablero[0], self.juego.sign_user)

    def test_movimiento_invalido(self):
        # Verifica que un movimiento inválido no se permite
        self.juego.introducirEscribirMovimiento(1, self.juego.sign_user)
        self.assertFalse(self.juego.introducirEscribirMovimiento(1, self.juego.sign_maquina))

    def test_comprobar_tablero_lleno(self):
        # Verifica que el método reconocerá correctamente cuando el tablero está lleno
        self.juego.tablero = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
        self.assertTrue(self.juego.comprobarTableroLleno())

    def test_comprobar_victoria_usuario(self):
        # Verifica que el usuario gana con una combinación ganadora
        self.juego.tablero = ['X', 'X', 'X', '4', '5', '6', '7', '8', '9']
        self.assertTrue(self.juego.comprobarVictoria(self.juego.sign_user))

    def test_comprobar_victoria_maquina(self):
        # Verifica que la máquina gana con una combinación ganadora
        self.juego.tablero = ['O', 'O', 'O', '4', '5', '6', '7', '8', '9']
        self.assertTrue(self.juego.comprobarVictoria(self.juego.sign_maquina))

    def test_comprobar_victoria_diagonal(self):
        # Verifica que se detecta una victoria en diagonal
        self.juego.tablero = ['X', '2', 'O', '4', 'X', '6', 'O', '8', 'X']
        self.assertTrue(self.juego.comprobarVictoria(self.juego.sign_user))


if __name__ == '__main__':
    unittest.main()
