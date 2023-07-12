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
    os.system("clear")
    exit = False
    diccPaci = LoadDataVet("pacientes.json")
    print ('+','-'*55,'+')
    print ('|{:^57}|'.format('MENU VETERINARIOS'))
    print ('+','-'*55,'+')