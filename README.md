# ed_semana_8

Sistema de Biblioteca Virtual

El Sistema de Biblioteca Virtual es un programa desarrollado en Python que permite gestionar libros en una biblioteca. El objetivo principal es proporcionar funcionalidades para agregar libros, prestar libros a usuarios, devolver libros prestados, buscar libros por su título, y visualizar los libros disponibles y prestados. Este sistema es útil para organizar y controlar el inventario de una biblioteca de manera sencilla y eficiente.

 Funciones:

1. agregar_libro()

Descripción: Permite al usuario agregar un nuevo libro al inventario.

Parámetros: Ninguno. Solicita id, titulo, y autor por entrada del usuario.

Resultado: Agrega el libro a la lista de libros disponibles.

2. prestar_libro()

Descripción: Permite prestar un libro a un usuario.

Parámetros: Ninguno. Solicita el id del libro y el nombre del usuario por entrada.

Resultado: Mueve el libro de la lista de disponibles a la lista de prestados y asocia el libro al usuario.

3. devolver_libro()

Descripción: Registra la devolución de un libro prestado.

Parámetros: Ninguno. Solicita el id del libro por entrada.

Resultado: Mueve el libro de la lista de prestados a la lista de disponibles.

4. buscar_libro_por_titulo()

Descripción: Busca un libro en las listas por su título.

Parámetros: Ninguno. Solicita el titulo del libro por entrada.

Resultado: Muestra la información del libro si se encuentra.

5. mostrar_libros_disponibles()

Descripción: Muestra todos los libros disponibles en la biblioteca.

Parámetros: Ninguno.

Resultado: Lista de libros con su id, titulo y autor.

6. mostrar_libros_prestados()

Descripción: Muestra todos los libros prestados junto con la información del usuario que los tiene.

Parámetros: Ninguno.

Resultado: Lista de libros con su id, titulo, autor, y usuario asociado.