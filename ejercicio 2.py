import datetime
# Definimos la clase Persona para representar al usuario
class Persona:
    def __init__(self, nombre: str, identificacion: str):
        self.nombre = nombre
        self.identificacion = identificacion

# Clase Libro para representar los libros disponibles para préstamo
class Libro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor

# Clase Prestamo que maneja la información del préstamo
class Prestamo:
    def __init__(self, libro: Libro, persona: Persona, fecha_prestamo: datetime, fecha_devolucion: datetime):
        self.libro = libro
        self.persona = persona
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def devolver_libro(self, fecha_devolucion_real: datetime) -> str:
        if fecha_devolucion_real > self.fecha_devolucion:
            dias_retraso = (fecha_devolucion_real - self.fecha_devolucion).days
            sancion = dias_retraso * 1  # Por ejemplo, 1 unidad de sanción por día de retraso
            return f"El libro se devolvió con {dias_retraso} días de retraso. Sanción: {sancion} unidades."
        else:
            return "El libro se devolvió a tiempo. No hay sanción."

# Clase Biblioteca que gestiona los préstamos y devoluciones
class Biblioteca:
    def __init__(self):
        self.prestamos = []

    def prestar_libro(self, libro: Libro, persona: Persona, dias_prestamo: int) -> str:
        fecha_prestamo = datetime.datetime.now()
        fecha_devolucion = fecha_prestamo + datetime.timedelta(days=dias_prestamo)
        prestamo = Prestamo(libro, persona, fecha_prestamo, fecha_devolucion)
        self.prestamos.append(prestamo)
        return f"El libro '{libro.titulo}' ha sido prestado a {persona.nombre}. Fecha límite de devolución: {fecha_devolucion.date()}."

    def devolver_libro(self, libro: Libro, persona: Persona, fecha_devolucion_real: datetime) -> str:
        for prestamo in self.prestamos:
            if prestamo.libro == libro and prestamo.persona == persona:
                self.prestamos.remove(prestamo)  # Remove the prestamo from the list
                return prestamo.devolver_libro(fecha_devolucion_real)
        return "No se encontró un préstamo registrado para este libro y persona."

#Ejemplo de uso
biblioteca = Biblioteca()

# Creamos algunos libros y personas
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
persona1 = Persona("Ana Pérez", "123456")

# Prestamos un libro
print(biblioteca.prestar_libro(libro1, persona1, 7))  # El libro se presta por 7 días

# Simulamos la devolución del libro después de 10 días (con retraso)
fecha_devolucion_real = datetime.datetime.now() + datetime.timedelta(days=10)
print(biblioteca.devolver_libro(libro1, persona1, fecha_devolucion_real))



#Planteamiento
# El problema consiste en crear un sistema de biblioteca que permita prestar y devolver.

# El sistema debe tener en cuenta la fecha de devolución y aplicar una sanción si
# el libro se devuelve después de la fecha límite.

# El sistema debe poder gestionar múltiples préstamos y devoluciones.
# El sistema debe poder gestionar múltiples libros y personas.
