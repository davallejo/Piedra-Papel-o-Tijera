# ✂️ Rock Paper Scissors — AI Player

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![FreeCodeCamp](https://img.shields.io/badge/FreeCodeCamp-0A0A23?logo=freecodecamp&logoColor=white)
![AI Strategy](https://img.shields.io/badge/Strategy-Adaptive%20AI-FF6B6B?logo=openai&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

> 🤖 **Jugador inteligente de Piedra, Papel o Tijera** que analiza el historial de jugadas del oponente y adapta su estrategia dinámicamente para ganar al menos el **60% de los juegos** contra cualquier bot.

---

## 📸 Vista General

Este proyecto forma parte del programa **Scientific Computing with Python** de [freeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/rock-paper-scissors) y demuestra el uso de **estrategias adaptativas basadas en historial** para superar a múltiples bots con distintos patrones de juego.

---

## 🧠 ¿Cómo funciona la estrategia?

El jugador implementado no juega al azar. Analiza las jugadas previas del oponente para **predecir y contraatacar**:

| Situación | Estrategia | Resultado |
|-----------|------------|-----------|
| 🎲 Primera jugada | Elección aleatoria | Inicio neutral |
| ✊ Oponente jugó `R` | Devuelve `P` (Papel cubre Piedra) | ✅ Victoria |
| 📄 Oponente jugó `P` | Devuelve `S` (Tijera corta Papel) | ✅ Victoria |
| ✂️ Oponente jugó `S` | Devuelve `R` (Piedra aplasta Tijera) | ✅ Victoria |

> La función `player` mantiene un **historial acumulado** del oponente usando un parámetro mutable por defecto, lo que le permite adaptar su estrategia a lo largo de toda la partida.

---

## 🤖 Bots Rivales

El jugador debe superar (60%+) a los siguientes bots:

| Bot | Comportamiento |
|-----|---------------|
| 🎲 **Quincy** | Jugadas completamente aleatorias |
| ✊ **Johnny** | Siempre juega `R` (Piedra) |
| 📄 **Jake** | Siempre juega `P` (Papel) |
| ✂️ **Jane** | Siempre juega `S` (Tijera) |

---

## 🛠️ Tecnologías y Herramientas

| Tecnología | Uso |
|------------|-----|
| 🐍 **Python 3.8+** | Lenguaje principal |
| 🎲 **random** | Módulo estándar para jugadas iniciales |
| 🧪 **Unittest** | Pruebas unitarias automatizadas |

---

## 📁 Estructura del Proyecto

```
rock-paper-scissors/
│
├── 🐍 RPS.py           # Módulo principal con la función player() (estrategia)
├── 🎮 RPS_game.py      # Motor del juego y definición de los 4 bots
├── 🐍 main.py          # Punto de entrada y ejecución de pruebas
├── 🧪 test_module.py   # Pruebas unitarias con unittest
└── 📘 README.md        # Documentación del proyecto
```

> ⚠️ **Nota:** El archivo `RPS_game.py` **no debe modificarse**. Contiene el motor del juego y los bots oponentes.

---

## ⚙️ Instalación y Uso

### 1️⃣ Clona el repositorio

```bash
git clone https://github.com/davallejo/rock-paper-scissors.git
cd rock-paper-scissors
```

### 2️⃣ Ejecuta el juego

```bash
python main.py
```

### 3️⃣ Prueba contra un bot específico

Descomenta la línea en `main.py` para probar con verbose:

```python
from RPS import player
from RPS_game import play, quincy, johnny, jake, jane

# Probar contra quincy en 1000 juegos con detalle
play(player, quincy, 1000, verbose=True)
```

### 4️⃣ Resultado esperado

```
Player 1 wins: 623
Player 2 wins: 201
Ties: 176
```

> 🏆 **Objetivo cumplido:** >60% victorias contra todos los bots.

---

## 🔬 Implementación del Jugador

```python
import random

def player(prev_play, opponent_history=[]):
    # Registra la última jugada del oponente
    if prev_play:
        opponent_history.append(prev_play)

    # Sin historial: jugada aleatoria
    if not opponent_history:
        return random.choice(["R", "P", "S"])

    # Contraataca la última jugada del oponente
    last_move = opponent_history[-1]
    if last_move == "R": return "P"   # Papel cubre Piedra
    if last_move == "P": return "S"   # Tijera corta Papel
    if last_move == "S": return "R"   # Piedra aplasta Tijera
```

---

## 🧪 Pruebas Unitarias

```bash
python -m unittest test_module.py -v
```

```
test_initial_play ................ OK  🎲 Primera jugada válida
test_react_to_previous_move ...... OK  ⚔️  Contraataca correctamente

----------------------------------------------------------------------
Ran 2 tests in 0.XXXs

OK ✅
```

---

## 💡 Habilidades Demostradas

✅ Diseño de **estrategias adaptativas** basadas en historial  
✅ Uso de **parámetros mutables por defecto** en Python para estado persistente  
✅ Comprensión de **lógica de juego** y análisis de patrones  
✅ Escritura de **pruebas unitarias** con `unittest`  
✅ Estructuración modular del código (`game engine` vs `player strategy`)  

---

## 🗺️ Roadmap

- [x] ✅ Función `player()` con estrategia de contraataque reactivo
- [x] ✅ Superación del 60% de victorias contra los 4 bots
- [x] ✅ Pruebas unitarias automatizadas
- [ ] 🧠 Implementar análisis de **frecuencia de jugadas** para detectar patrones más complejos
- [ ] 📊 Agregar **estadísticas visuales** de partidas con Matplotlib
- [ ] 🌐 Crear interfaz jugable en el navegador con **Streamlit** o **Flask**
- [ ] 🤖 Explorar estrategia con **Markov Chains** para predicción avanzada

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

## 👤 Autor

**Diego Vallejo**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Diego%20Vallejo-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ing-diego-vallejo)
[![GitHub](https://img.shields.io/badge/GitHub-davallejo-181717?logo=github&logoColor=white)](https://github.com/davallejo)
[![Portfolio](https://img.shields.io/badge/Portfolio-davallejo.github.io-4A90D9?logo=githubpages&logoColor=white)](https://davallejo.github.io/)
