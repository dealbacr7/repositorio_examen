class Libro:
    def __init__(self, libro, autor, cantidad_disponible):
        self.libro = libro
        self.autor = autor
        self.cantidad_disponible = cantidad_disponible

biblioteca = []

def añadir_libro():
    datos = input("Añade un libro con título, autor y cantidad disponible (separados por comas): ")
    try:
        titulo, autor, cantidad = [d.strip() for d in datos.split(",")]
        nuevo_libro = Libro(titulo, autor, int(cantidad))
        biblioteca.append(nuevo_libro)
        print(f"Libro '{titulo}' añadido correctamente.")
    except:
        print("Formato incorrecto. Use: Título, Autor, Cantidad")

def prestar_libro():
    titulo = input("Ingrese el título del libro a prestar: ")
    for libro in biblioteca:
        if libro.libro.lower() == titulo.lower():
            if libro.cantidad_disponible > 0:
                libro.cantidad_disponible -= 1
                print(f"Libro '{libro.libro}' prestado. Quedan {libro.cantidad_disponible} ejemplares.")
            else:
                print("No hay ejemplares disponibles de este libro.")
            return
    print("Libro no encontrado en la biblioteca.")

def devolver_libro():
    titulo = input("Ingrese el título del libro a devolver: ")
    for libro in biblioteca:
        if libro.libro.lower() == titulo.lower():
            libro.cantidad_disponible += 1
            print(f"Libro '{libro.libro}' devuelto. Ahora hay {libro.cantidad_disponible} ejemplares.")
            return
    print("Libro no encontrado en la biblioteca.")

def consultar_libro():
    titulo = input("Ingrese el título del libro a consultar: ")
    for libro in biblioteca:
        if libro.libro.lower() == titulo.lower():
            print(f"\nTítulo: {libro.libro}")
            print(f"Autor: {libro.autor}")
            print(f"Ejemplares disponibles: {libro.cantidad_disponible}")
            return
    print("Libro no encontrado en la biblioteca.")

def sugerir_libro():
    if not biblioteca:
        print("No hay libros en la biblioteca.")
        return
    
    ultimo_libro = input("¿Cuál fue el último libro que leíste? ").strip().lower()
    
    libro_encontrado = None
    for libro in biblioteca:
        if libro.libro.lower() == ultimo_libro:
            libro_encontrado = libro
            break
    
    if libro_encontrado:
        autor = libro_encontrado.autor
        recomendaciones = []
        
        print(f"\nBasado en que leíste '{libro_encontrado.libro}', te recomendamos:")
        print("\nOtros libros del mismo autor:")
        for libro in biblioteca:
            if libro.autor == autor and libro.libro.lower() != ultimo_libro:
                recomendaciones.append(libro)
                print(f"- {libro.libro} ({libro.cantidad_disponible} disponibles)")
        

        if len(recomendaciones) < 3:
            print("\nOtros libros que podrían interesarte:")
            for libro in biblioteca:
                if libro.libro.lower() != ultimo_libro and libro not in recomendaciones:
                    print(f"- {libro.libro} de {libro.autor} ({libro.cantidad_disponible} disponibles)")
                    if len(recomendaciones) >= 5:
                        break
    else:
        print("\nNo encontramos ese libro en nuestra biblioteca. Te recomendamos:")
        print("Libros más populares:")
        for i, libro in enumerate(biblioteca[:5], 1):
            print(f"{i}. {libro.libro} de {libro.autor} ({libro.cantidad_disponible} disponibles)")

def ordenar_libros():
    if not biblioteca:
        print("No hay libros en la biblioteca.")
        return
    
    libros_ordenados = sorted(biblioteca, key=lambda x: x.cantidad_disponible, reverse=True)
    print("\nLibros ordenados por cantidad disponible (descendente):")
    print("{:<5} {:<40} {:<30} {:<10}".format("No.", "Título", "Autor", "Disponibles"))
    print("-"*85)
    for i, libro in enumerate(libros_ordenados, 1):
        print("{:<5} {:<40} {:<30} {:<10}".format(
            i, 
            libro.libro[:37] + "..." if len(libro.libro) > 40 else libro.libro,
            libro.autor[:27] + "..." if len(libro.autor) > 30 else libro.autor,
            libro.cantidad_disponible
        ))

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 10)
libro2 = Libro("1984", "George Orwell", 9)
libro3 = Libro("El Principito", "Antoine de Saint-Exupéry", 8)
libro4 = Libro("Orgullo y prejuicio", "Jane Austen", 8)
libro5 = Libro("Crónica de una muerte anunciada", "Gabriel García Márquez", 7)

biblioteca.extend([libro1, libro2, libro3, libro4, libro5])

def menu():
    while True:
        print("\nMenú Principal")
        print("1. Añadir un libro")
        print("2. Tomar prestado un libro")
        print("3. Devolver un libro")
        print("4. Consultar un libro en la base de datos")
        print("5. Sugerir un libro")
        print("6. Ordenar libros por cantidad disponible")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            añadir_libro()
        elif opcion == "2":
            prestar_libro()
        elif opcion == "3":
            devolver_libro()
        elif opcion == "4":
            consultar_libro()
        elif opcion == "5":
            sugerir_libro()
        elif opcion == "6":
            ordenar_libros()
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
