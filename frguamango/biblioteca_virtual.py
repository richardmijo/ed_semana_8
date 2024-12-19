libros_disponibles = []  # Lista para almacenar los libros disponibles en la biblioteca
libros_prestados = []  # Lista para almacenar los libros prestados

# Función para agregar un libro a la biblioteca
def agregar_libro(id, titulo, autor):
    libro = {
        "id": id,  # ID único del libro
        "titulo": titulo,  # Título del libro
        "autor": autor,  # Autor del libro
        "estado": "Disponible"  # Estado inicial del libro (siempre "Disponible")
    }
    libros_disponibles.append(libro)  # Agrega el libro a la lista de disponibles
    print(f"El libro '{titulo}' ha sido agregado a la biblioteca.")  # Mensaje de confirmación

# Función para prestar un libro
def prestar_libro(id, usuario):
    for libro in libros_disponibles:  # Busca el libro en la lista de disponibles
        if libro["id"] == id:  # Si el ID del libro coincide
            libro["estado"] = "Prestado"  # Cambia el estado del libro a "Prestado"
            libro["usuario"] = usuario  # Asocia el libro con el usuario
            libros_disponibles.remove(libro)  # Elimina el libro de la lista de disponibles
            libros_prestados.append(libro)  # Añade el libro a la lista de prestados
            print(f"El libro '{libro['titulo']}' ha sido prestado a {usuario}.")  # Mensaje de confirmación
            return  # Termina la función
    print(f"El libro con ID {id} no está disponible para préstamo.")  # Mensaje si el libro no está disponible

# Función para devolver un libro
def devolver_libro(id):
    for libro in libros_prestados:  # Busca el libro en la lista de prestados
        if libro["id"] == id:  # Si el ID del libro coincide
            libro["estado"] = "Disponible"  # Cambia el estado del libro a "Disponible"
            libro.pop("usuario", None)  # Elimina la asociación del usuario
            libros_prestados.remove(libro)  # Elimina el libro de la lista de prestados
            libros_disponibles.append(libro)  # Añade el libro a la lista de disponibles
            print(f"El libro '{libro['titulo']}' ha sido devuelto a la biblioteca.")  # Mensaje de confirmación
            return  # Termina la función
    print(f"El libro con ID {id} no está en la lista de libros prestados.")  # Mensaje si el libro no está en prestados

# Función para buscar un libro por título
def buscar_libro_por_titulo(titulo):
    for libro in libros_disponibles + libros_prestados:  # Busca en ambas listas (disponibles y prestados)
        if libro["titulo"].lower() == titulo.lower():  # Compara el título ignorando mayúsculas/minúsculas
            return libro  # Retorna el libro encontrado
    print(f"No se encontró ningún libro con el título '{titulo}'.")  # Mensaje si no se encuentra el libro
    return None  # Retorna None si no se encuentra

# Función para mostrar los libros disponibles
def mostrar_libros_disponibles():
    print("\nLibros disponibles:")  # Encabezado de la sección
    if not libros_disponibles:  # Verifica si la lista está vacía
        print("No hay libros disponibles.")  # Mensaje si no hay libros disponibles
    else:
        for libro in libros_disponibles:  # Recorre la lista de libros disponibles
            print(f"ID: {libro['id']}, Título: {libro['titulo']}, Autor: {libro['autor']}, Estado: {libro['estado']}")

# Función para mostrar los libros prestados
def mostrar_libros_prestados():
    print("\nLibros prestados:")  # Encabezado de la sección
    if not libros_prestados:  # Verifica si la lista está vacía
        print("No hay libros prestados.")  # Mensaje si no hay libros prestados
    else:
        for libro in libros_prestados:  # Recorre la lista de libros prestados
            print(f"ID: {libro['id']}, Título: {libro['titulo']}, Autor: {libro['autor']}, Estado: {libro['estado']}, Usuario: {libro['usuario']}")

# Menú principal del programa
def menu():
    while True:  # Bucle infinito para mostrar el menú hasta que el usuario decida salir
        print("\n--- Menú Biblioteca Virtual ---")
        print("1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Buscar libro por título")
        print("5. Mostrar libros disponibles")
        print("6. Mostrar libros prestados")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")  # Solicita al usuario una opción
        
        if opcion == "1":  # Opción para agregar un libro
            id = int(input("Ingrese el ID del libro: "))  # Solicita el ID del libro
            titulo = input("Ingrese el título del libro: ")  # Solicita el título del libro
            autor = input("Ingrese el autor del libro: ")  # Solicita el autor del libro
            agregar_libro(id, titulo, autor)  # Llama a la función para agregar el libro
        elif opcion == "2":  # Opción para prestar un libro
            id = int(input("Ingrese el ID del libro a prestar: "))  # Solicita el ID del libro
            usuario = input("Ingrese el nombre del usuario: ")  # Solicita el nombre del usuario
            prestar_libro(id, usuario)  # Llama a la función para prestar el libro
        elif opcion == "3":  # Opción para devolver un libro
            id = int(input("Ingrese el ID del libro a devolver: "))  # Solicita el ID del libro
            devolver_libro(id)  # Llama a la función para devolver el libro
        elif opcion == "4":  # Opción para buscar un libro por título
            titulo = input("Ingrese el título del libro a buscar: ")  # Solicita el título del libro
            libro = buscar_libro_por_titulo(titulo)  # Llama a la función para buscar el libro
            if libro:  # Si el libro se encuentra, muestra su información
                print(f"ID: {libro['id']}, Título: {libro['titulo']}, Autor: {libro['autor']}, Estado: {libro['estado']}")
        elif opcion == "5":  # Opción para mostrar los libros disponibles
            mostrar_libros_disponibles()  # Llama a la función para mostrar los libros disponibles
        elif opcion == "6":  # Opción para mostrar los libros prestados
            mostrar_libros_prestados()  # Llama a la función para mostrar los libros prestados
        elif opcion == "7":  # Opción para salir del programa
            print("Saliendo del sistema...")  # Mensaje de salida
            break  # Termina el bucle y cierra el programa
        else:
            print("Opción no válida. Intente de nuevo.")  # Mensaje si la opción ingresada no es válida

# Punto de entrada del programa
if __name__ == "__main__":
    menu()  # Llama al menú principal
