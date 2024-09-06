# Proyecto 1: Piedra Papel o Tijera

Este proyecto tiene como objetivo desarrollar un programa que juegue al clásico juego de **Piedra, Papel o Tijera**. La tarea principal es implementar una función `player` que, basándose en la última jugada del oponente, devuelva la próxima jugada del jugador para maximizar las probabilidades de ganar.

## Requisitos del Proyecto

1. **Función `player`:** 
   - **Entrada:** Una cadena que representa la última jugada del oponente ("R" para Piedra, "P" para Papel, o "S" para Tijera). Para el primer juego de una partida, se recibirá una cadena vacía.
   - **Salida:** Una cadena que representa la próxima jugada del jugador ("R", "P", o "S").

2. **Objetivo:** 
   - Jugar contra cuatro bots diferentes, ganando al menos el 60% de los juegos en cada partida.

3. **Estrategia:** 
   - Implementar múltiples estrategias que se adapten en función de las jugadas del oponente para superar a todos los bots.

## Instrucciones de Desarrollo

- **Archivo `RPS.py`:** Este archivo debe ser modificado para implementar la lógica del juego. La función `player` debe ser actualizada según las estrategias desarrolladas.
- **Archivo `RPS_game.py`:** No se debe modificar este archivo, ya que contiene el código del juego y los bots.
- **Archivo `main.py`:** Este archivo puede ser utilizado para probar el código. Importa la función de juego y los bots desde `RPS_game.py` y emplea la función `play` para realizar las pruebas.

## Pruebas

Las pruebas unitarias están disponibles en el archivo `test_module.py`, el cual se ha importado en `main.py` para facilitar la ejecución. Las pruebas se pueden ejecutar automáticamente descomentando la última línea en `main.py`.

## Ejemplo de Uso

Para probar la función `player` contra el bot `quincy` en 1000 juegos y visualizar los resultados de cada juego, se puede utilizar el siguiente comando en `main.py`:

```python
play(player, quincy, 1000, verbose=True)


## Autor

Diego Vallejo
