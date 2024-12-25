# Juego Tres en Raya

Este es un juego de Tres en Raya (Tic-Tac-Toe) implementado en Python. El juego permite a un usuario jugar contra la máquina.

## Requisitos

- `Python 3.x`
- Módulo `estilos` (debe estar en el mismo directorio que `calculadora.py`)
- Módulo `os`

## Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/Cyber123-bot/JuegoTresEnRaya.git
   ```
2. Asegúrate de tener Python 3.x instalado.

## Cómo jugar

1. Ejecuta el archivo `pruebas.py`:
    ```bash
    python tres_en_raya.py
    ```
2. Sigue las instrucciones en la consola para realizar tu movimiento. Ingresa un número del 1 al 9 para colocar tu signo en el tablero.
3. El juego alternará entre tu movimiento y el de la máquina hasta que haya un ganador o el tablero esté lleno.

## Estructura del código

- `JuegoTresEnRaya`: Clase principal que maneja la lógica del juego.
  - `__init__()`: declara las variables de __board, sign_user y sign_máquina.
  - `mostrarTablero()`: Muestra el estado actual del tablero.
  - `introducirEscribirMovimiento()`: Pide al usuario su movimiento y actualiza el tablero.
  - `escribirMovimientoMaquina()`: Realiza el movimiento de la máquina.
  - `comprobarTableroLleno()`: Verifica si el tablero está lleno.
  - `comprobarVictoria(sign)`: Verifica si hay un ganador.
  - `limpiarTerminal()`: Limpia la pantalla de la terminal.
  - `mostrarCabecera()`: Muestra el título del juego.
  - `iniciarJuego()`: Inicia el juego y alterna los turnos entre el usuario y la máquina.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún problema o tienes alguna mejora, por favor abre un issue o envía un pull request. Más información en `docs/CONTRIBUTING.md`

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.