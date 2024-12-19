# Sistema de Biblioteca Virtual

## Introducción
El Sistema de Biblioteca Virtual permite gestionar libros disponibles y prestados, facilitando el control de préstamos y devoluciones mediante una implementación en Python.

## Requisitos Previos
- Python 3.7 o superior.
- Editor de texto o IDE (recomendado: Visual Studio Code).

## Funcionalidades
### Métodos principales:
- **`agregar_libro(id, titulo, autor)`**: Agrega un libro a la lista de libros disponibles.
- **`prestar_libro(id, usuario)`**: Mueve un libro a la lista de prestados, asociándolo con un usuario.
- **`devolver_libro(id)`**: Regresa un libro a la lista de disponibles.
- **`buscar_libro_por_titulo(titulo)`**: Devuelve información del libro si existe.
- **`mostrar_libros_disponibles()`**: Muestra los libros disponibles.
- **`mostrar_libros_prestados()`**: Muestra los libros prestados con el usuario correspondiente.

## Ejecución
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/richardmijo/ed_semana_8.git
   cd ed_semana_8/tu_usuario
 
