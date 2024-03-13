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

            #se obtiene el tipo de implante
            tipo_implante = implante.verTipo()

            if tipo_implante == "Marcapasos":
                implante.asignarNumElect(int(input("Ingrese el número de electrodos: ")))
                implante.asignarFrecuenciaE(int(input("Ingrese la frecuencia de estimulación: ")))
                tipo_marcapasos = input("Ingrese el tipo de marcapasos (alambrico o inalambrico): ")
                implante.asignarTipoMarcapasos(tipo_marcapasos)
                print("Se ha registrado el marcapasos correctamente.")

            elif tipo_implante == "StentCoronario":
                implante.asignarLongitud(int(input("Ingrese la longitud del stent coronario: ")))
                implante.asignarDiametro(int(input("Ingrese el diámetro del stent coronario: ")))
                implante.asignarMaterial(input("Ingrese el material del stent coronario: "))
                print("Se ha registrado el stent coronario correctamente.")

            elif tipo_implante == "ImplanteDental":
                implante.asignarForma(input("Ingrese la forma del implante dental: "))
                implante.asignarSistemaFij(input("Ingrese el sistema de fijación del implante dental: "))
                implante.asignarMaterial(input("Ingrese el material del implante dental: "))
                print("Se ha registrado el implante dental correctamente.")

            elif tipo_implante == "ImplanteRodilla" or tipo_implante == "ImplanteCadera":
                implante.asignarMaterial(input("Ingrese el material del implante de rodilla: "))
                implante.asignarTipoFijacion(input("Ingrese el tipo de fijación del implante de rodilla: "))
                implante.asignarTamaño(int(input("Ingrese el tamaño del implante de rodilla: ")))
                print("Se ha registrado el implante de rodilla o cadera correctamente.")

             # Incrementar el ID autoincremental y asignarlo al implante. Esto para que el 
             # implante tenga un identificador único
            self.__id_autoincremental += 1
            implante.asignarID(self.__id_autoincremental)

            # Agregar el implante a la lista
            self.__lista_implantes.append(implante)

    def mostrar_implantes(self):
        print("************** SE VAN A MOSTRAR LOS IMPLANTES **************************")
        print("\nLista de implantes:")
        for implante in self.__lista_implantes:
            print("----------------------------------------------------")
            print("ID:", implante.verID())
            print("Tipo:", implante.verTipo())
            print("Fecha Implantación:", implante.verFechaimp())
            print("Paciente:", implante.verPaciente())
            print("Médico:", implante.verMedicoR())
            print("Estado Implante:", implante.verEstadoimp())
            print("Fecha Revisión:", implante.verFecharev())
            print("Fecha Mantenimiento:", implante.verFechamant())
            

            if isinstance(implante, Marcapasos):
                print("Número de electrodos:", implante.verNumElect())
                print("Frecuencia de estimulación:", implante.verFrecuenciaE())
                print("Tipo de Marcapasos:", implante.verTipoMarcapasos())
            elif isinstance(implante, StentCoronario):
                print("Longitud:", implante.verLongitud())
                print("Diámetro:", implante.verDiametro())
                print("Material:", implante.verMaterial())
            elif isinstance(implante, ImplanteDental):
                print("Forma:", implante.verForma())
                print("Sistema de fijación:", implante.verSistemaFij())
                print("Material:", implante.verMaterial())
            elif isinstance(implante, ImplanteRodilla) or isinstance(implante, ImplanteCadera):
                print("Material:", implante.verMaterial())
                print("Tipo de fijación:", implante.verTipoFijacion())
                print("Tamaño:", implante.verTamaño())
        print("**************FIN MOSTAR IMPLANTES **************************")

    # Se toma un implante ya ingresado y se le asigna a un paciente
    def asignar_implante_paciente(self, idImplante, cedulaPaciente, cedulaMedico):
        print(idImplante)
        implante_encontrado = None
        for implante in self.__lista_implantes:
            if implante.verID() == idImplante:
                implante_encontrado = implante
                break

        if implante_encontrado:
            # Asignación de paciente
            implante_encontrado.asignarPaciente(cedulaPaciente)
            
            # Asignación de médico
            implante_encontrado.asignarMedicoR(cedulaMedico)
            
            # Asignación de fecha actual
            fecha_actual = datetime.now().strftime("%d/%m/%Y")
            implante_encontrado.asignarFechaimp(fecha_actual)
            
            # Asignación de estado del implante
            implante_encontrado.asignarEstadoimp("Correcto")

            # Ingreso de la fecha de revisión por el usuario
            fecha_revision = input("Ingrese la fecha de revisión (dd/mm/yyyy): ")
            implante_encontrado.asignarFecharev(fecha_revision)
            
            # Ingreso de la fecha de mantenimiento por el usuario
            fecha_mantenimiento = input("Ingrese la fecha de mantenimiento (dd/mm/yyyy): ")
            implante_encontrado.asignarFechamant(fecha_mantenimiento)
            print("Implante asignado correctamente al paciente con cédula:", cedulaPaciente)
        else:
            print("No se encontró ningún implante con el ID especificado.")

    def editar_implante(self):
        #solicitamos el implante que se quiere buscar
        id_implante = int(input("Ingrese el ID del implante que se desea editar: "))
        implante_encontrado = None
        #buscamos el implante en la lista de implantes
        for implante in self.__lista_implantes:
            if implante.verID() == id_implante:
                implante_encontrado = implante
                break
        if implante_encontrado:
            # Aquí se permite al usuario editar la información de cada atributo
            print("Editando información del implante ID:", id_implante)

            # Edición de las fechas de revisión y mantenimiento
            nueva_fecha_revision = input("Ingrese la nueva fecha de revisión (dd/mm/yyyy): ")
            implante_encontrado.asignarFecharev(nueva_fecha_revision)
            print("Fecha de revisión actualizada correctamente.")

            nueva_fecha_mantenimiento = input("Ingrese la nueva fecha de mantenimiento (dd/mm/yyyy): ")
            implante_encontrado.asignarFechamant(nueva_fecha_mantenimiento)
            print("Fecha de mantenimiento actualizada correctamente.")

            # Edición del ID del médico
            nuevo_id_medico = input("Ingrese el nuevo ID del médico: ")
            implante_encontrado.asignarMedicoR(nuevo_id_medico)
            print("ID del médico actualizado correctamente.")

            # Edición de información específica del marcapasos
            if isinstance(implante_encontrado, Marcapasos):
                print("Editando información específica del marcapasos.")
                nuevo_numero_electrodos = int(input("Ingrese el nuevo número de electrodos: "))
                implante_encontrado.asignarNumElect(nuevo_numero_electrodos)
                print("Número de electrodos actualizado correctamente.")
                nueva_frecuencia_estimulacion = int(input("Ingrese la nueva frecuencia de estimulación: "))
                implante_encontrado.asignarFrecuenciaE(nueva_frecuencia_estimulacion)
                print("Frecuencia de estimulación actualizada correctamente.")
                nuevo_tipo_marcapasos = input("Ingrese el nuevo tipo de marcapasos (alambrico o inalambrico): ")
                implante_encontrado.asignarTipoMarcapasos(nuevo_tipo_marcapasos)
                print("Tipo de marcapasos actualizado correctamente.")

             # Edición de la información especifica del StetCoronario    
            elif isinstance(implante_encontrado, StentCoronario):
                print("Editando información específica del Stent coronario.")
                nueva_longitud = int(input("Ingrese la nueva longitud de StentCoronario: "))
                implante_encontrado.asignarLongitud(nueva_longitud)
                print("longitud actualizada correctamente.")
                nuevo_diametro = int(input("Ingrese el nuevo diametro del stentCoronario: "))
                implante_encontrado.asignarDiametro(nuevo_diametro)
                print("Diametro actualizada correctamente.")
                nuevo_material = input("Ingrese el nuevo material del StentCoronario: ")
                implante_encontrado.asignarMaterial(nuevo_material)
                print("Material Actualizda correctamente")
             #edición de la información especifica implante Dental
            elif isinstance(implante_encontrado, ImplanteDental):
                print("Editando información específica del implanteDental.")
                nueva_forma= (input("Ingrese la nueva forma : "))
                implante_encontrado.asignarForma(nueva_forma)
                print(" Forma del implante dental actualizado correctamente.")
                nuevo_sistema_fijación = input("Ingrese el nuevo sistema de fijación del implante dental ")
                implante_encontrado.asignarSistemaFij(nuevo_sistema_fijación)
                print("Sistema de fijación actualizada correctamente.")
                nuevo_material = input("Ingrese el nuevo material delimplante dental ")
                implante_encontrado.asignarMaterial(nuevo_material)
                print("Material Actualizda correctamente")

            #edicion de la informacion especifica implante rodilla o cadera
            elif isinstance(implante_encontrado, ImplanteRodilla) or isinstance(implante_encontrado, ImplanteCadera):
                print("Editando información específica del implante de rodilla y cadera.")
                nuevo_material= (input("Ingrese el nuevo material : "))
                implante_encontrado.asignarMaterial(nuevo_material)
                print(" Forma del implante actualizado correctamente.")
                nuevo_tipo_fijación = input("Ingrese el nuevo tipo de fijación del implante: ")
                implante_encontrado.asignarTipoFijacion(nuevo_tipo_fijación)
                print("Tipo de fijación actualizada correctamente.")
                nuevo_tamaño = int(input("Ingrese el nuevo material del implante : "))
                implante_encontrado.asignarTamaño(nuevo_tamaño)
                print("Tamaño actualizada correctamente")
        else:
            print("No se encontró ningún implante con el ID especificado.")

    def eliminar_implante(self,IdImplante):
        for implante in self.__lista_implantes:
            if IdImplante == implante.verID():
                self.__lista_implantes.remove(implante)  
                return 
        

#Funcion main
def main ():
    #se crea el objeto de para la clase Sistema
    sis= Sistema()
    while True:
        opcion=int(input("\nIngrese \n0 para salir, \n1 para ingresar nuevo implante, \n2 Ver implantes Ingresados, \n3 para asignar implante a paciente,\n4 EditarImplante,\n5 EliminarImplante\n\t--> "))
        if opcion == 1:
            sis.agregar_implante()
        elif opcion == 2:
            sis.mostrar_implantes()
        elif opcion == 3:
            idImplante = int(input("Ingrese el ID del implante:"))
            cedulaPaciente = input("Ingrese la cédula del paciente:")
            cedulaMedico = input("Ingrese la cédula del médico:")
            sis.asignar_implante_paciente(idImplante, cedulaPaciente, cedulaMedico)

        elif opcion == 4:
            sis.editar_implante()

        elif opcion == 5 :
            ImplanteBorrar=int(input("Ingrese el id del implante que quiere borrar: "))
            resultado= sis.eliminar_implante(ImplanteBorrar)
            if resultado == True:
                print("Implante borrado con exito")
            else:
                print("No se encontró el implante con ese ID especificado")
        elif opcion == 0:
            break
        else:
            print("Opción incorrecta")
           
#funciòn principal
if __name__=="__main__":
    main()