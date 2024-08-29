# Definimos la clase Persona como base para los pacientes
class Persona:
    def __init__(self, nombre: str, edad: int, identificacion: str):
        self.nombre = nombre
        self.edad = edad
        self.identificacion = identificacion

# La clase Paciente se crea
class Paciente(Persona):
    def __init__(self, nombre: str, edad: int, identificacion: str, motivo_consulta: str):
        super().__init__(nombre, edad, identificacion)
        self.motivo_consulta = motivo_consulta

# Clase Consulta que guarda los detalles de la consulta médica
class Consulta:
    def __init__(self, paciente: Paciente, doctor: str, fecha: str):
        self.paciente = paciente
        self.doctor = doctor
        self.fecha = fecha

    def detalles_consulta(self) -> str:
        return f"Paciente: {self.paciente.nombre}, Doctor: {self.doctor}, Fecha: {self.fecha}"

# Clase Secretaria que maneja las consultas y verifica si el paciente ya tiene una cita
class Secretaria:
    def __init__(self):
        self.consultas = []

    def asignar_consulta(self, paciente: Paciente, doctor: str, fecha: str) -> None:
        # Verificamos si el paciente ya tiene una consulta previa
        consulta_previa = self.buscar_consulta_por_paciente(paciente)
        
        if consulta_previa:
            self._print_paciente_ya_tiene_consulta(paciente)
        else:
            # Asignamos una nueva consulta
            nueva_consulta = Consulta(paciente, doctor, fecha)
            self.consultas.append(nueva_consulta)
            self._print_consulta_asignada(paciente, doctor, fecha)

    def buscar_consulta_por_paciente(self, paciente: Paciente) -> Consulta:
        # Busca si el paciente ya tiene una consulta asignada
        for consulta in self.consultas:
            if consulta.paciente.identificacion == paciente.identificacion:
                return consulta
        return None

    def mostrar_consultas(self) -> None:
        for consulta in self.consultas:
            print(consulta.detalles_consulta())

    def _print_paciente_ya_tiene_consulta(self, paciente: Paciente) -> None:
        print(f"El paciente {paciente.nombre} ya tiene una consulta asignada. Páselo a la sala de espera.")

    def _print_consulta_asignada(self, paciente: Paciente, doctor: str, fecha: str) -> None:
        print(f"Consulta asignada para el paciente {paciente.nombre} con el doctor {doctor} el día {fecha}.")


#Planeamiento
# 1. Crear un objeto de la clase Paciente
# 2. Guardar la informacion de el paciente
# 3. Crear un objeto de la clase Secretaria
# 4. Asignar una consulta al paciente
# 5. Mostrar las consultas asignadas



    # Crear pacientes
paciente1 = Paciente("Manases Flores", 30, "1234567890", "Dolor de cabeza")
paciente2 = Paciente("Monica Turcios", 25, "9876543210", "Fiebre")

# Crear una secretaria
secretaria = Secretaria()

# Asignar consultas a los pacientes
secretaria.asignar_consulta(paciente1, "Dr. Cerritos", "2023-03-15")
secretaria.asignar_consulta(paciente2, "Dr. Neftali", "2023-03-16")

# Mostrar las consultas asignadas
secretaria.mostrar_consultas()

# Intentar asignar una nueva consulta a un paciente que ya tiene una
secretaria.asignar_consulta(paciente1, "Dr. Cerritos", "2023-03-17")

        
