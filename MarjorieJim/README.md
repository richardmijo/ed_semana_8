# Sistema de Biblioteca Virtual

## Introduccion
El Sistema de Biblioteca Virtual es un programa en Python diseñado para gestionar libros, permitiendo a los usuarios añadir, prestar, devolver y buscar libros de manera eficiente.

## Requisitos Previos
- Python 3 instalado en tu sistema.
- Clonar este repositorio:  
  ```bash
  git clone https://github.com/richardmijo/ed_semana_8.git

## Explicacion del codigo:
- Listas: libros_disponibles y libros_prestados son las listas que almacenan los libros, representados como diccionarios.
Funciones:
- agregar_libro: Agrega un nuevo libro a la lista de disponibles.
- prestar_libro: Mueve un libro de los disponibles a los prestados, asociando el usuario.
- devolver_libro: Mueve un libro de los prestados a los disponibles.
- buscar_libro_por_titulo: Busca un libro por título y devuelve su información.
- mostrar_libros_disponibles: Imprime todos los libros disponibles.
- mostrar_libros_prestados: Imprime todos los libros prestados con el usuario asociado.
- Menú interactivo: Permite al usuario interactuar con el sistema y ejecutar las acciones deseadas.

## Funciones Implementadas
- agregar_libro(id, titulo, autor): Agrega un libro a la lista de libros disponibles.
- prestar_libro(id, usuario): Presta un libro disponible a un usuario.
- devolver_libro(id): Devuelve un libro prestado.
- buscar_libro_por_titulo(titulo): Busca un libro por título.
- mostrar_libros_disponibles(): Lista los libros disponibles.
- mostrar_libros_prestados(): Lista los libros prestados con el usuario asociado.
