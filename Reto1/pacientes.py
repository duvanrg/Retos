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
    os.system("cls")
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
        os.system("cls")
        print('+','-'*55,'+')
        print("|{:^57}|".format(datos))
        print('+','-'*55,'+')
    elif opc == 3:
        datos = MostrarPaciente()
        if (datos == False):
            os.system("cls")
            print('+','-'*55,'+')
            print("|{:^57}|".format("Paciente no encontrado"))
            print('+','-'*55,'+')
        else:
            os.system("cls")
            print('+','-'*45,'+')
            print("|{:^47}|".format("DATOS DEL PACIENTE"))
            print('+','-'*45,'+')
            print("|{:^14}|{:^32}|".format('Id',datos["Id"]))
            print('+','-'*45,'+')
            print("|{:^14}|{:^32}|".format('Nombre',datos["Nombre"]))
            print('+','-'*45,'+')
            print("|{:^14}|{:^32}|".format('Edad',datos["Edad"]))
            print('+','-'*45,'+')
            print("|{:^14}|{:^32}|".format('Propietario',datos["Propietario"]))
            print('+','-'*45,'+')
            print("|{:^14}|{:^32}|".format('Tipo',datos["Tipo"]))
            print('+','-'*45,'+')
            print("|{:^14}|{:^32}|".format('Raza',datos["Raza"]))
            print('+','-'*45,'+')
            
    elif opc == 4:
        exit = True

    if (not exit):
        os.system('pause') 
        MainMenu()

def AddPaciente():
    os.system("cls")
    diccPaci = LoadDataPacientes("pacientes.json")
    select = []
    especies = ["Perro","Gato","Reptil","Ave"]
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
    for i, item in enumerate(especies):
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
    os.system("cls")
    diccPaci = LoadDataPacientes("pacientes.json")
    especies = ["Perro","Gato","Reptil","Ave"]
    save = []
    select = []
    print('+','-'*55,'+')
    print("|{:^57}|".format('BUSCADOR DE PACIENTES'))
    print('+','-'*55,'+')
    print("Seleccione el dato por el cual buscar","1. Nombre","2. especie")
    if input("> ") == 1:
        paciSearch = input("Ingrese el nombre del paciente a buscar: ")
    else:
        print("Seleccione la especia a buscar")
        for i, item in enumerate(especies):
            print(f"{i+1}. {item}")
            select.append(item)
        paciSearch = select[int(input(">"))-1]

    for i, item in enumerate(diccPaci["data"]):
        if paciSearch in item["Nombre"] or paciSearch in item["Tipo"]:
            save.append(item)
    if (len(save)==1):
        return ('PACIENTE ENCONTRADO')
    elif (len(save)>1):
        paciSearch = input("Ingrese el nombre del propietario del paciente: ")
        for item in save:
            if paciSearch in item["Propietario"]:
                return ('PACIENTE ENCONTRADO')
        return('PACIENTE NO ENCONTRADO')
        
    else:
        return('PACIENTE NO ENCONTRADO')
        

def MostrarPaciente():
    os.system("cls")
    diccPaci = LoadDataPacientes("pacientes.json")
    save = []
    print('+','-'*55,'+')
    print("|{:^57}|".format('BUSCADOR INFORMACION DE PACIENTES'))
    print('+','-'*55,'+')
    paciSearch = input("Ingrese el nombre del paciente a buscar: ")
    for i, item in enumerate(diccPaci["data"]):
        if paciSearch in item["Nombre"]:
            save.append(item)

    if (len(save)==1):
        return save[0]
    elif (len(save)>1):
        paciSearch = input("Ingrese el nombre del propietario del paciente: ")
        for i, item in enumerate(save):
            if paciSearch in item["Propietario"]:
                return save[i]
        return False
    else:
        return False
