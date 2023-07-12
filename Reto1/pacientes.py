import os
import core

diccPaci = {"data": []}

def LoadDataPacientes(args):
    global diccPaci
    if core.CheckData(args):
        return core.LoadData(args)
    else:
        core.CrearData(args, diccPaci)
        return core.LoadData(args)
    
def MainMenu():
    os.system("clear")
    exit = False
    print ('+','-'*55,'+')
    print ('|{:^57}|'.format('MENU PACIENTES'))
    print ('+','-'*55,'+')
    print ("1. Agregar paciente","2. Buscar paciente","3. Mostrar informacion de un paciente","4. Volver al menú príncipal",sep="\n")
    opc = int(input("> "))
    if opc == 1:
        AddPaciente()
    elif opc == 2:
        datos = BuscarPaciente()
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^57}|".format(datos))
        print('+','-'*55,'+')
    elif opc == 3:
        datos = MostrarPaciente()
        if (datos == False):
            os.system("clear")
            print('+','-'*55,'+')
            print("|{:^57}|".format("Paciente no encontrado"))
            print('+','-'*55,'+')
        else:
            os.system("clear")
            print('+','-'*45,'+')
            print("|{:^47}|".format("DATOS DEL PACIENTE"))
            print('+','-'*45,'+')
            print("|{:^10}|{:^35}|".format('Id',datos["Id"]))
            print('+','-'*44,'+')
            print("|{:^10}|{:^35}|".format('Nombre',datos["Nombre"]))
            print('+','-'*44,'+')
            print("|{:^10}|{:^35}|".format('Edad',datos["Edad"]))
            print('+','-'*44,'+')
            print("|{:^10}|{:^35}|".format('Propietario',datos["Propietario"]))
            print('+','-'*44,'+')
            print("|{:^10}|{:^35}|".format('Tipo',datos["Tipo"]))
            print('+','-'*44,'+')
            print("|{:^10}|{:^35}|".format('Raza',datos["Raza"]))
            print('+','-'*44,'+')
            
    elif opc == 4:
        exit = True

    if (not exit):
        os.system('sleep 3') 
        MainMenu()

def AddPaciente():
    os.system("clear")
    diccPaci = LoadDataPacientes("pacientes.json")
    select = []
    tipos = ["Perro","Gato","Reptil","Ave"]
    razas = {"Perro":["Golden","Pastor Aleman","Chiguagua","Labrador","Bóxer","Pug","Retriever"],"Gato":["Persa","Abisinio","Siamés","British","Ragdoll","Manx"],"Reptil":["Iguana","Gecko","Camaleón","Tortuga","Serpiente"],"Ave":["Periquito","Canario","Cotorra","Cacatúa","Loro","faisanes","Agapornis"]}
    autoId = 0
    for i, item in enumerate(diccPaci["data"]):
        autoId = item["Id"]
    autoId += 1
    print(autoId)
    print ('+','-'*55,'+')
    print ('|{:^57}|'.format('AGREGAR PACIENTE'))
    print ('+','-'*55,'+')
    print ("Agrega los datos del paciente")
    nombre = str(input("Nombre: ")).title()
    edad = int(input("Edad: "))
    propietario = str(input("Nombre Propietario: ")).title()
    print("seleccione el tipo del paciente")
    for i, item in enumerate(tipos):
        print(f"{i+1}. {item}")
        select.append(item)
    tipo = select[int(input("> "))-1]
    select = []
    print("seleccione la raza del paciente")
    for i, item in enumerate(razas[tipo]):
        print(f"{i+1}. {item}")
        select.append(item)
    raza = select[int(input("> "))-1]

    data = {
        "Id": autoId,
        "Nombre": nombre,
        "Edad": edad,
        "Propietario": propietario,
        "Tipo": tipo,
        "Raza":raza
        }
    core.CrearData("pacientes.json", data)


def BuscarPaciente():
    os.system("clear")
    diccPaci = LoadDataPacientes("pacientes.json")
    point = []
    print('+','-'*55,'+')
    print("|{:^57}|".format('BUSCADOR DE PACIENTES'))
    print('+','-'*55,'+')
    paciSearch = input("Ingrese el nombre del paciente a buscar: ")
    for i, item in enumerate(diccPaci["data"]):
        if paciSearch in item["Nombre"]:
            point.append(item)
    if (len(point)==1):
        return ('PACIENTE ENCONTRADO')
    elif (len(point)>1):
        paciSearch = input("Ingrese el nombre del propietario del paciente: ")
        for item in point:
            if paciSearch in item["Propietario"]:
                return ('PACIENTE ENCONTRADO')
        return('PACIENTE NO ENCONTRADO')
        
    else:
        return('PACIENTE NO ENCONTRADO')
        

def MostrarPaciente():
    os.system("clear")
    diccPaci = LoadDataPacientes("pacientes.json")
    point = []
    print('+','-'*55,'+')
    print("|{:^57}|".format('BUSCADOR INFORMACION DE PACIENTES'))
    print('+','-'*55,'+')
    paciSearch = input("Ingrese el nombre del paciente a buscar: ")
    for i, item in enumerate(diccPaci["data"]):
        if paciSearch in item["Nombre"]:
            point.append(item)

    if (len(point)==1):
        return point[0]
    elif (len(point)>1):
        paciSearch = input("Ingrese el nombre del propietario del paciente: ")
        for i, item in enumerate(point):
            if paciSearch in item["Propietario"]:
                return point[i]
        return False
        
    else:
        return False
