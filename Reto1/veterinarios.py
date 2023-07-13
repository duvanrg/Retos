import os
import core

diccVet = {"data": []}

def LoadDataVet(args):
    global diccVet
    if core.CheckData(args):
        return core.LoadData(args)
    else:
        core.CrearData(args, diccVet)
        return core.LoadData(args)
    
def MainMenu():
    os.system("cls")
    exit = False
    diccPaci = LoadDataVet("veterinarios.json")
    print ('+','-'*55,'+')
    print ('|{:^57}|'.format('MENU VETERINARIOS'))
    print ('+','-'*55,'+')
    print ("1. Agregar veterinario","2. Buscar veterinario","3. Mostrar informacion de un veterinario","4. Volver al menú príncipal",sep="\n")
    opc = int(input("> "))
    
    if opc == 1:
        AddVeterinario()
    elif opc == 2:
        datos = BuscarVeterinario()
        os.system("cls")
        print('+','-'*55,'+')
        print("|{:^57}|".format(datos))
        print('+','-'*55,'+')
    elif opc == 3:
        get = MostrarVeterinario()  
        print('+','-'*63,'+')
        print("|{:^65}|".format('RESULTADOS ENCONTRADOS'))
        print("|{:^4}|{:^20}|{:^15}|{:^11}|{:^11}|".format('Id','Nombre','Titulo', 'Telefono', 'Registro'))
        print('+','-'*63,'+')
        for i, item in enumerate(get):
            print("|{:^4}|{:^20}|{:^15}|{:^11}|{:^11}|".format(item['Id'],item['Nombre'],item['Titulo'], item['Telefono'], item['Registro']))
            print('+','-'*63,'+')       
    elif opc == 4:
        exit = True

    if (not exit):
        os.system('pause') 
        MainMenu()

def AddVeterinario():
    os.system("cls")
    select = []
    diccPaci = LoadDataVet("veterinarios.json")
    titulos = ["Ortopedista","Cirujano","Oncólogo","Oftalmólogo","Fisioterapeuta","Dermatólogo"]
    print ('+','-'*55,'+')
    print ('|{:^57}|'.format('AGREGAR VETERINARIO'))
    print ('+','-'*55,'+')
    print ("Agrega los datos del veterinario")
    idV = int(input("nro ID: "))
    nombre = str(input("Nombres: ")).title()
    print ("Selecione el Titulo profesional")
    for i, item in enumerate(titulos):
        print(f"{i+1}. {item}")
        select.append(item)
    titulo = select[int(input("> "))-1]
    telefono = input("Telefono: ")
    fechaReg = input("Fecha Registro : ")

    dataVet = {
        "Id": idV, 
        "Nombre": nombre, 
        "Titulo": titulo, 
        "Telefono": telefono,
        "Registro": fechaReg
        }
    core.CrearData("veterinarios.json",dataVet)

def BuscarVeterinario():
    os.system("cls")
    diccVet = LoadDataVet("veterinarios.json")
    save = []
    print('+','-'*55,'+')
    print("|{:^57}|".format('BUSCADOR DE VETERINARIO'))
    print('+','-'*55,'+')

    vetSearch = input("Ingrese el nombre o especialidad del veterinario a buscar: ")
    for i, item in enumerate(diccVet["data"]):
        if vetSearch in item["Nombre"] or vetSearch in item["Titulo"]:
            save.append(item)
    if (len(save)>=1):
        return ('VETERINARIO ENCONTRADO')
    else:
        return('VETERINARIO NO ENCONTRADO')

def MostrarVeterinario():
    diccVet = LoadDataVet("pacientes.json")
    save = []
    print('+','-'*55,'+')
    print("|{:^57}|".format('BUSCADOR INFORMACION DE PACIENTES'))
    print('+','-'*55,'+')
    vetSearch = input("Ingrese el nombre del paciente a buscar: ")
    for i, item in enumerate(diccVet["data"]):
        if vetSearch in item["Nombre"] or vetSearch in item["Titulo"]:
            save.append(item)

    if (len(save)>1):
        return save  
    else:
        return False