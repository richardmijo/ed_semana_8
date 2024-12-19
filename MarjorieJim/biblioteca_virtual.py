# Listas para gestionar los libros
libros_disponibles = []
libros_prestados = []

def agregar_libro(id, titulo, autor):
    """
    Agrega un libro a la lista de libros disponibles.
    
    Parámetros:
    - id: Numero unico del libro.
    - titulo: Título del libro.
    - autor: Autor del libro.
    
    No devuelve ningun valor.
    """
    libro = {"id": id, "titulo": titulo, "autor": autor, "estado": "Disponible"}
    libros_disponibles.append(libro)
    print(f"Libro '{titulo}' agregado a la biblioteca.")

def prestar_libro(id, usuario):
    """
    Mueve un libro de la lista de disponibles a la lista de prestados.
    
    Parametros:
    - id: Numero unico del libro.
    - usuario: Nombre del usuario que recibe el libro.
    
    Devuelve un mensaje con el estado del prestamo.
    """
    for libro in libros_disponibles:
        if libro["id"] == id and libro["estado"] == "Disponible":
            libro["estado"] = "Prestado"
            libro["usuario"] = usuario
            libros_prestados.append(libro)
            libros_disponibles.remove(libro)
            return f"El libro '{libro['titulo']}' ha sido prestado a {usuario}."
    return "El libro no esa disponible."

def devolver_libro(id):
    """
    Regresa un libro de la lista de prestados a la lista de disponibles.
    
    Parámetros:
    - id: Numero unico del libro.
    
    Devuelve un mensaje con el estado de la devolucion.
    """
    for libro in libros_prestados:
        if libro["id"] == id:
            libro["estado"] = "Disponible"
            libro.pop("usuario", None)  
            libros_disponibles.append(libro)
            libros_prestados.remove(libro)
            return f"El libro '{libro['titulo']}' ha sido devuelto."
    return "El libro no esta en la lista de prestados."

def buscar_libro_por_titulo(titulo):
    """
    Busca un libro por titulo y devuelve su informacion.
    
    Parámetro:
    - titulo: El titulo del libro a buscar.
    
    Devuelve la informacion del libro si existe, o un mensaje de error.
    """
    for libro in libros_disponibles + libros_prestados:
        if libro["titulo"].lower() == titulo.lower():
            return libro
    return "No se encontro el libro."

def mostrar_libros_disponibles():
    """
    Muestra todos los libros disponibles en la biblioteca.
    
    No recibe parametros ni devuelve valores.
    """
    print("Libros disponibles:")
    if libros_disponibles:
        for libro in libros_disponibles:
            print(f"{libro['id']} - {libro['titulo']} por {libro['autor']}")
    else:
        print("No hay libros disponibles en este momento.")

def mostrar_libros_prestados():
    """
    Muestra todos los libros prestados junto con el usuario que los tiene.
    
    No recibe parametros ni devuelve valores.
    """
    print("Libros prestados:")
    if libros_prestados:
        for libro in libros_prestados:
            print(f"{libro['id']} - {libro['titulo']} prestado a {libro['usuario']}")
    else:
        print("No hay libros prestados en este momento.")

# Menu interactivo para probar el sistema
def menu():
    """
    Muestra un menu interactivo para gestionar los libros de la biblioteca.
    """
    while True:
        print("\nSistema de Biblioteca Virtual")
        print("1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Buscar libro por titulo")
        print("5. Mostrar libros disponibles")
        print("6. Mostrar libros prestados")
        print("7. Salir")
        
        opcion = input("Elige una opcion: ")
        
        if opcion == "1":
            id = int(input("Ingrese el ID del libro: "))
            titulo = input("Ingrese el titulo del libro: ")
            autor = input("Ingrese el autor del libro: ")
            agregar_libro(id, titulo, autor)
        
        elif opcion == "2":
            id = int(input("Ingrese el ID del libro a prestar: "))
            usuario = input("Ingrese el nombre del usuario: ")
            print(prestar_libro(id, usuario))
        
        elif opcion == "3":
            id = int(input("Ingrese el ID del libro a devolver: "))
            print(devolver_libro(id))
        
        elif opcion == "4":
            titulo = input("Ingrese el titulo del libro a buscar: ")
            resultado = buscar_libro_por_titulo(titulo)
            if isinstance(resultado, dict):
                print(f"Libro encontrado: {resultado['titulo']} por {resultado['autor']}, Estado: {resultado['estado']}")
            else:
                print(resultado)
        
        elif opcion == "5":
            mostrar_libros_disponibles()
        
        elif opcion == "6":
            mostrar_libros_prestados()
        
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no valida. Intenta de nuevo.")

# Ejecuta el menú
if __name__ == "__main__":
    menu()
