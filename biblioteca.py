# Sistema de Biblioteca Virtual

# Listas para gestionar libros
libros_disponibles = []
libros_prestados = []

# Función para agregar un libro
def agregar_libro():
    try:
        id = int(input("Ingrese el ID del libro: "))
        titulo = input("Ingrese el título del libro: ").strip()
        autor = input("Ingrese el autor del libro: ").strip()

        for libro in libros_disponibles + libros_prestados:
            if libro["id"] == id:
                print("Ya existe un libro con ese ID. Intente de nuevo.")
                return

        libro = {"id": id, "titulo": titulo, "autor": autor, "estado": "Disponible"}
        libros_disponibles.append(libro)
        print(f"Libro '{titulo}' agregado exitosamente.")
    except ValueError:
        print("ID inválido. Intente de nuevo con un número.")

# Función para prestar un libro
def prestar_libro():
    try:
        id = int(input("Ingrese el ID del libro que desea prestar: "))
        usuario = input("Ingrese el nombre del usuario: ").strip()

        for libro in libros_disponibles:
            if libro["id"] == id:
                libro["estado"] = "Prestado"
                libro["usuario"] = usuario
                libros_prestados.append(libro)
                libros_disponibles.remove(libro)
                print(f"Libro '{libro['titulo']}' prestado a {usuario}.")
                return

        print(f"El libro con ID {id} no está disponible para préstamo.")
    except ValueError:
        print("ID inválido. Intente de nuevo con un número.")

# Función para devolver un libro
def devolver_libro():
    try:
        id = int(input("Ingrese el ID del libro que desea devolver: "))

        for libro in libros_prestados:
            if libro["id"] == id:
                libro["estado"] = "Disponible"
                libro.pop("usuario", None)
                libros_disponibles.append(libro)
                libros_prestados.remove(libro)
                print(f"Libro '{libro['titulo']}' devuelto exitosamente.")
                return

        print(f"El libro con ID {id} no está en la lista de prestados.")
    except ValueError:
        print("ID inválido. Intente de nuevo con un número.")

# Función para buscar un libro por título
def buscar_libro_por_titulo():
    titulo = input("Ingrese el título del libro que desea buscar: ").strip().lower()
    for libro in libros_disponibles + libros_prestados:
        if libro["titulo"].lower() == titulo:
            print(f"Libro encontrado: {libro}")
            return
    print(f"No se encontró ningún libro con el título '{titulo}'.")

# Función para mostrar libros disponibles
def mostrar_libros_disponibles():
    if libros_disponibles:
        print("Libros disponibles:")
        for libro in libros_disponibles:
            print(f"ID: {libro['id']}, Título: {libro['titulo']}, Autor: {libro['autor']}")
    else:
        print("No hay libros disponibles.")

# Función para mostrar libros prestados
def mostrar_libros_prestados():
    if libros_prestados:
        print("Libros prestados:")
        for libro in libros_prestados:
            print(f"ID: {libro['id']}, Título: {libro['titulo']}, Autor: {libro['autor']}, Usuario: {libro['usuario']}")
    else:
        print("No hay libros prestados.")

# Menú principal
def menu():
    while True:
        print("\n--- Menú Biblioteca Virtual ---")
        print("1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Buscar libro por título")
        print("5. Mostrar libros disponibles")
        print("6. Mostrar libros prestados")
        print("7. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            prestar_libro()
        elif opcion == "3":
            devolver_libro()
        elif opcion == "4":
            buscar_libro_por_titulo()
        elif opcion == "5":
            mostrar_libros_disponibles()
        elif opcion == "6":
            mostrar_libros_prestados()
        elif opcion == "7":
            print("Gracias por usar la Biblioteca Virtual. ¡Adiós!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecutar el sistema
if __name__ == "__main__":
    menu()
