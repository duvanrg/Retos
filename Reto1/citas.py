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
    os.system("clear")
    exit = False
    diccCitas = LoadDataCitas("citas.json")
    print ('+','-'*55,'+')
    print ('|{:^57}|'.format('MENU CITAS'))
    print ('+','-'*55,'+')
    print ("1. Crear Cita","2. Cancelar cita","3. Consultar citas por fecha","4. Consultar citas por veterinario","5. Volver al menú príncipal",sep="\n")
    opc = int(input("> "))
    os.system("clear")
    if opc == 1:
        AddCita()
    elif opc == 2:
        CancelarCita()
    elif opc == 3:
        BuscarCitaFecha()
    elif opc == 4:
        BuscarCitaVeterinaria()
    elif opc == 5:
        exit = True

    if (not exit):
        os.system('sleep 5') 
        MainMenu()

def AddCita():
    diccCitas = LoadDataCitas("citas.json")
    diccVet = veterinarios.LoadDataVeterinarios("veterinarios.json")
    diccPaci = pacientes.LoadDataPacientes("pacientes.json")
    autoId = 0
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
        idVet = str(input("Id Veterinario: "))
        for i, item in enumerate(diccVet):
            if idVet == item["Id"]:
                nombreVet = item["Nombre"]
                confirm = True
        if not confirm:
            print ("Veterinario no encontrado, intente otra vez")
    while not confirm:
        idPaci = str(input("Id Paciente: "))
        for i, item in enumerate(diccPaci):
            if idPaci == item["Id"]:
                confirm = True
        if not confirm:
            print ("Paciente no encontrado, intente otra vez")

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
    citaSearch = int(input("Ingrese el Id de la cita a cancelar"))
    for i, item in enumerate(diccCitas["data"]):
        if item["Id"] == citaSearch:
            print('+','-'*63,'+')
            print("|{:^45}|".format('CITA ENCONTRADA'))
            print('+','-'*63,'+')
            print("|{:^4}|{:^20}|{:^15}|{:^11}|{:^11}|".format('Id','Fecha','Hora', 'id Veterinario', 'NombreVet'))
            print('+','-'*63,'+')
            print("|{:^4}|{:^20}|{:^15}|{:^11}|{:^11}|".format(item['Id'],item['Fecha'],item['Hora'], item['IdVet'], item['Registro']))
            print('+','-'*63,'+')     
    

def BuscarCitaFecha():
    pass

def BuscarCitaVeterinaria():
    pass