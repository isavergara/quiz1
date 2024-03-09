from datetime import datetime

class ImplantesMedicos:
    def __init__(self):
        self.__historia = 0
        self.__tipo = ""
        self.__fecha_imp = None
        self.__medico_r = ""
        self.__estado_imp = ""
        self.__fecha_rev = None
        self.__fecha_mant = None

    # Getters para todos los atributos
    def obtenerHistoria(self):
        return self.__historia
    def obtenerTipo(self):
        return self.__tipo
    def obtenerFechaImp(self):
        return self.__fecha_imp
    def obtenerMedicoR(self):
        return self.__medico_r
    def obtenerEstadoImp(self):
        return self.__estado_imp
    def obtenerFechaRev(self):
        return self.__fecha_rev
    def obtenerFechaMant(self):
        return self.__fecha_mant

    # Setters para todos los atributos
    def asignarHistoria(self, historia):
        self.__historia = historia
    def asignarTipo(self, tipo):
        self.__tipo = tipo
    def asignarFechaImp(self, fecha_imp):
        self.__fecha_imp = fecha_imp
    def asignarMedicoR(self, medico_r):
        self.__medico_r = medico_r
    def asignarEstadoImp(self, estado_imp):
        self.__estado_imp = estado_imp
    def asignarFechaRev(self, fecha_rev):
        self.__fecha_rev = fecha_rev

    def asignarFechaMant(self, fecha_mant):
        self.__fecha_mant = fecha_mant

#clase marcapasos
class Marcapasos(ImplantesMedicos):
    def __init__(self):
        # Llamamos al constructor de la clase padre ImplantesMedicos
        super().__init__()
        # Añadimos los nuevos atributos para la clase Marcapasos
        self.__num_elect = 0
        self.__tipo = ""
        self.__frecuencia_e = 0

    # Getters y Setters para los nuevos atributos

    def obtenerNumElect(self):
        return self.__num_elect
    def asignarNumElect(self, num_elect):
        self.__num_elect = num_elect
    def obtenerTipo(self):
        return self.__tipo
    def asignarTipo(self, tipo):
        self.__tipo = tipo
    def obtenerFrecuenciaE(self):
        return self.__frecuencia_e
    def asignarFrecuenciaE(self, frecuencia_e):
        self.__frecuencia_e = frecuencia_e
#Clase imp. de rodilla
class ImplanteRodilla(ImplantesMedicos):
    def __init__(self):
        super().__init__()
        self.__material = ""
        self.__tipo_fijacion = ""
        self.__tamaño = 0

    # Getters para los atributos

    def obtenerMaterial(self):
        return self.__material
    def obtenerTipoFijacion(self):
        return self.__tipo_fijacion
    def obtenerTamaño(self):
        return self.__tamaño

    # Setters para los atributos
    def asignarMaterial(self, material):
        self.__material = material
    def asignarTipoFijacion(self, tipo_fijacion):
        self.__tipo_fijacion = tipo_fijacion
    def asignarTamaño(self, tamaño):
        self.__tamaño = tamaño

#clase implante dental
class ImplanteDental(ImplantesMedicos):
    def __init__(self):
        # Llamamos al constructor de la clase padre ImplantesMedicos
        super().__init__()
        # Añadimos los nuevos atributos para la clase ImplanteDental
        self.__forma = ""
        self.__sistema_fijacion = ""
        self.__material = ""

    # Getters para los atributos

    def obtenerForma(self):
        return self.__forma
    def obtenerSistemaFijacion(self):
        return self.__sistema_fijacion
    def obtenerMaterial(self):
        return self.__material

    # Setters para los atributos
    def asignarForma(self, forma):
        self.__forma = forma
    def asignarSistemaFijacion(self, sistema_fijacion):
        self.__sistema_fijacion = sistema_fijacion
    def asignarMaterial(self, material):
        self.__material = material
#clase imp. de cadera        
class ImplanteCadera(ImplantesMedicos):
    def __init__(self):
        # Llamamos al constructor de la clase padre ImplantesMedicos
        super().__init__()
        # Añadimos los nuevos atributos para la clase ImplanteCadera
        self.__material = ""
        self.__tipoFijacion = ""
        self.__tamaño = 0

    # Getters para los atributos
    def obtenerMaterial(self):
        return self.__material
    def obtenerTipoFijacion(self):
        return self.__tipoFijacion
    def obtenerTamaño(self):
        return self.__tamaño

    # Setters para los atributos
    def asignarMaterial(self, material):
        self.__material = material
    def asignarTipoFijacion(self, tipoFijacion):
        self.__tipoFijacion = tipoFijacion
    def asignarTamaño(self, tamaño):
        self.__tamaño = tamaño
        
#clase stent coronario
class StentCoronario(ImplantesMedicos):
    def __init__(self):
        # Llamamos al constructor de la clase padre ImplantesMedicos
        super().__init__()
        # Añadimos los nuevos atributos para la clase StentCoronario
        self.__longitud = 0
        self.__diametro = 0
        self.__material = ""

    # Getters para los atributos

    def obtenerLongitud(self):
        return self.__longitud
    def obtenerDiametro(self):
        return self.__diametro
    def obtenerMaterial(self):
        return self.__material

    # Setters para los atributos

    def asignarLongitud(self, longitud):
        self.__longitud = longitud
    def asignarDiametro(self, diametro):
        self.__diametro = diametro
    def asignarMaterial(self, material):
        self.__material = material
                       
        