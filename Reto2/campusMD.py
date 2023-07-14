import os
import core

diccCitas = {"data": []}

def LoadDataCitas(args):
    global diccCitas
    if core.CheckData(args):
        return core.LoadData(args)
    else:
        core.CreateData(args, diccCitas) 
        return core.LoadData(args)

if __name__ == '__main__':
    run = True
    while run:
        os.system('clear')
        diccCitas = LoadDataCitas("citas.json")
        print ('+','-'*55,'+')
        print ('|{:^57}|'.format('MENU CITAS'))
        print ('+','-'*55,'+')
        print ("1. Agregar Cita","2. Buscar cita","3. Modificar cita","4. Cancelar Cita","5. Salir",sep="\n")
        opc = int(input("> "))
        os.system("clear")
        if opc == 1:
            print ('+','-'*55,'+')
            print ('|{:^57}|'.format('AGREGAR CITA'))
            print ('+','-'*55,'+')
            print("Ingrese los datos del paciente")
            nombre = input("Nombre: ")
            fecha = input("Fecha: ")
            hora = input("Hora: ")
            motivo = input("Motivo Consulta: ")
            data = {
                "Nombre": nombre,
                "Fecha": fecha,
                "Hora": hora,
                "Motivo": motivo
            }
            core.CreateData("citas.json",data)
            print ('+','-'*55,'+')
            print ('|{:^57}|'.format('CITA AGREGADA CORECTAMENTE'))
            print ('+','-'*55,'+')
        elif opc == 2:
            found = False
            band = 1
            print ('+','-'*55,'+')
            print ('|{:^57}|'.format('BUSCAR CITA'))
            print ('+','-'*55,'+')
            print("dato de busqueda","1. Nombre","2. Fecha","3. Motivo",sep="\n")
            dato = int(input("> "))-1
            keys = list(diccCitas["data"][0])
            keys.remove("Hora")
            search = input(f"ingrese {keys[dato]}: ")
            for i, item in enumerate(diccCitas["data"]):
                if search in item.values():
                    if band == 1:
                        os.system("clear")  
                        print ('+','-'*59,'+')
                        print ('|{:^61}|'.format('DATO ENCONTRADO'))
                        print ('+','-'*59,'+')
                        print('|{:^13}|{:^12}|{:^8}|{:^25}|'.format("Nombre", "Fecha", "Hora", "Motivo"))
                        print ('+','-'*59,'+')
                        band = 0
                    print('|{:^13}|{:^12}|{:^8}|{:^25}|'.format(item["Nombre"], item["Fecha"], item["Hora"], item["Motivo"]))
                    print ('+','-'*59,'+')
                    found = True
            if not found:
                print ('+','-'*55,'+')
                print ('|{:^57}|'.format('DATO NO ENCONTRADO'))
                print ('+','-'*55,'+')              
        elif opc == 3:
            print ('+','-'*64,'+')
            print ('|{:^66}|'.format('MODIFICAR CITA'))
            print ('+','-'*64,'+')
            print('|{:^4}|{:^13}|{:^12}|{:^8}|{:^25}|'.format("nro","Nombre", "Fecha", "Hora", "Motivo"))
            print ('+','-'*64,'+')
            for i, item in enumerate(diccCitas["data"]):
                print('|{:^4}|{:^13}|{:^12}|{:^8}|{:^25}|'.format(i+1, item["Nombre"], item["Fecha"], item["Hora"], item["Motivo"]))
                print ('+','-'*64,'+')
            print("Ingrese el numero de la cita a modificar")
            save = diccCitas["data"][select := int(input("> "))-1]
            os.system("clear")
            save["Nombre"] = input("ingrese el nuevo nombre: ") or save["Nombre"]
            save["Fecha"] = input("ingrese la nueva Fecha: ") or save["Fecha"]
            save["Hora"] = input("ingrese la nueva Hora: ") or save["Hora"]
            save["Motivo"] = input("ingrese el nuevo Motivo: ") or save["Motivo"]

            diccCitas["data"][select] = save
            print(diccCitas)
            core.EditData("citas.json", diccCitas)
        elif opc == 4:
            print ('+','-'*64,'+')
            print ('|{:^66}|'.format('MODIFICAR CITA'))
            print ('+','-'*64,'+')
            print('|{:^4}|{:^13}|{:^12}|{:^8}|{:^25}|'.format("nro","Nombre", "Fecha", "Hora", "Motivo"))
            print ('+','-'*64,'+')
            for i, item in enumerate(diccCitas["data"]):
                print('|{:^4}|{:^13}|{:^12}|{:^8}|{:^25}|'.format(i+1, item["Nombre"], item["Fecha"], item["Hora"], item["Motivo"]))
                print ('+','-'*64,'+')
            print("Ingrese el numero de la cita a Eliminar")
        elif opc == 5:
            print("⠀╭ ◜◝ ͡ ◝ ͡ ◜◝╮","(   Chaito   )","╰ ͜ ⠀ ͜   ͜   ͜  ╯","        O","         o","         °","〃∩ _∧＿∧_♡","  |('・ω・）♡"," ¨ヽ_っ＿/￣￣￣/","　    ＼/＿＿＿/",sep="\n")
            run = False
        input("Presione Enter para continuar")
