from datetime import datetime

# Clase Padre
class ImplanteMedico:
    def __init__(self, tipo):
        self.__tipo = tipo
        self.__fechaimp = None
        self.__medicoR = ""
        self.__paciente = ""
        self.__estadoimp = None
        self.__fecharev = None
        self.__fechamant = None
        self.__ID = 0

    # Getters y Setters
    
    def verTipo(self):
        return self.__tipo
    
    def verFechaimp(self):
        return self.__fechaimp
    
    def verMedicoR(self):
        return self.__medicoR
    
    def verEstadoimp(self):
        return self.__estadoimp
    
    def verFecharev(self):
        return self.__fecharev
    
    def verPaciente(self):
        return self.__paciente
    
    def verFechamant(self):
        return self.__fechamant
    
    def verID(self):
        return self.__ID
    
    def asignarID(self, ID):
        self.__ID = ID

    def asignarTipo(self, tipo):
        self.__tipo = tipo
    
    def asignarFechaimp(self, fechaimp):
        self.__fechaimp = fechaimp
    
    def asignarMedicoR(self, medicoR):
        self.__medicoR = medicoR

    def asignarPaciente(self, paciente):
        self.__paciente = paciente
    
    def asignarEstadoimp(self, estadoimp):
        self.__estadoimp = estadoimp
    
    def asignarFecharev(self, fecharev):
        self.__fecharev = fecharev
    
    def asignarFechamant(self, fechamant):
        self.__fechamant = fechamant


# Clase Hija Marcapasos
class Marcapasos(ImplanteMedico):
    def __init__(self):
        super().__init__("Marcapasos")
        self.__numElect = 0
        self.__frecuenciaE = 0
        self.__tipoMarcapasos = ""

    # Getters y Setters específicos para Marcapasos
    def verNumElect(self):
        return self.__numElect
    
    def asignarNumElect(self, numElect):
        self.__numElect = numElect
    
    def verFrecuenciaE(self):
        return self.__frecuenciaE
    
    def asignarFrecuenciaE(self, frecuenciaE):
        self.__frecuenciaE = frecuenciaE

    def verTipoMarcapasos(self):
        return self.__tipoMarcapasos

    def asignarTipoMarcapasos(self, tipoMarcapasos):
        self.__tipoMarcapasos = tipoMarcapasos

# Clase Hija Implante de Rodilla
class ImplanteRodilla(ImplanteMedico):
    def __init__(self):
        super().__init__("ImplanteRodilla")
        self.__material = ""
        self.__tipoFijacion = ""
        self.__tamaño = 0

    # Getters y Setters específicos para Implante de Rodilla
    def verMaterial(self):
        return self.__material
    
    def asignarMaterial(self, material):
        self.__material = material
    
    def verTipoFijacion(self):
        return self.__tipoFijacion
    
    def asignarTipoFijacion(self, tipoFijacion):
        self.__tipoFijacion = tipoFijacion
    
    def verTamaño(self):
        return self.__tamaño
    
    def asignarTamaño(self, tamaño):
        self.__tamaño = tamaño

# Clase Hija Implante Dental
class ImplanteDental(ImplanteMedico):
    def __init__(self):
        super().__init__("ImplanteDental")
        self.__forma = ""
        self.__sistemaFij = ""
        self.__material = ""

    # Getters y Setters específicos para Implante Dental
    def verForma(self):
        return self.__forma
    
    def asignarForma(self, forma):
        self.__forma = forma
    
    def verSistemaFij(self):
        return self.__sistemaFij
    
    def asignarSistemaFij(self, sistemaFij):
        self.__sistemaFij = sistemaFij
    
    def verMaterial(self):
        return self.__material
    
    def asignarMaterial(self, material):
        self.__material = material
#clase imp. de cadera        
class ImplanteCadera(ImplanteMedico):
    def __init__(self):
        # Llamamos al constructor de la clase padre ImplantesMedicos
        super().__init__("ImplanteCadera")
        # Añadimos los nuevos atributos para la clase ImplanteCadera
        self.__material = ""
        self.__tipoFijacion = ""
        self.__tamaño = 0

    # Getters para los atributos
    def verMaterial(self):
        return self.__material
    def verTipoFijacion(self):
        return self.__tipoFijacion
    def verTamaño(self):
        return self.__tamaño

    # Setters para los atributos
    def asignarMaterial(self, material):
        self.__material = material
    def asignarTipoFijacion(self, tipoFijacion):
        self.__tipoFijacion = tipoFijacion
    def asignarTamaño(self, tamaño):
        self.__tamaño = tamaño
# Clase Hija Stent Coronario
class StentCoronario(ImplanteMedico):
    def __init__(self):
        super().__init__("StentCoronario")
        self.__longitud = 0
        self.__diametro = 0
        self.__material = ""

    # Getters y Setters específicos para Stent Coronario
    def verLongitud(self):
        return self.__longitud
    
    def asignarLongitud(self, longitud):
        self.__longitud = longitud
    
    def verDiametro(self):
        return self.__diametro
    
    def asignarDiametro(self, diametro):
        self.__diametro = diametro
    
    def verMaterial(self):
        return self.__material
    
    def asignarMaterial(self, material):
        self.__material = material


#clase que representa el sistema de gestion de implantes médicos
class Sistema:    
    def __init__(self):
        # Inicialización de la lista de implantes
        self.__lista_implantes = [] 
        # Contador autoincremental para asignar IDs únicos a los implantes que después seran usados en la asignación al paciente
        self.__id_autoincremental = 0 
               
    def agregar_implante(self):
        while True:
            print("\nAgregar nuevo implante:")
            print("Seleccione el tipo de implante:")
            print("1. Marcapasos")
            print("2. Stent Coronario")
            print("3. Implante Dental")
            print("4. Implante de Rodilla")
            print("5. Implante de Cadera")
            print("6. Salir")

            tipo_implante_num = int(input("Ingrese el número correspondiente al tipo de implante: "))

            if tipo_implante_num == 1:
                implante = Marcapasos()
            elif tipo_implante_num == 2:
                implante = StentCoronario()
            elif tipo_implante_num == 3:
                implante = ImplanteDental()
            elif tipo_implante_num == 4:
                implante = ImplanteRodilla()
            elif tipo_implante_num == 5:
                implante = ImplanteCadera()
            else:
                print("El número ingresado no corresponde a ningún tipo de implante.")
                break    