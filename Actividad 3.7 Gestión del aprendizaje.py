# Lista de libros disponibles y prestados
libros_disponibles = []
libros_prestados = []

def agregar_libro(id, titulo, autor):
    """
    Agrega un libro a la lista de libros disponibles.
    
    Parámetros:
    id (int): El ID único del libro.
    titulo (str): El título del libro.
    autor (str): El autor del libro.
    """
    libro = {'id': id, 'titulo': titulo, 'autor': autor, 'estado': 'Disponible'}
    libros_disponibles.append(libro)
    print(f"El libro '{titulo}' ha sido agregado.")

def prestar_libro(id, usuario):
    """
    Mueve un libro de la lista de disponibles a la lista de prestados, asociándolo al usuario.
    
    Parámetros:
    id (int): El ID del libro a prestar.
    usuario (str): El nombre del usuario que recibe el libro.
    """
    for libro in libros_disponibles:
        if libro['id'] == id:
            libro['estado'] = 'Prestado'
            libro['usuario'] = usuario
            libros_prestados.append(libro)
            libros_disponibles.remove(libro)
            print(f"El libro '{libro['titulo']}' ha sido prestado a {usuario}.")
            return
    print("Libro no encontrado.")

def devolver_libro(id):
    """
    Regresa un libro de la lista de prestados a la lista de disponibles.
    
    Parámetros:
    id (int): El ID del libro a devolver.
    """
    for libro in libros_prestados:
        if libro['id'] == id:
            libro['estado'] = 'Disponible'
            del libro['usuario']
            libros_disponibles.append(libro)
            libros_prestados.remove(libro)
            print(f"El libro '{libro['titulo']}' ha sido devuelto.")
            return
    print("Libro no encontrado.")

def buscar_libro_por_titulo(titulo):
    """
    Busca un libro por su título y devuelve su información.
    
    Parámetros:
    titulo (str): El título del libro a buscar.
    """
    for libro in libros_disponibles + libros_prestados:
        if libro['titulo'].lower() == titulo.lower():
            return libro
    return "Libro no encontrado."

def mostrar_libros_disponibles():
    """
    Imprime todos los libros disponibles.
    """
    if not libros_disponibles:
        print("No hay libros disponibles.")
        return
    for libro in libros_disponibles:
        print(f"ID: {libro['id']} | Título: {libro['titulo']} | Autor: {libro['autor']}")

def mostrar_libros_prestados():
    """
    Imprime todos los libros prestados junto con la información del usuario que lo tiene.
    """
    if not libros_prestados:
        print("No hay libros prestados.")
        return
    for libro in libros_prestados:
        print(f"ID: {libro['id']} | Título: {libro['titulo']} | Autor: {libro['autor']} | Usuario: {libro['usuario']}")

def mostrar_menu():
    """
    Muestra el menú de opciones para interactuar con el sistema de biblioteca.
    """
    while True:
        print("\n--- Sistema de Biblioteca Virtual ---")
        print("1. Agregar un libro")
        print("2. Prestar un libro")
        print("3. Devolver un libro")
        print("4. Buscar un libro por título")
        print("5. Mostrar libros disponibles")
        print("6. Mostrar libros prestados")
        print("7. Salir")
        opcion = input("Seleccione una opción (1-7): ")

        if opcion == '1':
            id = int(input("Ingrese el ID del libro: "))
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            agregar_libro(id, titulo, autor)
        elif opcion == '2':
            id = int(input("Ingrese el ID del libro a prestar: "))
            usuario = input("Ingrese el nombre del usuario: ")
            prestar_libro(id, usuario)
        elif opcion == '3':
            id = int(input("Ingrese el ID del libro a devolver: "))
            devolver_libro(id)
        elif opcion == '4':
            titulo = input("Ingrese el título del libro a buscar: ")
            resultado = buscar_libro_por_titulo(titulo)
            if isinstance(resultado, dict):
                print(f"ID: {resultado['id']} | Título: {resultado['titulo']} | Autor: {resultado['autor']} | Estado: {resultado['estado']}")
            else:
                print(resultado)
        elif opcion == '5':
            mostrar_libros_disponibles()
        elif opcion == '6':
            mostrar_libros_prestados()
        elif opcion == '7':
            print("Gracias por usar el sistema de Biblioteca Virtual.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 7.")

# Ejecutar el menú
if __name__ == "__main__":
    mostrar_menu()
