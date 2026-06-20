# 🤖 Laboratorio 11: Agente Inteligente con Algoritmos de Búsqueda Adversaria (Minimax y Poda Alfa-Beta)

Este proyecto implementa y evalúa un agente inteligente basado en los algoritmos **Minimax** y **Poda Alfa-Beta** para la toma de decisiones óptimas en entornos adversarios. Desarrollado como parte del curso de Sistemas Inteligentes en la Universidad César Vallejo (UCV - Sede Ate).

---

## 🛠️ Estructura del Proyecto

El proyecto está organizado bajo estándares de desarrollo limpio, incluyendo pruebas unitarias automatizadas y análisis de cobertura de código:

```text
mi-proyecto-alpha-beta/
├── .github/workflows/   # Configuración de Integración Continua (GitHub Actions)
│   └── ci.yml
├── src/                 # Código fuente del agente inteligente
│   ├── alpha_beta.py    # Implementación del algoritmo con Poda Alfa-Beta
│   ├── minimax.py       # Implementación del algoritmo Minimax clásico
│   ├── game_tree.py     # Estructura y generación del árbol de juego
│   └── main.py          # Punto de entrada y simulación
├── tests/               # Pruebas unitarias
│   └── test_algorithms.py
├── .gitignore           # Archivos excluidos del control de versiones
├── requirements.txt     # Dependencias del proyecto (pytest, pytest-cov)
└── sonar-project.properties # Configuración de análisis de calidad (SonarCloud)
