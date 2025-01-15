# Juego Tres en Raya

Este es un juego de Tres en Raya (Tic-Tac-Toe) implementado en Python. El juego permite a un usuario jugar contra la máquina o contra otro usuario.

## Requisitos

- `Python 3.x`
- Módulo `estilos` (debe estar en el mismo directorio que `tres_en_raya.py`)
- Módulo `os`

## Testeo
Para asegurarte de que todo funciona correctamente puedes ejecutar el archivo `src/test.py`

## Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/Cyber123-bot/JuegoTresEnRaya.git
   ```
2. Asegúrate de tener Python 3.x instalado.

## Cómo jugar

1. Ejecuta el archivo `tres_en_raya.py`:
    ```bash
    python tres_en_raya.py
    ```
2. Elige el modo de juego
2. Sigue las instrucciones en la consola para realizar tu movimiento. 

## Estructura del código

- `JuegoTresEnRaya`: Clase principal que maneja la lógica del juego.
  - `__init__()`: declara la variable board, y la lista de sign.
  - `_mostrarTablero()`: Muestra el estado actual del tablero.
  - `_entradaUsuario()`: Pide al usuario su movimiento y actualiza el tablero.
  - `_escribirMovimientoMaquina()`: Realiza el movimiento de la máquina.
  - `_comprobarTableroLleno()`: Verifica si el tablero está lleno.
  - `_comprobarVictoria()`: Verifica si hay un ganador.
  - `_limpiarTerminal()`: Limpia la pantalla de la terminal.
  - `_mostrarCabecera()`: Muestra el título del juego.
  - `iniciarJuego()`: Inicia el juego y alterna los turnos entre el usuario y la máquina.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún problema o tienes alguna mejora, por favor abre un issue o envía un pull request. Más información en `docs/CONTRIBUTING.md`

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.