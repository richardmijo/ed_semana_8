libros_disponibles = []
libros_prestados = []

# Agregar los libros
def agregar_libro(id, titulo, autor):
    """
    Agrega un libro a la lista de libros disponibles.
    """
    libros_disponibles.append({'id': id, 'titulo': titulo, 'autor': autor, 'estado': 'Disponible'})
    print(f"Libro '{titulo}' agregado con éxito.")

# Prestar un libro
def prestar_libro(id, usuario):
    """
    Mueve un libro de la lista de disponibles a la lista de prestados, asociándolo a un usuario.
    """
    for libro in libros_disponibles:
        if libro['id'] == id and libro['estado'] == 'Disponible':
            libro['estado'] = 'Prestado'
            libro['usuario'] = usuario
            libros_disponibles.remove(libro)
            libros_prestados.append(libro)
            print(f"Libro '{libro['titulo']}' prestado a {usuario}.")
            return
    print("Libro no disponible o no encontrado.")

# Devolver un libro
def devolver_libro(id):
    """
    Regresa un libro de la lista de prestados a la lista de disponibles.
    """
    for libro in libros_prestados:
        if libro['id'] == id:
            libro['estado'] = 'Disponible'
            libro.pop('usuario', None)
            libros_prestados.remove(libro)
            libros_disponibles.append(libro)
            print(f"Libro '{libro['titulo']}' devuelto con éxito.")
            return
    print("Libro no encontrado en la lista de prestados.")

# Buscar libro por título
def buscar_libro_por_titulo(titulo):
    """
    Busca un libro por su título y devuelve su información.
    """
    for libro in libros_disponibles + libros_prestados:
        if libro['titulo'].lower() == titulo.lower():
            return libro
    return "Libro no encontrado."

# Mostrar libros disponibles
def mostrar_libros_disponibles():
    """
    Muestra todos los libros disponibles.
    """
    print("\nLibros disponibles:")
    if not libros_disponibles:
        print("No hay libros disponibles.")
    for libro in libros_disponibles:
        print(f"ID: {libro['id']}, Título: {libro['titulo']}, Autor: {libro['autor']}")

# Mostrar libros prestados
def mostrar_libros_prestados():
    """
    Muestra todos los libros prestados junto con el usuario que los tiene.
    """
    print("\nLibros prestados:")
    if not libros_prestados:
        print("No hay libros prestados.")
    for libro in libros_prestados:
        print(f"ID: {libro['id']}, Título: {libro['titulo']}, Autor: {libro['autor']}, Usuario: {libro['usuario']}")

# Menú interactivo
def menu():
    while True:
        print("\n=== Menú de la Biblioteca Virtual ===")
        print("1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Buscar libro por título")
        print("5. Mostrar libros disponibles")
        print("6. Mostrar libros prestados")
        print("7. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            id = int(input("ID del libro: "))
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            agregar_libro(id, titulo, autor)
        
        elif opcion == "2":
            id = int(input("ID del libro a prestar: "))
            usuario = input("Nombre del usuario: ")
            prestar_libro(id, usuario)
        
        elif opcion == "3":
            id = int(input("ID del libro a devolver: "))
            devolver_libro(id)
        
        elif opcion == "4":
            titulo = input("Título del libro a buscar: ")
            resultado = buscar_libro_por_titulo(titulo)
            print(resultado)
        
        elif opcion == "5":
            mostrar_libros_disponibles()
        
        elif opcion == "6":
            mostrar_libros_prestados()
        
        elif opcion == "7":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        
        else:
            print("Opción inválida. Inténtalo nuevamente.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
