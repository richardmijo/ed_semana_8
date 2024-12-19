class BibliotecaVirtual:
    def __init__(self):
        """Inicializa las listas de libros disponibles y prestados."""
        self.libros_disponibles = []
        self.libros_prestados = []

    def agregar_libro(self, id, titulo, autor):
        """Agrega un libro a la lista de libros disponibles.

        Args:
            id (int): Identificador único del libro.
            titulo (str): Título del libro.
            autor (str): Autor del libro.
        """
        libro = {"id": id, "titulo": titulo, "autor": autor, "estado": "Disponible"}
        self.libros_disponibles.append(libro)

    def prestar_libro(self, id, usuario):
        """Presta un libro a un usuario, moviéndolo de disponibles a prestados.

        Args:
            id (int): Identificador único del libro.
            usuario (str): Nombre del usuario.

        Returns:
            str: Mensaje indicando el resultado de la operación.
        """
        for libro in self.libros_disponibles:
            if libro["id"] == id:
                libro["estado"] = "Prestado"
                libro["usuario"] = usuario
                self.libros_disponibles.remove(libro)
                self.libros_prestados.append(libro)
                return f"El libro '{libro['titulo']}' ha sido prestado a {usuario}."
        return "Libro no disponible."

    def devolver_libro(self, id):
        """Devuelve un libro a la lista de disponibles.

        Args:
            id (int): Identificador único del libro.

        Returns:
            str: Mensaje indicando el resultado de la operación.
        """
        for libro in self.libros_prestados:
            if libro["id"] == id:
                libro["estado"] = "Disponible"
                libro.pop("usuario", None)
                self.libros_prestados.remove(libro)
                self.libros_disponibles.append(libro)
                return f"El libro '{libro['titulo']}' ha sido devuelto."
        return "Libro no encontrado en la lista de prestados."

    def buscar_libro_por_titulo(self, titulo):
        """Busca un libro por su título.

        Args:
            titulo (str): Título del libro a buscar.

        Returns:
            dict: Información del libro si se encuentra, o None si no existe.
        """
        for libro in self.libros_disponibles + self.libros_prestados:
            if libro["titulo"].lower() == titulo.lower():
                return libro
        return None

    def mostrar_libros_disponibles(self):
        """Imprime la lista de libros disponibles."""
        if not self.libros_disponibles:
            print("No hay libros disponibles.")
        else:
            print("Libros disponibles:")
            for libro in self.libros_disponibles:
                print(f"ID: {libro['id']}, Título: {libro['titulo']}, Autor: {libro['autor']}")

    def mostrar_libros_prestados(self):
        """Imprime la lista de libros prestados."""
        if not self.libros_prestados:
            print("No hay libros prestados.")
        else:
            print("Libros prestados:")
            for libro in self.libros_prestados:
                print(f"ID: {libro['id']}, Título: {libro['titulo']}, Usuario: {libro['usuario']}")

# Ejemplo de uso
if __name__ == "__main__":
    biblioteca = BibliotecaVirtual()

    # Agregar libros
    biblioteca.agregar_libro(1, "Cien Años de Soledad", "Gabriel García Márquez")
    biblioteca.agregar_libro(2, "Don Quijote de la Mancha", "Miguel de Cervantes")

    # Mostrar libros disponibles
    biblioteca.mostrar_libros_disponibles()

    # Prestar un libro
    print(biblioteca.prestar_libro(1, "Juan Perez"))

    # Mostrar libros disponibles y prestados
    biblioteca.mostrar_libros_disponibles()
    biblioteca.mostrar_libros_prestados()

    # Devolver un libro
    print(biblioteca.devolver_libro(1))

    # Mostrar libros disponibles y prestados nuevamente
    biblioteca.mostrar_libros_disponibles()
    biblioteca.mostrar_libros_prestados() 
