# Listas para libros
librosDisponibles = []
librosPrestados = []

def agregar_libro(id, titulo, autor):
    """
    Agrega un libro a la lista de libros disponibles.
    """
    libro = {"id": id, "titulo": titulo, "autor": autor, "estado": "Disponible"}
    librosDisponibles.append(libro)

def prestar_libro(id, usuario):
    """
    Mueve un libro de disponible a prestado.
    """
    for libro in librosDisponibles:
        if libro["id"] == id:
            libro["estado"] = "Prestado"
            librosDisponibles.remove(libro)
            librosPrestados.append({"libro": libro, "usuario": usuario})
            return f"El libro '{libro['titulo']}' ha sido prestado a {usuario}."
    return "Libro no encontrado o ya prestado."

def devolver_libro(id):
    """
    Regresa un libro prestado a la lista de disponibles.
    """
    for prestamo in librosPrestados:
        if prestamo["libro"]["id"] == id:
            libro = prestamo["libro"]
            libro["estado"] = "Disponible"
            librosPrestados.remove(prestamo)
            librosDisponibles.append(libro)
            return f"El libro '{libro['titulo']}' ha sido devuelto."
    return "Libro no encontrado en la lista de prestados."

def buscar_libro_por_titulo(titulo):
    """
    Busca un libro por su título.
    """
    for libro in librosDisponibles + [prestamo["libro"] for prestamo in librosPrestados]:
        if libro["titulo"].lower() == titulo.lower():
            return libro
    return "Libro no encontrado."

def mostrar_libros_disponibles():
    """
    Muestra los libros disponibles.
    """
    print("Libros Disponibles:")
    for libro in librosDisponibles:
        print(f"ID: {libro['id']}, Título: {libro['titulo']}, Autor: {libro['autor']}")

def mostrar_libros_prestados():
    """
    Muestra los libros prestados.
    """
    print("Libros Prestados:")
    for prestamo in librosPrestados:
        libro = prestamo["libro"]
        usuario = prestamo["usuario"]
        print(f"ID: {libro['id']}, Título: {libro['titulo']}, Usuario: {usuario}")

# Ejemplo de uso
if __name__ == "__main__":
    # Agregar libros
    agregar_libro(1, "El Chavo", "Franco Quezada")
    agregar_libro(2, "Cien Años ", "Gabriel  ")
    agregar_libro(3, "1984", "George ")

    # Mostrar libros disponibles
    mostrar_libros_disponibles()

    # Prestar un libro
    print(prestar_libro(1, "Juan Pérez"))

    # Mostrar libros prestados
    mostrar_libros_prestados()

    # Devolver un libro
    print(devolver_libro(1))

    # Mostrar libros disponibles de nuevo
    mostrar_libros_disponibles()
