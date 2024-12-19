# Sistema de Biblioteca Virtual

## Introducción
El "Sistema de Biblioteca Virtual" es una aplicación desarrollada en Python que permite gestionar una biblioteca. Proporciona funcionalidades para agregar libros, prestar libros a usuarios y devolverlos, además de buscar libros por su título y mostrar listados de libros disponibles y prestados. Este sistema está diseñado para simplificar la administración de libros en una biblioteca, manteniendo un registro dinámico y organizado.

## Requisitos Previos
Antes de ejecutar el programa, asegúrese de tener instalado:

- Python 3.7 o superior.
- Un editor de texto o IDE para Python (opcional, pero recomendado).

### Instrucciones para ejecutar el programa:
1. Clone el repositorio del proyecto desde GitHub.
   ```bash
   git clone https://github.com/richardmijo/ed_semana_8.git
   ```
2. Cambie al branch correspondiente a su nombre de usuario:
   ```bash
   git checkout <frguamango>
   ```
3. Navegue hasta el directorio con su nombre de usuario:
   ```bash
   cd <frguamango>
   ```
4. Ejecute el archivo Python:
   ```bash
   python biblioteca_virtual.py
   ```

## Documentación de Funciones

### `agregar_libro(id, titulo, autor)`
Agrega un libro a la lista de libros disponibles.

- **Parámetros:**
  - `id` (int): Identificador único del libro.
  - `titulo` (str): Nombre del libro.
  - `autor` (str): Nombre del autor del libro.

### `prestar_libro(id, usuario)`
Presta un libro a un usuario.

- **Parámetros:**
  - `id` (int): Identificador del libro a prestar.
  - `usuario` (str): Nombre del usuario que solicita el libro.

### `devolver_libro(id)`
Devuelve un libro prestado a la lista de libros disponibles.

- **Parámetros:**
  - `id` (int): Identificador del libro a devolver.

### `buscar_libro_por_titulo(titulo)`
Busca un libro por su título y devuelve su información si se encuentra.

- **Parámetros:**
  - `titulo` (str): Nombre del libro a buscar.

### `mostrar_libros_disponibles()`
Muestra una lista de todos los libros disponibles.

### `mostrar_libros_prestados()`
Muestra una lista de todos los libros prestados, incluyendo información del usuario que los tiene.

## Formato
El archivo está estructurado utilizando listas y diccionarios en Python. Todos los métodos cuentan con docstrings para documentar sus funcionalidades.
