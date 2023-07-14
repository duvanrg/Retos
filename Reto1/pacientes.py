import os
import core
import citas

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
    
    os.system("clear")
    if opc == 1:
        AddPaciente()
    elif opc == 2:
        datos = BuscarPaciente()
        os.system("clear")
        if (datos == False):
            print('+','-'*55,'+')
            print("|{:^57}|".format("PACIENTE NO ENCONTRADO"))
            print('+','-'*55,'+')
        else:
            print('+','-'*30,'+')
            print("|{:^32}|".format(datos[0]))
            print('+','-'*30,'+')
            print("|{:^10}:{:^21}|".format(datos[2],datos[3]))
            print('+','-'*30,'+')
            for i, item in enumerate(datos[1]):
                print("|{:^4}|{:^27}|".format("Id",item["Id"]))
                print('+','-'*30,'+')
    elif opc == 3:
        datos = MostrarPaciente()
        band = 1
        os.system("clear")
        if (datos == False):
            print('+','-'*55,'+')
            print("|{:^57}|".format("PACIENTE NO ENCONTRADO"))
            print('+','-'*55,'+')
        else:
            paci = datos[0]
            histo = datos[1]
            print('+','-'*45,'+')
            print("|{:^47}|".format("DATOS DEL PACIENTE"))
            print('+','-'*45,'+')
            print("|{:^14}|{:^32}|".format('Id',paci["Id"]))
            print('+','-'*45,'+')
            print("|{:^14}|{:^32}|".format('Nombre',paci["Nombre"]))
            print('+','-'*45,'+')
            print("|{:^14}|{:^32}|".format('Edad',paci["Edad"]))
            print('+','-'*45,'+')
            print("|{:^14}|{:^32}|".format('Propietario',paci["Propietario"]))
            print('+','-'*45,'+')
            print("|{:^14}|{:^32}|".format('Especie',paci["Especie"]))
            print('+','-'*45,'+')
            print("|{:^14}|{:^32}|".format('Raza',paci["Raza"]))
            print('+','-'*45,'+\n')  
            for i, item in enumerate(histo):
                if band == 1:
                    print("+","-"*71,'+')
                    print("|{:^73}|".format('HISTORIAL MEDICO'))
                    print('+','-'*71,'+')
                    print("|{:^4}|{:^15}|{:^8}|{:^11}|{:^22}|{:^8}|".format('Id','Fecha','Hora', 'id Vet', 'NombreVet','IdPaci'))
                    print('+','-'*71,'+')
                    band = 0
                print("|{:^4}|{:^15}|{:^8}|{:^11}|{:^22}|{:^8}|".format(item['Id'],item['Fecha'],item['Hora'], item['IdVet'], item['NombreVet'], item['IdPaci']))
                print('+','-'*71,'+')
                valid = True
            input()
    elif opc == 4:
        exit = True

    if (not exit):
        os.system('sleep 3') 
        MainMenu()

def AddPaciente():
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
    print("seleccione la especie del paciente")
    for i, item in enumerate(especies):
        print(f"{i+1}. {item}")
        select.append(item)
    especie = select[int(input("> "))-1]
    select = []
    print("seleccione la raza del paciente")
    for i, item in enumerate(razas[especie]):
        print(f"{i+1}. {item}")
        select.append(item)
    raza = select[int(input("> "))-1]

    data = {
        "Id": autoId,
        "Nombre": nombre,
        "Edad": edad,
        "Propietario": propietario,
        "Especie": especie,
        "Raza":raza
        }
    core.CrearData("pacientes.json", data)

def BuscarPaciente():
    diccPaci = LoadDataPacientes("pacientes.json")
    especies = ["Perro","Gato","Reptil","Ave"]
    save = []
    select = []
    print('+','-'*55,'+')
    print("|{:^57}|".format('BUSCADOR DE PACIENTES'))
    print('+','-'*55,'+')
    print("Seleccione el dato por el cual buscar","1. Nombre","2. especie",sep=("\n"))
    opc = int(input("> "))
    if  opc == 1:
        paciSearch = input("Ingrese el nombre del paciente a buscar: ")
        opc = "Nombre"
    elif  opc == 2:
        print("Seleccione la especie")
        for i, item in enumerate(especies):
            print(f"{i+1}. {item}")
            select.append(item)
        paciSearch = select[int(input(">"))-1]
        opc = "Especie"
    else:
        print("seleccion no valida")
        return False

    for i, item in enumerate(diccPaci["data"]):
        if paciSearch == item["Nombre"] or paciSearch == item["Especie"]:
            save.append(item)
            
    if (len(save)==1):
        return (['PACIENTE ENCONTRADO',save,opc,paciSearch])
    elif (len(save)>1):
            return ([f'{len(save)} PACIENTES ENCONTRADOS',save,opc,paciSearch])
    else:
        return False      

def MostrarPaciente():
    diccPaci = LoadDataPacientes("pacientes.json")
    diccCitas = citas.LoadDataCitas("citas.json")
    save = []
    historial = []
    
    print('+','-'*55,'+')
    print("|{:^57}|".format('BUSCADOR INFORMACION DE PACIENTES'))
    print('+','-'*55,'+')
    paciSearch = int(input("Ingrese el Id del paciente a buscar: "))
    for i, item in enumerate(diccPaci["data"]):
        if paciSearch == item["Id"]:
            save.append(item)
            for i, cita in enumerate(diccCitas["data"]):
                if item["Id"] == cita["IdPaci"]:
                    historial.append(cita)
    save.append(historial)
    if (len(save)>=1):
        print (save)
        return save
    else:
        return False
