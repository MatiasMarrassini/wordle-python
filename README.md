# Wordle en Python

Implementación en consola del clásico juego Wordle, desarrollada en Python como proyecto para la materia de Programación (UADE).

Soporta login de usuarios, partidas para 1 o 2 jugadores, palabras de 5, 6 o 7 letras, ranking de puntajes y estadísticas persistentes por usuario.

## Características

- **Sistema de usuarios**: registro y login con validación de usuario/contraseña, guardado en JSON.
- **Multijugador local**: podés jugar solo o loguear un segundo usuario en la misma partida.
- **Dificultad configurable**: palabras de 5, 6 o 7 letras.
- **Feedback por colores**: letras en verde (posición correcta), amarillo (letra correcta, posición incorrecta) y gris (letra no está en la palabra), usando códigos ANSI en la terminal.
- **Ranking y estadísticas**: puntaje acumulado, partidas jugadas y veces que jugó primero, con persistencia entre partidas.
- **Normalización de tildes**: los intentos con o sin acentos se comparan correctamente contra la palabra a adivinar.
- **Tests unitarios** para la lógica del juego y de la interfaz (carpeta `testing/`).

## Cómo jugar

Requisitos: Python 3.10 o superior (no usa librerías externas).

```bash
git clone https://github.com/MatiasMarrassini/wordle-python.git
cd wordle-python
python main.py
```

Al iniciar vas a ver el menú principal, donde podés loguearte, elegir la dificultad y empezar a jugar. En cada intento, escribí una palabra de la longitud correspondiente y vas a ver el resultado coloreado letra por letra.

> **Nota:** el proyecto incluye dos usuarios de ejemplo (`ejemplo` / `Ejemplo123` e `invitado` / `Invitado123`) para probar el ranking y las estadísticas sin tener que registrarte primero.

## Estructura del proyecto

```
main.py                  # Punto de entrada, loop principal del juego
autenticacion/           # Registro y login de usuarios
datos/                   # Persistencia (usuarios, configuración, listas de palabras)
juego/                   # Lógica central del juego (selección de palabra, orden de turnos)
UI/                      # Menús, render de intentos, ranking y alineación de texto
utils/                   # Utilidades compartidas (colores ANSI)
testing/                 # Tests unitarios
```

## Tecnologías

Python puro (sin dependencias externas): módulos `json`, `re`, `random`, `time`, `math`, `functools`, `unittest`.

## Posibles mejoras a futuro

- Corregir la superposición visual de intentos en algunos anchos de terminal.
- Unificar el sistema de dificultades (actualmente conviven varias formas de definirla).
- Sumar más validación de bordes en el manejo de sesión sin login previo.
