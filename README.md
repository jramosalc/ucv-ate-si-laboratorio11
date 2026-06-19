# alpha-beta-lab
# Laboratorio: Inteligencia Artificial Adversarial - Poda Alfa-Beta

Este proyecto implementa y compara los algoritmos de búsqueda adversarial **Minimax Clásico** y **Poda Alfa-Beta** sobre diferentes estructuras de árboles de juego (`GameTree`). El objetivo es evaluar empíricamente la eficiencia en términos de nodos evaluados y ramas podadas bajo distintas condiciones de ordenamiento.

---

## 🚀 Arquitectura del Proyecto

* **`src/game_tree.py`**: Define el tipo de dato recursivo `GameTree` y provee los árboles de prueba (`sample_tree`, `medium_tree`, `ordered_tree_for_pruning`).
* **`src/minimax.py`**: Implementación recursiva del algoritmo Minimax clásico que calcula la decisión óptima explorando todo el árbol.
* **`src/alpha_beta.py`**: Implementación optimizada de la Poda Alfa-Beta utilizando límites dinámicos para descartar subárboles innecesarios.
* **`src/main.py`**: Script de orquestación principal que ejecuta y compara ambos algoritmos en la consola.
* **`tests/test_algorithms.py`**: Suite de pruebas unitarias automatizadas con `pytest` para garantizar la estabilidad del motor matemático.

---

## 🛠️ Ejecución y Pruebas Locales

### 1. Ejecutar la Comparación de Algoritmos
Para visualizar el rendimiento en consola, ejecuta el script principal:
```bash
python -m src.main

## 🎮 Reto: Tres en Raya (Tic-Tac-Toe) Adversarial
Se implementó una versión interactiva por consola del juego Tres en Raya en el archivo `src/challenge.py`. 

### Características de la Implementación:
* **Generación Dinámica del Árbol:** A diferencia de los experimentos estáticos, aquí el árbol de estados del juego se computa en tiempo real según los movimientos del jugador.
* **Refactorización de Mantenibilidad:** La lógica del algoritmo se dividió en subfunciones especializadas (`_maximize` y `_minimize`) para reducir la complejidad cognitiva por debajo de los límites exigidos por **SonarLint**, garantizando un código limpio de alta cohesión.
* **Imbatibilidad:** Gracias a la precisión matemática de la Poda Alfa-Beta, el agente inteligente es capaz de bloquear cualquier intento de victoria del usuario humano, asegurando como mínimo un empate en condiciones de juego perfecto.

Para ejecutar el reto:
```bash
python -m src.challenge