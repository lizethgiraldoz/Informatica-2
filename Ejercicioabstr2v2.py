class Paciente:
    def __init__(self, nombre, cedula, genero, servicio):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__genero = genero
        self.__servicio = servicio

    def get_nombre(self):
        return self.__nombre

    def get_cedula(self):
        return self.__cedula

    def get_genero(self):
        return self.__genero

    def get_servicio(self):
        return self.__servicio

    def __str__(self):
        return (f"Nombre  : {self.__nombre}\n"
                f"Cédula  : {self.__cedula}\n"
                f"Género  : {self.__genero}\n"
                f"Servicio: {self.__servicio}")
    
class Sistema:
    def __init__(self):
        self.__pacientes = []
        
    def registrar_paciente(self):
        print("\n Registro de Nuevo Paciente")
        nombre   = input("Nombre   : ").strip()
        cedula   = int(input("Cédula   : "))
        genero   = input("Género   : ").strip()
        servicio = input("Servicio : ").strip()

        nuevo = Paciente(nombre, cedula, genero, servicio)
        self.__pacientes.append(nuevo)
        print(f"Paciente '{nombre}' registrado con exito.")


    def total_pacientes(self):
        return len(self.__pacientes)

    def buscar_paciente(self):
        print("\n--- Búsqueda de Paciente ---")
        cedula = int(input("Ingrese la cédula a buscar: "))
        encontrado = None

        for p in self.__pacientes:
            if p.get_cedula() == cedula:
                encontrado = p
                break

        if encontrado:
            print("\n Datos del Paciente ")
            print(encontrado)
        else:
            print(" No se encontro ningun paciente con esa cédula.")
                
sistemaPacientes = Sistema()

while True:
    try:
     opcion = int(input("1. nuevo paciente - 2. Numero de Pacientes - 3. Datos Paciente - 4. Salir"))
    except ValueError:
        print( "Por favor ingrese un número válido.")
        continue

    if opcion == 1:
        sistemaPacientes.registrar_paciente()
    elif opcion == 2:
        print(f"\nTotal de pacientes registrados: {sistemaPacientes.total_pacientes()}")
    elif opcion == 3:
        sistemaPacientes.buscar_paciente()
    elif opcion == 4:
        break
    else:
        print(" Opción inválida. Intente de nuevo.")