class BibliotecaVirtual:
    def __init__(self):
        """Inicializa las listas para libros disponibles y prestados."""
        self.libros_disponibles = []
        self.libros_prestados = []

    def agregar_libro(self, id, titulo, autor):
        """Agrega un libro a la lista de libros disponibles.
        Args:
            id (int): Identificador único del libro.
            titulo (str): Título del libro.
            autor (str): Autor del libro.
        """
        libro = {
            "id": id,
            "titulo": titulo,
            "autor": autor,
            "estado": "Disponible"
        }
        self.libros_disponibles.append(libro)

    def prestar_libro(self, id, usuario):
        """Presta un libro a un usuario.
        Args:
            id (int): Identificador del libro.
            usuario (str): Nombre del usuario que solicita el libro.
        """
        for libro in self.libros_disponibles:
            if libro["id"] == id:
                libro["estado"] = "Prestado"
                libro["usuario"] = usuario
                self.libros_prestados.append(libro)
                self.libros_disponibles.remove(libro)
                print(f"El libro '{libro['titulo']}' ha sido prestado a {usuario}.")
                return
        print("El libro no está disponible para prestar.")

    def devolver_libro(self, id):
        """Devuelve un libro a la lista de disponibles.
        Args:
            id (int): Identificador del libro a devolver.
        """
        for libro in self.libros_prestados:
            if libro["id"] == id:
                libro["estado"] = "Disponible"
                libro.pop("usuario", None)
                self.libros_disponibles.append(libro)
                self.libros_prestados.remove(libro)
                print(f"El libro '{libro['titulo']}' ha sido devuelto.")
                return
        print("El libro no está en la lista de prestados.")

    def buscar_libro_por_titulo(self, titulo):
        """Busca un libro por su título.
        Args:
            titulo (str): Título del libro a buscar.
        Returns:
            dict: Información del libro si se encuentra, None si no.
        """
        for libro in self.libros_disponibles + self.libros_prestados:
            if libro["titulo"].lower() == titulo.lower():
                return libro
        print("El libro no se encuentra en la biblioteca.")
        return None

    def mostrar_libros_disponibles(self):
        """Muestra todos los libros disponibles."""
        print("Libros disponibles:")
        for libro in self.libros_disponibles:
            print(f"ID: {libro['id']}, Título: {libro['titulo']}, Autor: {libro['autor']}")

    def mostrar_libros_prestados(self):
        """Muestra todos los libros prestados."""
        print("Libros prestados:")
        for libro in self.libros_prestados:
            print(f"ID: {libro['id']}, Título: {libro['titulo']}, Autor: {libro['autor']}, Usuario: {libro['usuario']}")

# Ejemplo de uso
biblioteca = BibliotecaVirtual()
biblioteca.agregar_libro(1, "Cien Años de Soledad", "Gabriel García Márquez")
biblioteca.agregar_libro(2, "El Quijote", "Miguel de Cervantes")
biblioteca.mostrar_libros_disponibles()
biblioteca.prestar_libro(1, "Juan Perez")
biblioteca.mostrar_libros_prestados()
biblioteca.devolver_libro(1)
biblioteca.mostrar_libros_disponibles()
