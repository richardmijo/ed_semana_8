libros_disponibles = []
libros_prestados = []

def agregar_libro(id, titulo, autor):
    libro = {
        "id": id,
        "titulo": titulo,
        "autor": autor,
        "estado": "Disponible"
    }
    libros_disponibles.append(libro)
    print(f"El libro '{titulo}' ha sido agregado a la biblioteca.")

def prestar_libro(id, usuario):
    for libro in libros_disponibles:
        if libro["id"] == id:
            libro["estado"] = "Prestado"
            libro["usuario"] = usuario
            libros_disponibles.remove(libro)
            libros_prestados.append(libro)
            print(f"El libro '{libro['titulo']}' ha sido prestado a {usuario}.")
            return
    print(f"El libro con ID {id} no está disponible para préstamo.")

def devolver_libro(id):
    for libro in libros_prestados:
        if libro["id"] == id:
            libro["estado"] = "Disponible"
            libro.pop("usuario", None)
            libros_prestados.remove(libro)
            libros_disponibles.append(libro)
            print(f"El libro '{libro['titulo']}' ha sido devuelto a la biblioteca.")
            return
    print(f"El libro con ID {id} no está en la lista de libros prestados.")

def buscar_libro_por_titulo(titulo):
    for libro in libros_disponibles + libros_prestados:
        if libro["titulo"].lower() == titulo.lower():
            return libro
    print(f"No se encontró ningún libro con el título '{titulo}'.")
    return None

def mostrar_libros_disponibles():
    print("\nLibros disponibles:")
    if not libros_disponibles:
        print("No hay libros disponibles.")
    else:
        for libro in libros_disponibles:
            print(f"ID: {libro['id']}, Título: {libro['titulo']}, Autor: {libro['autor']}, Estado: {libro['estado']}")

def mostrar_libros_prestados():
    print("\nLibros prestados:")
    if not libros_prestados:
        print("No hay libros prestados.")
    else:
        for libro in libros_prestados:
            print(f"ID: {libro['id']}, Título: {libro['titulo']}, Autor: {libro['autor']}, Estado: {libro['estado']}, Usuario: {libro['usuario']}")

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
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            id = int(input("Ingrese el ID del libro: "))
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            agregar_libro(id, titulo, autor)
        elif opcion == "2":
            id = int(input("Ingrese el ID del libro a prestar: "))
            usuario = input("Ingrese el nombre del usuario: ")
            prestar_libro(id, usuario)
        elif opcion == "3":
            id = int(input("Ingrese el ID del libro a devolver: "))
            devolver_libro(id)
        elif opcion == "4":
            titulo = input("Ingrese el título del libro a buscar: ")
            libro = buscar_libro_por_titulo(titulo)
            if libro:
                print(f"ID: {libro['id']}, Título: {libro['titulo']}, Autor: {libro['autor']}, Estado: {libro['estado']}")
        elif opcion == "5":
            mostrar_libros_disponibles()
        elif opcion == "6":
            mostrar_libros_prestados()
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
