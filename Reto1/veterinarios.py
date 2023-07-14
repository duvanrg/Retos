import os
import core

diccVet = {"data": []}

def LoadDataVeterinarios(args):
    global diccVet
    if core.CheckData(args):
        return core.LoadData(args)
    else:
        core.CrearData(args, diccVet)
        return core.LoadData(args)
    
def MainMenu():
    os.system("cls")
    exit = False
    diccPaci = LoadDataVeterinarios("veterinarios.json")
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
        if (datos == False):
            print('+','-'*55,'+')
            print("|{:^57}|".format("VETERINARIO NO ENCONTRADO"))
            print('+','-'*55,'+')
        else:
            print('+','-'*35,'+')
            print("|{:^37}|".format(datos[0]))
            print('+','-'*35,'+')
            print("|{:^15}:{:^21}|".format(datos[2],datos[3]))
            print('+','-'*35,'+')
            for i, item in enumerate(datos[1]):
                print("|{:^4}|{:^32}|".format("Id",item["Id"]))
                print('+','-'*35,'+')
    elif opc == 3:
        datos = MostrarVeterinario()
        os.system("cls")
        if (datos == False):
            print('+','-'*55,'+')
            print("|{:^57}|".format("PACIENTE NO ENCONTRADO"))
            print('+','-'*55,'+')
        else:
            print('+','-'*63,'+')
            print("|{:^65}|".format('RESULTADOS ENCONTRADOS'))
            print('+','-'*63,'+')
            print("|{:^4}|{:^20}|{:^15}|{:^11}|{:^11}|".format('Id','Nombre','Titulo', 'Telefono', 'Registro'))
            print('+','-'*63,'+')
            for i, item in enumerate(datos):
                print("|{:^4}|{:^20}|{:^15}|{:^11}|{:^11}|".format(item['Id'],item['Nombre'],item['Titulo'], item['Telefono'], item['Registro']))
                print('+','-'*63,'+')       
    elif opc == 4:
        exit = True

    if (not exit):
        os.system('pause') 
        MainMenu()

def AddVeterinario():
    select = []
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
    fechaReg = input("Fecha Registro (dd/mm/aaaa): ")

    dataVet = {
        "Id": idV, 
        "Nombre": nombre, 
        "Titulo": titulo, 
        "Telefono": telefono,
        "Registro": fechaReg
        }
    core.CrearData("veterinarios.json",dataVet)

def BuscarVeterinario():
    diccVet = LoadDataVeterinarios("veterinarios.json")
    save = []
    select = []
    titulos = ["Ortopedista","Cirujano","Oncólogo","Oftalmólogo","Fisioterapeuta","Dermatólogo"]
    print('+','-'*55,'+')
    print("|{:^57}|".format('BUSCADOR DE VETERINARIO'))
    print('+','-'*55,'+')
    print("Seleccione el dato por el cual buscar","1. Nombre","2. Especialidad",sep=("\n"))
    opc = int(input("> "))
    if opc == 1:
        vetSearch = input("Ingrese el nombre del veterinario a buscar: ")
        opc = "Nombre"
    elif opc == 2:
        print("Seleccione la especialidad")    
        for i, item in enumerate(titulos):
            print(f"{i+1}. {item}")
            select.append(item)
        vetSearch = select[int(input(">"))-1]
        opc = "Especialidad"
    else:
        print("seleccion no valida")
        return False
    
    for i, item in enumerate(diccVet["data"]):
        if vetSearch in item["Nombre"] or vetSearch in item["Titulo"]:
            save.append(item)

    if (len(save)==1):
        return (['VETERINARIO ENCONTRADO',save,opc,vetSearch])
    elif (len(save)>1):
        return ([f'{len(save)} VETERINARIOS ENCONTRADOS',save,opc,vetSearch])
    else:
        return False

def MostrarVeterinario():
    diccVet = LoadDataVeterinarios("veterinarios.json")
    save = []
    print('+','-'*55,'+')
    print("|{:^57}|".format('BUSCADOR INFORMACION DE VETERINARIOS'))
    print('+','-'*55,'+')
    vetSearch = int(input("Ingrese el id del veterinario a buscar: "))
    for i, item in enumerate(diccVet["data"]):
        if vetSearch == item["Id"]:
            save.append(item)
    if (len(save)==1):
        return save
    else:
        return False