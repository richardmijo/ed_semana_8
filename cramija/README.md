# Sistema de Biblioteca Virtual

## Introducción
Este programa implementa un sistema de Biblioteca Virtual para gestionar libros disponibles y prestados.

## Requisitos Previos
- Python 3.x instalado.
- Editor de texto (VS Code, PyCharm, etc.).

## Funciones
- `agregar_libro(id, titulo, autor)`: Agrega un libro nuevo.
- `prestar_libro(id, usuario)`: Asocia un libro a un usuario y lo mueve a la lista de prestados.
- `devolver_libro(id)`: Devuelve un libro prestado.
- `buscar_libro_por_titulo(titulo)`: Busca un libro por su título.
- `mostrar_libros_disponibles()`: Muestra todos los libros disponibles.
- `mostrar_libros_prestados()`: Muestra todos los libros prestados.

## Ejecución
1. Ejecutar el programa:
   ```bash
   python biblioteca.py