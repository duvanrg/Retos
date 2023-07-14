import os
import core
import veterinarios
import pacientes

diccCitas = {"data": []}

def LoadDataCitas(args):
    global diccCitas
    if core.CheckData(args):
        return core.LoadData(args)
    else:
        core.CrearData(args, diccCitas)
        return core.LoadData(args)
    
    
def MainMenu():
    os.system("cls")
    exit = False
    diccCitas = LoadDataCitas("citas.json")
    print ('+','-'*55,'+')
    print ('|{:^57}|'.format('MENU CITAS'))
    print ('+','-'*55,'+')
    print ("1. Crear Cita","2. Cancelar cita","3. Consultar cita","4. Volver al menú príncipal",sep="\n")
    opc = int(input("> "))
    os.system("cls")
    if opc == 1:
        AddCita()
    elif opc == 2:
        CancelarCita()
    elif opc == 3:
        BuscarCita()
    elif opc == 4:
        exit = True

    if (not exit):
        os.system('pause') 
        MainMenu()

def AddCita():
    diccCitas = LoadDataCitas("citas.json")
    diccVet = veterinarios.LoadDataVeterinarios("veterinarios.json")
    diccPaci = pacientes.LoadDataPacientes("pacientes.json")
    autoId = 0
    idVet = 0
    idPaci = 0
    confirm = False
    print ('+','-'*55,'+')
    print ('|{:^57}|'.format('AGREGAR CITA'))
    print ('+','-'*55,'+')
    print ("Agrega los datos de la cita")
    for i, item in enumerate(diccCitas["data"]):
        autoId = item["Id"]
    autoId += 1
    fecha = str(input("Fecha(dd/mm/aaaa): "))
    hora = str(input("Hora (hh:mm): "))
    while not confirm:
        idVet = int(input("Id Veterinario: "))
        for i, item in enumerate(diccVet["data"]):
            if idVet == item["Id"]:
                nombreVet = item["Nombre"]
                confirm = True
        if not confirm:
            print("Veterinario no encontrado, desea intentar de nuevo","1. Si","2. No",sep=("\n"))
            if (int(input("> "))==2):
                return False
            else:
                print ("Valor no valido")
                return False
    confirm = False
    while not confirm:
        idPaci = int(input("Id Paciente: "))
        for i, item in enumerate(diccPaci["data"]):
            print(item)
            if idPaci == item["Id"]:
                confirm = True
        if not confirm:
            print("Paciente no encontrado, desea intentar de nuevo","1. Si","2. No",sep=("\n"))
            if (int(input("> "))==2):
                return False
            else:
                print ("Valor no valido")
                return False
    dataCita = {
        "Id": autoId,
        "Fecha":fecha,
        "Hora": hora,
        "IdVet":idVet,
        "NombreVet": nombreVet,
        "IdPaci":idPaci,
        "Estado":"Agendada"
        }
    core.CrearData("citas.json", dataCita)
    print ('+','-'*55,'+')
    print ('|{:^17}|{:^40}|'.format('ID CITA :',autoId))
    print ('+','-'*55,'+')
    
def CancelarCita():
    diccCitas = LoadDataCitas("citas.json")
    print ('+','-'*55,'+')
    print ('|{:^57}|'.format('CANCELAR CITA'))
    print ('+','-'*55,'+')
    citaSearch = int(input("Ingrese el Id de la cita a cancelar: "))
    for i, item in enumerate(diccCitas["data"]):
        if item["Id"] == citaSearch:
            os.system("cls")
            if item["Estado"] == "Cancelada":
                print('+','-'*71,'+')
                print("|{:^73}|".format('CITA YA CANCELADA'))
                print('+','-'*71,'+')
                return True
            print('+','-'*71,'+')
            print("|{:^73}|".format('CITA ENCONTRADA'))
            print('+','-'*71,'+')
            print("|{:^4}|{:^15}|{:^8}|{:^11}|{:^22}|{:^8}|".format('Id','Fecha','Hora', 'id Vet', 'NombreVet','IdPaci'))
            print('+','-'*71,'+')
            print("|{:^4}|{:^15}|{:^8}|{:^11}|{:^22}|{:^8}|".format(item['Id'],item['Fecha'],item['Hora'], item['IdVet'], item['NombreVet'], item['IdPaci']))
            print('+','-'*71,'+')    
            print("Confirme la cancelacion de la cita","1. Si","2. No",sep=("\n"))
            if (select := int(input("> ")))==2:
                return False
            elif select == 1:
                print('+','-'*71,'+')
                print("|{:^73}|".format('CITA CANCELADA CORRECTAMENTE'))
                print('+','-'*71,'+')
                item["Estado"] = "Cancelada"
                core.EditarData("citas.json",diccCitas)    
            else: 
                print ("Valor no valido")
                return False
        
        else:
            print('+','-'*71,'+')
            print("|{:^73}|".format('CITA NO ENCONTRADA'))
            print('+','-'*71,'+')

def BuscarCita():
    diccCitas = LoadDataCitas("citas.json")
    band = 1
    valid = False
    print('+','-'*55,'+')
    print("|{:^57}|".format('BUSCADOR DE CITA'))
    print('+','-'*55,'+')
    print("Seleccione el dato por el cual buscar","1. fecha","2. veterinario","3. paciente")
    if (opc := int(input("> "))) == 1:
        datSearch = input("ingrese la fecha de la cita (dd/mm/aaaa): ")
    elif opc == 2:
        datSearch = int(input("ingrese el ID del veterinario: "))
    elif opc == 3:
        datSearch = int(input("ingrese el ID del paciente: "))
    else:
        print ("Valor no valido")
        return False
    for i, item in enumerate(diccCitas["data"]):
        if datSearch == item["Fecha"] or datSearch == item["IdVet"] or datSearch == item["IdPaci"]:
            if band == 1:
                print("+","-"*71,'+')
                print("|{:^73}|".format('CITA ENCONTRADA'))
                print('+','-'*71,'+')
                print("|{:^4}|{:^15}|{:^8}|{:^11}|{:^22}|{:^8}|".format('Id','Fecha','Hora', 'id Vet', 'NombreVet','IdPaci'))
                print('+','-'*71,'+')
                band = 0
            print("|{:^4}|{:^15}|{:^8}|{:^11}|{:^22}|{:^8}|".format(item['Id'],item['Fecha'],item['Hora'], item['IdVet'], item['NombreVet'], item['IdPaci']))
            print('+','-'*71,'+')
            valid = True
    if not valid:
        print("+","-"*71,'+')
        print("|{:^73}|".format('CITA NO ENCONTRADA'))
        print('+','-'*71,'+')
        return False
    else:
        return True