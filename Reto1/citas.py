import os
import core

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
    diccPaci = LoadDataCitas("pacientes.json")
    print ('+','-'*55,'+')
    print ('|{:^57}|'.format('MENU CITAS'))
    print ('+','-'*55,'+')