class Paciente:
    def __init__(self):
        self.__nombre = ""
        self.__genero = ""
        self.__servicio = ""
        self.__cedula = 0
    def Vernombre(self):
        return self.__nombre
    def Vergenero(self):
        return self.__genero
    def Verservicio(self):
        return self.__servicio
    def Vercedula(self):
        return self.__cedula
    def Asignar_nombre(self,name):
        self.__nombre = name
    def Asignar_genero(self,gender):
        self.__genero = gender
    def Asignar_servicio(self,service):
        self.__servicio= service
    def Asignar_cedula(self,id):
        self.__cedula= id
class Sistema:
    def __init__(self):
        self.__lista_pacientes=[]
        self.__num_pacientes = len(self.__lista_pacientes)
    def ingresar_paciente(self):
        nombre=input("Ingrese nombre del paciente: ")
        servicio=input("Ingrese servicio: ")
        genero=input("Ingrese género: ")
        cedula=int(input("Ingrese cedula: "))
        p=Paciente()
        p.Asignar_nombre(nombre)
        p.Asignar_cedula(cedula)
        p.Asignar_servicio(servicio)
        p.Asignar_genero(genero)
        self.__lista_pacientes.append(p)
        self.__num_pacientes = len(self.__lista_pacientes)
    def VerNumPacientes(self):
        return self.__num_pacientes
    def VerDatosPacientes(self):
        cedula=int(input("Ingrese cedula del paciente a buscar: "))
        for paciente in self.__lista_pacientes:
            if cedula == paciente.Vercedula():
                print("Nombre: "+ paciente.Vernombre())
                print("Servicio: "+ paciente.Verservicio())
                print("Genero: "+ paciente.Vergenero())
                print("Cedula: "+ str(paciente.Vercedula()))


Mi_sistema=Sistema()
while True:
    op=int(input("Ingrese opción a realizar\n1.Agregar paciente\n2.Ver cantidad de pacientes\n3.Ver datos de un paciente\n4.Salir"))
    if op==1:
        Mi_sistema.ingresar_paciente()
    elif op==2:
        print("Hay "+ str(Mi_sistema.VerNumPacientes())+ " Pacientes")
    elif op==3:
        Mi_sistema.VerDatosPacientes()
    elif op==4:
        break
    else:
        print("Ingrese opción valida")

